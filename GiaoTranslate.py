# -*- coding:utf-8 -*-
import hashlib
import random
import sys
import time
import pyperclip
import requests
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QDesktopWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QCoreApplication
from pynput import keyboard
from qfluentwidgets import FluentIcon, Flyout, InfoBarIcon, FlyoutAnimationType, \
    RoundMenu, Action, ToolTipFilter, ToolTipPosition
# from youdao_translation import Translate
from Ui import Ui_Form
from Screenshot import WScreenShot
from Ocr import Ocr
from youdao import Translate

class ModeTranslate(object):
    def __init__(self, mode = None):
        self.mode = mode

    def get_translate_result(self, text, tolang = None):
        print(self.mode, text, tolang)
        if self.mode == 'Baidu':

            T = BaiduT()
            if tolang == 'English':
                tolang = 'en'
            elif tolang == 'Chinese':
                tolang = 'zh'
            print(self.mode, text, tolang, type(tolang), tolang == "Chinese")
            return T.get_translate_result(text, tolang)
        else:
            T = Translate(text)
            result = T.get_result()
            print(result)
            return result

class MyDiy(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self.window())

        # 系统窗口和托盘初始化
        self.tray_icon = QSystemTrayIcon(self)  # 初始化系统托盘图标
        self.menu = RoundMenu()  # 创建右键菜单
        self.sys_window_init()

        # 下拉按钮内容初始化
        self.lang_items = ['English', 'Chinese']
        self.mode_items = ['Baidu', 'Google', 'Deepl', 'Youdao']
        self.ComboBox_init()

        # 鼠标聚焦提示初始化
        self.tooltip_set_init()

        self.auto_flag = True  # True 开启自动，锁定转换按钮
        self.auto_mode.setChecked(True)
        self.change.setEnabled(False)

        self.signTodef()

        self.Monitor = Background_Monitor_Thread()
        self.Monitor.dataProcessed.connect(self.Monitor_print)
        self.Monitor.start()
        self.translate_thread = None
        self.dialog = None
        self.change_x_position = 50
        self.change_y_position = 20
        self.max_window_w = 500
        self.win = None

    # 系统窗口和托盘初始化
    def sys_window_init(self):
        # 初始化系统托盘图标
        self.tray_icon.setIcon(QIcon(":/static/static/T.png"))
        self.tray_icon.show()
        # 创建右键菜单

        self.menu.addAction(Action(FluentIcon.HOME, '主界面', triggered = lambda: self.showNormal()))
        self.menu.addAction(Action(FluentIcon.IMAGE_EXPORT, 'OCR', triggered = lambda: self.screenshot()))
        self.menu.addAction(Action(FluentIcon.SETTING, '设置'))
        self.menu.addAction(Action(FluentIcon.CLOSE, '退出', triggered = lambda: QCoreApplication.instance().quit()))

        # 设置系统托盘图标的上下文菜单
        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.activated.connect(self.menu_double_click)
        self.setWindowOpacity(0.8)  # 50% 透明度
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setLayout(self.mainLayout)
        self.setWindowIcon(QIcon(":/static/static/T.png"))
        self.setWindowTitle("Giao-Translate")

    def screenshot(self):
        if not hasattr(self, 'win') or self.win is None:
            self.win = WScreenShot()
            self.win.creenshothide.connect(lambda: self.creenshothide_())
        self.win.show()

    def creenshothide_(self):
        size = self.size()
        # 屏幕尺寸
        screen = QApplication.instance().primaryScreen()
        screen_size = screen.geometry().size()

        # 计算窗口居中的位置
        self.move((screen_size.width() - size.width()) // 2,
                  (screen_size.height() - size.height()) // 2)
        self.show()
        try:
            str_ = Ocr()
            print(f'|{str_}|')
            self.data.setPlainText(str_)
            self.translate_()

        except:
            self.data.setPlainText('网路错误  or  接口返回数据错误！！！')
            self.data.setPlainText('网路错误  or  接口返回数据错误！！！')

    # 鼠标聚焦提示初始化
    def tooltip_set_init(self):
        self.close_.setToolTip('最小化到系统托盘✨')
        self.close_.installEventFilter(ToolTipFilter(self.close_, showDelay = 500, position = ToolTipPosition.TOP))
        self.min_.setToolTip('缩小窗口尺寸✨')
        self.min_.installEventFilter(ToolTipFilter(self.min_, showDelay = 500, position = ToolTipPosition.TOP))
        self.max_.setToolTip('放大窗口尺寸✨')
        self.max_.installEventFilter(ToolTipFilter(self.max_, showDelay = 500, position = ToolTipPosition.TOP))
        self.set_.setToolTip('更多功能开发中噢~~✨')
        self.set_.installEventFilter(ToolTipFilter(self.set_, showDelay = 500, position = ToolTipPosition.TOP))
        self.auto_mode.setToolTip('自动设别翻译语言 个别API还不支持噢~~😄✨')
        self.auto_mode.installEventFilter(ToolTipFilter(self.auto_mode, showDelay = 500, position = ToolTipPosition.TOP))
        self.change.setToolTip('到处乱看什么啊~老弟✨')
        self.change.installEventFilter(ToolTipFilter(self.change, showDelay = 500, position = ToolTipPosition.TOP))
        self.mainicon.setToolTip('em~~吃个桃桃✨')
        self.mainicon.installEventFilter(ToolTipFilter(self.mainicon, showDelay = 500, position = ToolTipPosition.TOP))
        self.translate.setToolTip('还在等什么 GO GO GO!✨')
        self.translate.installEventFilter(ToolTipFilter(self.translate, showDelay = 500, position = ToolTipPosition.TOP))
        self.changemode.setToolTip('现在只支持有道翻译 选其他的也没用！！!✨')
        self.changemode.installEventFilter(ToolTipFilter(self.changemode, showDelay = 500, position = ToolTipPosition.TOP))

    # 下拉按钮内容初始化
    def ComboBox_init(self):
        self.change1.addItems(self.lang_items)
        self.change1.setCurrentIndex(0)
        self.change2.addItems(self.lang_items)
        self.change2.setCurrentIndex(1)
        self.changemode.addItems(self.mode_items)
        self.changemode.setCurrentIndex(3)

    # 托盘图标被双击
    def menu_double_click(self, reason):
        # 检查双击事件
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()

    # 托盘选择主界面
    def menu_home(self):
        self.showNormal()

    def menu_set(self):
        pass

    # 各个信号与各个槽的链接
    def signTodef(self):
        self.set_.clicked.connect(lambda: self.open_setwindow())
        self.translate.clicked.connect(lambda: self.translate_())
        self.auto_mode.clicked.connect(lambda: self.auto_mode_())
        self.change.clicked.connect(lambda: self.change_())
        self.changemode.currentIndexChanged.connect(lambda: self.changemode_())
        self.min_.clicked.connect(lambda: self.min_window())
        self.close_.clicked.connect(lambda: self.close_window())
        self.max_.clicked.connect(lambda: self.max_window())

    # 翻译接口选择回调函数
    def changemode_(self):
        pass

    # 缩小按钮点击执行
    def min_window(self):
        screen = QDesktopWidget().screenGeometry()
        # 计算窗口位置
        x_ = 200
        y_ = 200
        x = (screen.width() - x_) // 2
        y = (screen.height() - y_) // 2
        # 移动窗口到计算出的位置
        self.resize(x_, y_)
        self.move(x, y)

    # 放大窗口按钮点击执行
    def max_window(self):
        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        # 计算窗口位置
        x = (screen.width() - (screen.width() // 2)) // 2
        y = (screen.height() - (screen.height() // 2)) // 2
        # 移动窗口到计算出的位置
        self.resize(screen.width() // 2, screen.height() // 2)
        self.move(x, y)

    # 设置按钮点击执行
    def open_setwindow(self):
        Flyout.create(
            icon = InfoBarIcon.INFORMATION,
            title = 'INFO',
            content = "更多功能开发中噢~~~~~",
            target = self.set_,
            parent = self,
            isClosable = True,
            aniType = FlyoutAnimationType.PULL_UP
        )

    # 关闭按钮点击执行
    def close_window(self):
        self.hide()
        # self.dialog = Dialog("尊嘟假嘟~", "哥哥要让我走吗！！呜呜呜~", self)
        # self.dialog.yesButton.setText("最小化到系统托盘")
        # self.dialog.cancelButton.setText("不要你了！！M3~")
        # if_close = self.dialog.exec()
        # if if_close:
        #     self.hide()
        #     self.tray_icon.show()
        #     print('确认')
        # else:
        #     print('取消')

    # 互换按钮点击执行
    def change_(self):
        change1_index = self.lang_items.index(self.change2.text())
        change2_index = self.lang_items.index(self.change1.text())
        self.change1.setCurrentIndex(change1_index)
        self.change2.setCurrentIndex(change2_index)

    # 自动按钮点击执行
    def auto_mode_(self):
        if not self.auto_flag:
            print('自动')
            self.change.setEnabled(False)
            self.auto_flag = True
        else:
            print('手动')
            self.change.setEnabled(True)
            self.auto_flag = False

    # 翻译按钮点击执行
    def translate_(self):
        mode = self.changemode.text()
        t1 = self.change1.text()
        t2 = self.change2.text()
        text = self.data.toPlainText()
        data = {
            'tolang': t2,
            'text': text,
            'mode': mode
        }
        # 开启线程进行网络请求
        if text:
            self.translate_thread = WorkThread(data = data, class_ = ModeTranslate)  # 加self才行
            self.translate_thread.dataProcessed.connect(self.set_data_text)
            self.translate_thread.start()
        else:
            Flyout.create(
                icon = InfoBarIcon.WARNING,
                title = 'WARNING',
                content = "准备让我翻译空气吗🐎..\n自己去看看是不是快捷键冲突了👿",
                target = self.data,
                parent = self,
                isClosable = True,
                aniType = FlyoutAnimationType.PULL_UP
            )

    # 翻译按键回调，显示翻译结果
    def set_data_text(self, data):
        self.result.setPlainText(data['result'].replace('    ', '💨\n'))

    # 快捷键检测回调函数
    def Monitor_print(self, data):
        self.data.setPlainText(data)
        self.translate_()
        # 设置窗口在鼠标出显示
        print(self.isHidden())
        if self.isHidden():
            mouse_position = QCursor.pos()
            x = mouse_position.x()
            y = mouse_position.y()
            self.move(x + self.change_x_position, y - self.change_y_position)
            self.show()

    #  鼠标窗口可移动，函数重写
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  #获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QtGui.QCursor(Qt.CustomCursor))  #更改鼠标图标

    #  鼠标窗口可移动，函数重写
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  #更改窗口位置
            QMouseEvent.accept()

    #  鼠标窗口可移动，函数重写
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

# 翻译接口请求线程
class WorkThread(QThread):
    dataProcessed = pyqtSignal(dict)  # 更有描述性的信号名

    def __init__(self, class_ = None, data = None, parent = None):
        super().__init__(parent)
        self.data = data
        self.text = data['text']
        self.tolang = data['tolang']
        self.mode = data['mode']
        self.class_ = class_(self.mode)

    def run(self):
        result = self.class_.get_translate_result(text = self.text, tolang = self.tolang)
        self.dataProcessed.emit(result)

# 键盘监控线程
class Background_Monitor_Thread(QThread):
    dataProcessed = pyqtSignal(str)  # 更有描述性的信号名

    def __init__(self, parent = None):
        super().__init__(parent)
        self.keyboard_ = keyboard.Controller()

    def run(self):
        print('键盘监听已开启')
        self.keyboard_listener()

    """  按下 ctrl + c """

    def press_ctrl_c(self):
        with self.keyboard_.pressed(keyboard.Key.ctrl):
            self.keyboard_.press('c')
            self.keyboard_.release('c')
            time.sleep(0.1)

    # 定义键盘监听器函数
    def keyboard_listener(self):
        with keyboard.Listener(
                on_press = self.on_press,  # 定义按下键盘时的回调函数
        ) as listener:
            listener.join()

    # 定义按下键盘时的回调函数
    def on_press(self, key):
        try:
            if key.char == '\x11':  # 组合键ctrl + c 为\x11
                self.press_ctrl_c()
                paste_data = pyperclip.paste()
                pyperclip.copy('')
                self.dataProcessed.emit(paste_data)
        except AttributeError:
            pass

class BaiduT:
    def __init__(self):
        self.data = {}

    def get_translate_result(self, text, toLang):  # toLang = 'zh'  # 译文语种

        try:
            appid = '20240814002123485'  # 填写你的appid
            secretKey = 'gDUR3d5uQhIUYSg0bxOr'  # 填写你的密钥
            myurl = 'https://api.fanyi.baidu.com/api/trans/vip/translate'  # 通用翻译API HTTP地址
            fromLang = 'auto'  # 原文语种
            salt = random.randint(32768, 65536)
            # 手动录入翻译内容，q存放
            sign = appid + text + str(salt) + secretKey
            sign = hashlib.md5(sign.encode()).hexdigest()
            myurl = myurl + '?appid=' + appid + '&q=' + text + '&from=' + fromLang + \
                '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
            # 建立会话，返回结果
            self.data = requests.get(url = myurl).json()
            return {
                'code': 0,
                'result': self.data["trans_result"][0]["dst"],
                'src': self.data["trans_result"][0]['src'],
                'type': f'{self.data["from"]}->{self.data["to"]}'
            }
        except:
            return {
                'code': 1,
                'result': f'网路错误  or  接口返回数据错误！！！'
            }

if __name__ == '__main__':
    # QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = MyDiy()
    w.show()
    app.exec()
