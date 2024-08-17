# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(381, 188)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/static/static/桃.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setToolTipDuration(0)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(True)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 187))
        self.layoutWidget.setObjectName("layoutWidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainicon = ImageLabel(self.layoutWidget)
        self.mainicon.setMinimumSize(QtCore.QSize(30, 30))
        self.mainicon.setMaximumSize(QtCore.QSize(30, 30))
        self.mainicon.setPixmap(QtGui.QPixmap(":/static/static/桃.png"))
        self.mainicon.setObjectName("mainicon")
        self.horizontalLayout.addWidget(self.mainicon)
        self.changemode = EditableComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changemode.sizePolicy().hasHeightForWidth())
        self.changemode.setSizePolicy(sizePolicy)
        self.changemode.setMinimumSize(QtCore.QSize(0, 30))
        self.changemode.setMaximumSize(QtCore.QSize(120, 30))
        self.changemode.setFrame(True)
        self.changemode.setReadOnly(True)
        self.changemode.setObjectName("changemode")
        self.horizontalLayout.addWidget(self.changemode)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.set_ = ToolButton(self.layoutWidget)
        self.set_.setMaximumSize(QtCore.QSize(30, 30))
        self.set_.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/static/static/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_.setIcon(icon1)
        self.set_.setObjectName("set_")
        self.horizontalLayout.addWidget(self.set_)
        self.min_ = ToolButton(self.layoutWidget)
        self.min_.setMaximumSize(QtCore.QSize(30, 30))
        self.min_.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/static/static/最小化2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min_.setIcon(icon2)
        self.min_.setObjectName("min_")
        self.horizontalLayout.addWidget(self.min_)
        self.max_ = ToolButton(self.layoutWidget)
        self.max_.setMaximumSize(QtCore.QSize(30, 30))
        self.max_.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/static/static/最大化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_.setIcon(icon3)
        self.max_.setObjectName("max_")
        self.horizontalLayout.addWidget(self.max_)
        self.close_ = ToolButton(self.layoutWidget)
        self.close_.setMaximumSize(QtCore.QSize(30, 30))
        self.close_.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/static/static/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_.setIcon(icon4)
        self.close_.setObjectName("close_")
        self.horizontalLayout.addWidget(self.close_)
        self.mainLayout.addLayout(self.horizontalLayout)
        self.data = PlainTextEdit(self.layoutWidget)
        self.data.setMinimumSize(QtCore.QSize(0, 50))
        self.data.setObjectName("data")
        self.mainLayout.addWidget(self.data)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.change1 = ComboBox(self.layoutWidget)
        self.change1.setMaximumSize(QtCore.QSize(130, 30))
        self.change1.setObjectName("change1")
        self.horizontalLayout_2.addWidget(self.change1)
        self.change = ToolButton(self.layoutWidget)
        self.change.setMaximumSize(QtCore.QSize(50, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/static/static/交换.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change.setIcon(icon5)
        self.change.setObjectName("change")
        self.horizontalLayout_2.addWidget(self.change)
        self.change2 = ComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change2.sizePolicy().hasHeightForWidth())
        self.change2.setSizePolicy(sizePolicy)
        self.change2.setMaximumSize(QtCore.QSize(130, 30))
        self.change2.setObjectName("change2")
        self.horizontalLayout_2.addWidget(self.change2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.auto_mode = PillToolButton(self.layoutWidget)
        self.auto_mode.setMaximumSize(QtCore.QSize(40, 30))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/static/static/自动.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.auto_mode.setIcon(icon6)
        self.auto_mode.setIconSize(QtCore.QSize(25, 25))
        self.auto_mode.setObjectName("auto_mode")
        self.horizontalLayout_2.addWidget(self.auto_mode)
        self.translate = PushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translate.sizePolicy().hasHeightForWidth())
        self.translate.setSizePolicy(sizePolicy)
        self.translate.setMaximumSize(QtCore.QSize(80, 30))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/static/static/翻译2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.translate.setIcon(icon7)
        self.translate.setIconSize(QtCore.QSize(20, 20))
        self.translate.setObjectName("translate")
        self.horizontalLayout_2.addWidget(self.translate)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.mainLayout.addLayout(self.horizontalLayout_2)
        self.result = PlainTextEdit(self.layoutWidget)
        self.result.setMinimumSize(QtCore.QSize(0, 50))
        self.result.setPlainText("")
        self.result.setObjectName("result")
        self.mainLayout.addWidget(self.result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.data.setPlaceholderText(_translate("Form", "输入需要翻译的文本"))
        self.translate.setText(_translate("Form", "翻译"))
        self.result.setPlaceholderText(_translate("Form", "结果展示"))
from qfluentwidgets import ComboBox, EditableComboBox, ImageLabel, PillToolButton, PlainTextEdit, PushButton, ToolButton
import qrc_rc
