# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt, QPoint)
from PySide2.QtGui import (QBrush, QColor, QFont,
                           QIcon, QPalette, QPixmap)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 729)
        MainWindow.setMinimumSize(QSize(1035, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(210, 210, 210, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(210, 210, 210, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(66, 73, 90))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        brush = QBrush(QColor(55, 61, 75))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        brush = QBrush(QColor(29, 32, 40))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        brush = QBrush(QColor(22, 24, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush = QBrush(QColor(51, 153, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        brush = QBrush(QColor(85, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(44, 49, 60))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(210, 210, 210))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(210, 210, 210, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QSize(1035, 720))
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_36 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("/* LINE EDIT */\n"
"QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(icons/16x16/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);    \n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(icons/32x32/show.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu.setText("")
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"background-image: url(icons/24x24/video-camera.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setLayoutDirection(Qt.LeftToRight)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QFrame(self.frame_top_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_minimize = QPushButton(self.frame_btns_right)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/16x16/cil-window-minimize.png"), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_5.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/16x16/cil-window-maximize.png"), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)
        self.btn_close = QPushButton(self.frame_btns_right)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/16x16/cil-x.png"), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setFlat(False)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_top_btns)
        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setMaximumSize(QSize(16777215, 100))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet("color: #ffffff; ")
        self.label_top_info_1.setObjectName("label_top_info_1")
        self.horizontalLayout_8.addWidget(self.label_top_info_1)
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QFrame(self.frame_main)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QFrame(self.frame_center)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.frame_menus.setObjectName("frame_menus")
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName("layout_menus")
        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)
        self.frame_extra_menus = QFrame(self.frame_left_menu)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName("layout_menu_bottom")
        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_report = QWidget()
        self.page_report.setObjectName("page_report")
        self.verticalLayout_6 = QVBoxLayout(self.page_report)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QFrame(self.page_report)
        self.frame.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setMaximumSize(QSize(16777215, 89))
        self.frame_2.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QLabel(self.frame_2)
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.comboBox = QComboBox(self.frame_2)
        font = QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QComboBox::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QSize(350, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_2 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2)
        self.label_3 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_13.addWidget(self.label_3)
        self.label_4 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_13.addWidget(self.label_4)
        self.label_5 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.label_30 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_13.addWidget(self.label_30)
        self.label_6 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.label_7 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.label_8 = QLabel(self.frame_7)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.verticalLayout_10.addWidget(self.frame_7)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_29 = QVBoxLayout(self.frame_8)
        self.verticalLayout_29.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame_34 = QFrame(self.frame_8)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_31 = QVBoxLayout(self.frame_36)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_20.addWidget(self.frame_36)
        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_32 = QVBoxLayout(self.frame_37)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.pushButton_98 = QPushButton(self.frame_37)
        self.pushButton_98.setMaximumSize(QSize(170, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.pushButton_98.setFont(font)
        self.pushButton_98.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_98.setObjectName("pushButton_98")
        self.verticalLayout_32.addWidget(self.pushButton_98)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_33 = QVBoxLayout(self.frame_38)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_32.addWidget(self.frame_38)
        self.horizontalLayout_20.addWidget(self.frame_37)
        self.verticalLayout_29.addWidget(self.frame_34)
        self.frame_35 = QFrame(self.frame_8)
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_30 = QVBoxLayout(self.frame_35)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_29.addWidget(self.frame_35)
        self.verticalLayout_10.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setContentsMargins(20, 5, 5, 5)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QLabel(self.frame_5)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.plainTextEdit = QPlainTextEdit(self.frame_5)
        font = QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_12.addWidget(self.plainTextEdit)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QPushButton(self.frame_6)
        font = QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.frame_6)
        font = QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_report)
        self.page_bill = QWidget()
        self.page_bill.setObjectName("page_bill")
        self.verticalLayout_17 = QVBoxLayout(self.page_bill)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_9 = QFrame(self.page_bill)
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setMaximumSize(QSize(16777215, 89))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_21 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 8)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_42 = QFrame(self.frame_10)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.verticalLayout_35 = QVBoxLayout(self.frame_42)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_10 = QLabel(self.frame_42)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_35.addWidget(self.label_10)
        self.comboBox_2 = QComboBox(self.frame_42)
        self.comboBox_2.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QComboBox::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_35.addWidget(self.comboBox_2)
        self.horizontalLayout_21.addWidget(self.frame_42)
        self.frame_43 = QFrame(self.frame_10)
        self.frame_43.setMaximumSize(QSize(340, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.verticalLayout_16 = QVBoxLayout(self.frame_43)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_31 = QLabel(self.frame_43)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_16.addWidget(self.label_31)
        self.comboBox_4 = QComboBox(self.frame_43)
        self.comboBox_4.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("QComboBox {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QComboBox::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_16.addWidget(self.comboBox_4)
        self.horizontalLayout_21.addWidget(self.frame_43)
        self.verticalLayout_14.addWidget(self.frame_10)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_19 = QFrame(self.frame_11)
        font = QFont()
        font.setPointSize(12)
        self.frame_19.setFont(font)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_18 = QVBoxLayout(self.frame_19)
        self.verticalLayout_18.setContentsMargins(-1, 20, -1, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_13 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_18.addWidget(self.label_13)
        self.label_15 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_18.addWidget(self.label_15)
        self.label_17 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_18.addWidget(self.label_17)
        self.label_16 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_18.addWidget(self.label_16)
        self.label_14 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_18.addWidget(self.label_14)
        self.label_11 = QLabel(self.frame_19)
        font = QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_18.addWidget(self.label_11)
        self.horizontalLayout_9.addWidget(self.frame_19)
        self.frame_18 = QFrame(self.frame_11)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_12 = QFrame(self.frame_18)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_3 = QPushButton(self.frame_12)
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.frame_12)
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_5 = QPushButton(self.frame_12)
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.frame_12)
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.pushButton_7 = QPushButton(self.frame_12)
        self.pushButton_7.setMinimumSize(QSize(50, 50))
        self.pushButton_7.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_8 = QPushButton(self.frame_12)
        self.pushButton_8.setMinimumSize(QSize(50, 50))
        self.pushButton_8.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.pushButton_9 = QPushButton(self.frame_12)
        self.pushButton_9.setMinimumSize(QSize(50, 50))
        self.pushButton_9.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setMinimumSize(QSize(50, 50))
        self.pushButton_10.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setMinimumSize(QSize(50, 50))
        self.pushButton_11.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_7.addWidget(self.pushButton_11)
        self.pushButton_12 = QPushButton(self.frame_12)
        self.pushButton_12.setMinimumSize(QSize(50, 50))
        self.pushButton_12.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_7.addWidget(self.pushButton_12)
        self.pushButton_17 = QPushButton(self.frame_12)
        self.pushButton_17.setMinimumSize(QSize(50, 50))
        self.pushButton_17.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_7.addWidget(self.pushButton_17)
        self.pushButton_16 = QPushButton(self.frame_12)
        self.pushButton_16.setMinimumSize(QSize(50, 50))
        self.pushButton_16.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_7.addWidget(self.pushButton_16)
        self.pushButton_15 = QPushButton(self.frame_12)
        self.pushButton_15.setMinimumSize(QSize(50, 50))
        self.pushButton_15.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_7.addWidget(self.pushButton_15)
        self.pushButton_14 = QPushButton(self.frame_12)
        self.pushButton_14.setMinimumSize(QSize(50, 50))
        self.pushButton_14.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_7.addWidget(self.pushButton_14)
        self.pushButton_13 = QPushButton(self.frame_12)
        self.pushButton_13.setMinimumSize(QSize(50, 50))
        self.pushButton_13.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_7.addWidget(self.pushButton_13)
        self.verticalLayout_15.addWidget(self.frame_12)
        self.frame_13 = QFrame(self.frame_18)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_20 = QPushButton(self.frame_13)
        self.pushButton_20.setMinimumSize(QSize(50, 50))
        self.pushButton_20.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_11.addWidget(self.pushButton_20)
        self.pushButton_28 = QPushButton(self.frame_13)
        self.pushButton_28.setMinimumSize(QSize(50, 50))
        self.pushButton_28.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_11.addWidget(self.pushButton_28)
        self.pushButton_26 = QPushButton(self.frame_13)
        self.pushButton_26.setMinimumSize(QSize(50, 50))
        self.pushButton_26.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_11.addWidget(self.pushButton_26)
        self.pushButton_19 = QPushButton(self.frame_13)
        self.pushButton_19.setMinimumSize(QSize(50, 50))
        self.pushButton_19.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_11.addWidget(self.pushButton_19)
        self.pushButton_32 = QPushButton(self.frame_13)
        self.pushButton_32.setMinimumSize(QSize(50, 50))
        self.pushButton_32.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_11.addWidget(self.pushButton_32)
        self.pushButton_29 = QPushButton(self.frame_13)
        self.pushButton_29.setMinimumSize(QSize(50, 50))
        self.pushButton_29.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_11.addWidget(self.pushButton_29)
        self.pushButton_30 = QPushButton(self.frame_13)
        self.pushButton_30.setMinimumSize(QSize(50, 50))
        self.pushButton_30.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_11.addWidget(self.pushButton_30)
        self.pushButton_21 = QPushButton(self.frame_13)
        self.pushButton_21.setMinimumSize(QSize(50, 50))
        self.pushButton_21.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_11.addWidget(self.pushButton_21)
        self.pushButton_22 = QPushButton(self.frame_13)
        self.pushButton_22.setMinimumSize(QSize(50, 50))
        self.pushButton_22.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_11.addWidget(self.pushButton_22)
        self.pushButton_23 = QPushButton(self.frame_13)
        self.pushButton_23.setMinimumSize(QSize(50, 50))
        self.pushButton_23.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_11.addWidget(self.pushButton_23)
        self.pushButton_31 = QPushButton(self.frame_13)
        self.pushButton_31.setMinimumSize(QSize(50, 50))
        self.pushButton_31.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_11.addWidget(self.pushButton_31)
        self.pushButton_24 = QPushButton(self.frame_13)
        self.pushButton_24.setMinimumSize(QSize(50, 50))
        self.pushButton_24.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_11.addWidget(self.pushButton_24)
        self.pushButton_25 = QPushButton(self.frame_13)
        self.pushButton_25.setMinimumSize(QSize(50, 50))
        self.pushButton_25.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_11.addWidget(self.pushButton_25)
        self.pushButton_27 = QPushButton(self.frame_13)
        self.pushButton_27.setMinimumSize(QSize(50, 50))
        self.pushButton_27.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_11.addWidget(self.pushButton_27)
        self.pushButton_18 = QPushButton(self.frame_13)
        self.pushButton_18.setMinimumSize(QSize(50, 50))
        self.pushButton_18.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_11.addWidget(self.pushButton_18)
        self.verticalLayout_15.addWidget(self.frame_13)
        self.frame_14 = QFrame(self.frame_18)
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_35 = QPushButton(self.frame_14)
        self.pushButton_35.setMinimumSize(QSize(50, 50))
        self.pushButton_35.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_12.addWidget(self.pushButton_35)
        self.pushButton_43 = QPushButton(self.frame_14)
        self.pushButton_43.setMinimumSize(QSize(50, 50))
        self.pushButton_43.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_43.setObjectName("pushButton_43")
        self.horizontalLayout_12.addWidget(self.pushButton_43)
        self.pushButton_41 = QPushButton(self.frame_14)
        self.pushButton_41.setMinimumSize(QSize(50, 50))
        self.pushButton_41.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_41.setObjectName("pushButton_41")
        self.horizontalLayout_12.addWidget(self.pushButton_41)
        self.pushButton_34 = QPushButton(self.frame_14)
        self.pushButton_34.setMinimumSize(QSize(50, 50))
        self.pushButton_34.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_12.addWidget(self.pushButton_34)
        self.pushButton_47 = QPushButton(self.frame_14)
        self.pushButton_47.setMinimumSize(QSize(50, 50))
        self.pushButton_47.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_47.setObjectName("pushButton_47")
        self.horizontalLayout_12.addWidget(self.pushButton_47)
        self.pushButton_44 = QPushButton(self.frame_14)
        self.pushButton_44.setMinimumSize(QSize(50, 50))
        self.pushButton_44.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_44.setObjectName("pushButton_44")
        self.horizontalLayout_12.addWidget(self.pushButton_44)
        self.pushButton_45 = QPushButton(self.frame_14)
        self.pushButton_45.setMinimumSize(QSize(50, 50))
        self.pushButton_45.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_45.setObjectName("pushButton_45")
        self.horizontalLayout_12.addWidget(self.pushButton_45)
        self.pushButton_36 = QPushButton(self.frame_14)
        self.pushButton_36.setMinimumSize(QSize(50, 50))
        self.pushButton_36.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_12.addWidget(self.pushButton_36)
        self.pushButton_37 = QPushButton(self.frame_14)
        self.pushButton_37.setMinimumSize(QSize(50, 50))
        self.pushButton_37.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_37.setObjectName("pushButton_37")
        self.horizontalLayout_12.addWidget(self.pushButton_37)
        self.pushButton_38 = QPushButton(self.frame_14)
        self.pushButton_38.setMinimumSize(QSize(50, 50))
        self.pushButton_38.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout_12.addWidget(self.pushButton_38)
        self.pushButton_46 = QPushButton(self.frame_14)
        self.pushButton_46.setMinimumSize(QSize(50, 50))
        self.pushButton_46.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_46.setObjectName("pushButton_46")
        self.horizontalLayout_12.addWidget(self.pushButton_46)
        self.pushButton_39 = QPushButton(self.frame_14)
        self.pushButton_39.setMinimumSize(QSize(50, 50))
        self.pushButton_39.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_39.setObjectName("pushButton_39")
        self.horizontalLayout_12.addWidget(self.pushButton_39)
        self.pushButton_40 = QPushButton(self.frame_14)
        self.pushButton_40.setMinimumSize(QSize(50, 50))
        self.pushButton_40.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_12.addWidget(self.pushButton_40)
        self.pushButton_42 = QPushButton(self.frame_14)
        self.pushButton_42.setMinimumSize(QSize(50, 50))
        self.pushButton_42.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_42.setObjectName("pushButton_42")
        self.horizontalLayout_12.addWidget(self.pushButton_42)
        self.pushButton_33 = QPushButton(self.frame_14)
        self.pushButton_33.setMinimumSize(QSize(50, 50))
        self.pushButton_33.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_12.addWidget(self.pushButton_33)
        self.verticalLayout_15.addWidget(self.frame_14)
        self.frame_15 = QFrame(self.frame_18)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_50 = QPushButton(self.frame_15)
        self.pushButton_50.setMinimumSize(QSize(50, 50))
        self.pushButton_50.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_50.setObjectName("pushButton_50")
        self.horizontalLayout_13.addWidget(self.pushButton_50)
        self.pushButton_58 = QPushButton(self.frame_15)
        self.pushButton_58.setMinimumSize(QSize(50, 50))
        self.pushButton_58.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_58.setObjectName("pushButton_58")
        self.horizontalLayout_13.addWidget(self.pushButton_58)
        self.pushButton_56 = QPushButton(self.frame_15)
        self.pushButton_56.setMinimumSize(QSize(50, 50))
        self.pushButton_56.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_56.setObjectName("pushButton_56")
        self.horizontalLayout_13.addWidget(self.pushButton_56)
        self.pushButton_49 = QPushButton(self.frame_15)
        self.pushButton_49.setMinimumSize(QSize(50, 50))
        self.pushButton_49.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_49.setObjectName("pushButton_49")
        self.horizontalLayout_13.addWidget(self.pushButton_49)
        self.pushButton_62 = QPushButton(self.frame_15)
        self.pushButton_62.setMinimumSize(QSize(50, 50))
        self.pushButton_62.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_62.setObjectName("pushButton_62")
        self.horizontalLayout_13.addWidget(self.pushButton_62)
        self.pushButton_59 = QPushButton(self.frame_15)
        self.pushButton_59.setMinimumSize(QSize(50, 50))
        self.pushButton_59.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_59.setObjectName("pushButton_59")
        self.horizontalLayout_13.addWidget(self.pushButton_59)
        self.pushButton_60 = QPushButton(self.frame_15)
        self.pushButton_60.setMinimumSize(QSize(50, 50))
        self.pushButton_60.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_60.setObjectName("pushButton_60")
        self.horizontalLayout_13.addWidget(self.pushButton_60)
        self.pushButton_51 = QPushButton(self.frame_15)
        self.pushButton_51.setMinimumSize(QSize(50, 50))
        self.pushButton_51.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_51.setObjectName("pushButton_51")
        self.horizontalLayout_13.addWidget(self.pushButton_51)
        self.pushButton_52 = QPushButton(self.frame_15)
        self.pushButton_52.setMinimumSize(QSize(50, 50))
        self.pushButton_52.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_52.setObjectName("pushButton_52")
        self.horizontalLayout_13.addWidget(self.pushButton_52)
        self.pushButton_53 = QPushButton(self.frame_15)
        self.pushButton_53.setMinimumSize(QSize(50, 50))
        self.pushButton_53.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_53.setObjectName("pushButton_53")
        self.horizontalLayout_13.addWidget(self.pushButton_53)
        self.pushButton_61 = QPushButton(self.frame_15)
        self.pushButton_61.setMinimumSize(QSize(50, 50))
        self.pushButton_61.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_61.setObjectName("pushButton_61")
        self.horizontalLayout_13.addWidget(self.pushButton_61)
        self.pushButton_54 = QPushButton(self.frame_15)
        self.pushButton_54.setMinimumSize(QSize(50, 50))
        self.pushButton_54.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_54.setObjectName("pushButton_54")
        self.horizontalLayout_13.addWidget(self.pushButton_54)
        self.pushButton_55 = QPushButton(self.frame_15)
        self.pushButton_55.setMinimumSize(QSize(50, 50))
        self.pushButton_55.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_55.setObjectName("pushButton_55")
        self.horizontalLayout_13.addWidget(self.pushButton_55)
        self.pushButton_57 = QPushButton(self.frame_15)
        self.pushButton_57.setMinimumSize(QSize(50, 50))
        self.pushButton_57.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_57.setObjectName("pushButton_57")
        self.horizontalLayout_13.addWidget(self.pushButton_57)
        self.pushButton_48 = QPushButton(self.frame_15)
        self.pushButton_48.setMinimumSize(QSize(50, 50))
        self.pushButton_48.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_48.setObjectName("pushButton_48")
        self.horizontalLayout_13.addWidget(self.pushButton_48)
        self.verticalLayout_15.addWidget(self.frame_15)
        self.frame_16 = QFrame(self.frame_18)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_65 = QPushButton(self.frame_16)
        self.pushButton_65.setMinimumSize(QSize(50, 50))
        self.pushButton_65.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_65.setObjectName("pushButton_65")
        self.horizontalLayout_14.addWidget(self.pushButton_65)
        self.pushButton_73 = QPushButton(self.frame_16)
        self.pushButton_73.setMinimumSize(QSize(50, 50))
        self.pushButton_73.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_73.setObjectName("pushButton_73")
        self.horizontalLayout_14.addWidget(self.pushButton_73)
        self.pushButton_71 = QPushButton(self.frame_16)
        self.pushButton_71.setMinimumSize(QSize(50, 50))
        self.pushButton_71.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_71.setObjectName("pushButton_71")
        self.horizontalLayout_14.addWidget(self.pushButton_71)
        self.pushButton_64 = QPushButton(self.frame_16)
        self.pushButton_64.setMinimumSize(QSize(50, 50))
        self.pushButton_64.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_64.setObjectName("pushButton_64")
        self.horizontalLayout_14.addWidget(self.pushButton_64)
        self.pushButton_77 = QPushButton(self.frame_16)
        self.pushButton_77.setMinimumSize(QSize(50, 50))
        self.pushButton_77.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_77.setObjectName("pushButton_77")
        self.horizontalLayout_14.addWidget(self.pushButton_77)
        self.pushButton_74 = QPushButton(self.frame_16)
        self.pushButton_74.setMinimumSize(QSize(50, 50))
        self.pushButton_74.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_74.setObjectName("pushButton_74")
        self.horizontalLayout_14.addWidget(self.pushButton_74)
        self.pushButton_75 = QPushButton(self.frame_16)
        self.pushButton_75.setMinimumSize(QSize(50, 50))
        self.pushButton_75.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_75.setObjectName("pushButton_75")
        self.horizontalLayout_14.addWidget(self.pushButton_75)
        self.pushButton_66 = QPushButton(self.frame_16)
        self.pushButton_66.setMinimumSize(QSize(50, 50))
        self.pushButton_66.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_66.setObjectName("pushButton_66")
        self.horizontalLayout_14.addWidget(self.pushButton_66)
        self.pushButton_67 = QPushButton(self.frame_16)
        self.pushButton_67.setMinimumSize(QSize(50, 50))
        self.pushButton_67.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_67.setObjectName("pushButton_67")
        self.horizontalLayout_14.addWidget(self.pushButton_67)
        self.pushButton_68 = QPushButton(self.frame_16)
        self.pushButton_68.setMinimumSize(QSize(50, 50))
        self.pushButton_68.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_68.setObjectName("pushButton_68")
        self.horizontalLayout_14.addWidget(self.pushButton_68)
        self.pushButton_76 = QPushButton(self.frame_16)
        self.pushButton_76.setMinimumSize(QSize(50, 50))
        self.pushButton_76.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_76.setObjectName("pushButton_76")
        self.horizontalLayout_14.addWidget(self.pushButton_76)
        self.pushButton_69 = QPushButton(self.frame_16)
        self.pushButton_69.setMinimumSize(QSize(50, 50))
        self.pushButton_69.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_69.setObjectName("pushButton_69")
        self.horizontalLayout_14.addWidget(self.pushButton_69)
        self.pushButton_70 = QPushButton(self.frame_16)
        self.pushButton_70.setMinimumSize(QSize(50, 50))
        self.pushButton_70.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_70.setFont(font)
        self.pushButton_70.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_70.setObjectName("pushButton_70")
        self.horizontalLayout_14.addWidget(self.pushButton_70)
        self.pushButton_72 = QPushButton(self.frame_16)
        self.pushButton_72.setMinimumSize(QSize(50, 50))
        self.pushButton_72.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_72.setObjectName("pushButton_72")
        self.horizontalLayout_14.addWidget(self.pushButton_72)
        self.pushButton_63 = QPushButton(self.frame_16)
        self.pushButton_63.setMinimumSize(QSize(50, 50))
        self.pushButton_63.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_63.setObjectName("pushButton_63")
        self.horizontalLayout_14.addWidget(self.pushButton_63)
        self.verticalLayout_15.addWidget(self.frame_16)
        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_80 = QPushButton(self.frame_17)
        self.pushButton_80.setMinimumSize(QSize(50, 50))
        self.pushButton_80.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_80.setObjectName("pushButton_80")
        self.horizontalLayout_15.addWidget(self.pushButton_80)
        self.pushButton_88 = QPushButton(self.frame_17)
        self.pushButton_88.setMinimumSize(QSize(50, 50))
        self.pushButton_88.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_88.setObjectName("pushButton_88")
        self.horizontalLayout_15.addWidget(self.pushButton_88)
        self.pushButton_86 = QPushButton(self.frame_17)
        self.pushButton_86.setMinimumSize(QSize(50, 50))
        self.pushButton_86.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_86.setObjectName("pushButton_86")
        self.horizontalLayout_15.addWidget(self.pushButton_86)
        self.pushButton_79 = QPushButton(self.frame_17)
        self.pushButton_79.setMinimumSize(QSize(50, 50))
        self.pushButton_79.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_79.setObjectName("pushButton_79")
        self.horizontalLayout_15.addWidget(self.pushButton_79)
        self.pushButton_92 = QPushButton(self.frame_17)
        self.pushButton_92.setMinimumSize(QSize(50, 50))
        self.pushButton_92.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_92.setFont(font)
        self.pushButton_92.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_92.setObjectName("pushButton_92")
        self.horizontalLayout_15.addWidget(self.pushButton_92)
        self.pushButton_89 = QPushButton(self.frame_17)
        self.pushButton_89.setMinimumSize(QSize(50, 50))
        self.pushButton_89.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_89.setFont(font)
        self.pushButton_89.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_89.setObjectName("pushButton_89")
        self.horizontalLayout_15.addWidget(self.pushButton_89)
        self.pushButton_90 = QPushButton(self.frame_17)
        self.pushButton_90.setMinimumSize(QSize(50, 50))
        self.pushButton_90.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_90.setFont(font)
        self.pushButton_90.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_90.setObjectName("pushButton_90")
        self.horizontalLayout_15.addWidget(self.pushButton_90)
        self.pushButton_81 = QPushButton(self.frame_17)
        self.pushButton_81.setMinimumSize(QSize(50, 50))
        self.pushButton_81.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_81.setObjectName("pushButton_81")
        self.horizontalLayout_15.addWidget(self.pushButton_81)
        self.pushButton_82 = QPushButton(self.frame_17)
        self.pushButton_82.setMinimumSize(QSize(50, 50))
        self.pushButton_82.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_82.setObjectName("pushButton_82")
        self.horizontalLayout_15.addWidget(self.pushButton_82)
        self.pushButton_83 = QPushButton(self.frame_17)
        self.pushButton_83.setMinimumSize(QSize(50, 50))
        self.pushButton_83.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_83.setObjectName("pushButton_83")
        self.horizontalLayout_15.addWidget(self.pushButton_83)
        self.pushButton_91 = QPushButton(self.frame_17)
        self.pushButton_91.setMinimumSize(QSize(50, 50))
        self.pushButton_91.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_91.setObjectName("pushButton_91")
        self.horizontalLayout_15.addWidget(self.pushButton_91)
        self.pushButton_84 = QPushButton(self.frame_17)
        self.pushButton_84.setMinimumSize(QSize(50, 50))
        self.pushButton_84.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_84.setFont(font)
        self.pushButton_84.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_84.setObjectName("pushButton_84")
        self.horizontalLayout_15.addWidget(self.pushButton_84)
        self.pushButton_85 = QPushButton(self.frame_17)
        self.pushButton_85.setMinimumSize(QSize(50, 50))
        self.pushButton_85.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_85.setObjectName("pushButton_85")
        self.horizontalLayout_15.addWidget(self.pushButton_85)
        self.pushButton_87 = QPushButton(self.frame_17)
        self.pushButton_87.setMinimumSize(QSize(50, 50))
        self.pushButton_87.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_87.setObjectName("pushButton_87")
        self.horizontalLayout_15.addWidget(self.pushButton_87)
        self.pushButton_78 = QPushButton(self.frame_17)
        self.pushButton_78.setMinimumSize(QSize(50, 50))
        self.pushButton_78.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 25px;\n"
"border-color: rgb(52, 59, 72);")
        self.pushButton_78.setObjectName("pushButton_78")
        self.horizontalLayout_15.addWidget(self.pushButton_78)
        self.verticalLayout_15.addWidget(self.frame_17)
        self.horizontalLayout_9.addWidget(self.frame_18)
        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_19 = QVBoxLayout(self.frame_20)
        self.verticalLayout_19.setContentsMargins(-1, 15, -1, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_19 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_19.addWidget(self.label_19)
        self.label_21 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_19.addWidget(self.label_21)
        self.label_22 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_19.addWidget(self.label_22)
        self.label_18 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_19.addWidget(self.label_18)
        self.label_20 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_19.addWidget(self.label_20)
        self.label_12 = QLabel(self.frame_20)
        font = QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_19.addWidget(self.label_12)
        self.horizontalLayout_9.addWidget(self.frame_20)
        self.verticalLayout_14.addWidget(self.frame_11)
        self.verticalLayout_17.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.page_bill)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_21 = QFrame(self.page_2)
        self.frame_21.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_20 = QVBoxLayout(self.frame_22)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.tableWidget = QTableWidget(self.frame_22)
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableCornerButton::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(169)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_20.addWidget(self.tableWidget)
        self.horizontalLayout_18.addWidget(self.frame_22)
        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1)
        self.frame_23 = QFrame(self.page_2)
        self.frame_23.setMaximumSize(QSize(370, 16777215))
        self.frame_23.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setMaximumSize(QSize(16777215, 150))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_21 = QVBoxLayout(self.frame_24)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_23 = QLabel(self.frame_24)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_21.addWidget(self.label_23)
        self.lineEdit = QLineEdit(self.frame_24)
        self.lineEdit.setMaximumSize(QSize(335, 16777215))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_21.addWidget(self.lineEdit)
        self.pushButton_95 = QPushButton(self.frame_24)
        self.pushButton_95.setMaximumSize(QSize(335, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.pushButton_95.setFont(font)
        self.pushButton_95.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_95.setObjectName("pushButton_95")
        self.verticalLayout_21.addWidget(self.pushButton_95)
        self.pushButton_94 = QPushButton(self.frame_24)
        self.pushButton_94.setMaximumSize(QSize(335, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.pushButton_94.setFont(font)
        self.pushButton_94.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_94.setObjectName("pushButton_94")
        self.verticalLayout_21.addWidget(self.pushButton_94)
        self.pushButton_93 = QPushButton(self.frame_24)
        self.pushButton_93.setMaximumSize(QSize(335, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.pushButton_93.setFont(font)
        self.pushButton_93.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_93.setObjectName("pushButton_93")
        self.verticalLayout_21.addWidget(self.pushButton_93)
        self.verticalLayout_11.addWidget(self.frame_24)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_22 = QVBoxLayout(self.frame_25)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_11.addWidget(self.frame_25)
        self.gridLayout.addWidget(self.frame_23, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_22 = QHBoxLayout(self.page_3)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_40 = QFrame(self.page_3)
        self.frame_40.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_28 = QVBoxLayout(self.frame_40)
        self.verticalLayout_28.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.tableWidget_2 = QTableWidget(self.frame_40)
        self.tableWidget_2.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableCornerButton::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(169)
        self.verticalLayout_28.addWidget(self.tableWidget_2)
        self.horizontalLayout_22.addWidget(self.frame_40)
        self.frame_39 = QFrame(self.page_3)
        self.frame_39.setMinimumSize(QSize(0, 0))
        self.frame_39.setMaximumSize(QSize(450, 16777215))
        self.frame_39.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.verticalLayout_34 = QVBoxLayout(self.frame_39)
        self.verticalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.comboBox_3 = QComboBox(self.frame_39)
        self.comboBox_3.setStyleSheet("QComboBox {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::section{    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::title{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QComboBox::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QComboBox::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_34.addWidget(self.comboBox_3)
        self.lineEdit_6 = QLineEdit(self.frame_39)
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_34.addWidget(self.lineEdit_6)
        self.pushButton_97 = QPushButton(self.frame_39)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_97.setFont(font)
        self.pushButton_97.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_97.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_97.setObjectName("pushButton_97")
        self.verticalLayout_34.addWidget(self.pushButton_97)
        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.verticalLayout_34.addWidget(self.frame_41)
        self.horizontalLayout_22.addWidget(self.frame_39)
        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_26 = QFrame(self.page)
        self.frame_26.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_23 = QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_16 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_24 = QVBoxLayout(self.frame_29)
        self.verticalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_24 = QLabel(self.frame_29)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_24.addWidget(self.label_24)
        self.label_25 = QLabel(self.frame_29)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_24.addWidget(self.label_25)
        self.label_26 = QLabel(self.frame_29)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_24.addWidget(self.label_26)
        self.label_27 = QLabel(self.frame_29)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_24.addWidget(self.label_27)
        self.horizontalLayout_16.addWidget(self.frame_29)
        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_17 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_25 = QVBoxLayout(self.frame_31)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.lineEdit_2 = QLineEdit(self.frame_31)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_25.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QLineEdit(self.frame_31)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_25.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QLineEdit(self.frame_31)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_25.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QLineEdit(self.frame_31)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_25.addWidget(self.lineEdit_5)
        self.horizontalLayout_17.addWidget(self.frame_31)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setMinimumSize(QSize(250, 0))
        self.frame_32.setMaximumSize(QSize(100, 16777215))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_19 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_96 = QPushButton(self.frame_32)
        self.pushButton_96.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.pushButton_96.setFont(font)
        self.pushButton_96.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_96.setObjectName("pushButton_96")
        self.horizontalLayout_19.addWidget(self.pushButton_96)
        self.horizontalLayout_17.addWidget(self.frame_32)
        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setMinimumSize(QSize(320, 0))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_27 = QVBoxLayout(self.frame_33)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_17.addWidget(self.frame_33)
        self.horizontalLayout_16.addWidget(self.frame_30)
        self.verticalLayout_23.addWidget(self.frame_27)
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_26 = QVBoxLayout(self.frame_28)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_28 = QLabel(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_26.addWidget(self.label_28)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_26.addWidget(self.plainTextEdit_2)
        self.label_29 = QLabel(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_26.addWidget(self.label_29)
        self.plainTextEdit_3 = QPlainTextEdit(self.frame_28)
        font = QFont()
        font.setPointSize(10)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_26.addWidget(self.plainTextEdit_3)
        self.verticalLayout_23.addWidget(self.frame_28)
        self.gridLayout_2.addWidget(self.frame_26, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.verticalLayout_36.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setGeometry(QRect(0, 0, 1089, 26))
        self.menuBar.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"color: #ffffff;")
        self.menuBar.setDefaultUp(True)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        MainWindow.setTabOrder(self.btn_maximize_restore, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.btn_toggle_menu)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Киномания"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label_top_info_1.setText(_translate("MainWindow", "Фильмы"))
        self.label.setText(_translate("MainWindow", "Выберите фильм:"))
        self.label_2.setText(_translate("MainWindow", "Название: "))
        self.label_3.setText(_translate("MainWindow", "Страна:"))
        self.label_4.setText(_translate("MainWindow", "Жанр:"))
        self.label_5.setText(_translate("MainWindow", "Длительность:"))
        self.label_30.setText(_translate("MainWindow", "Дата выхода:"))
        self.label_6.setText(_translate("MainWindow", "Бюджет:"))
        self.label_7.setText(_translate("MainWindow", "Рейтинг:"))
        self.label_8.setText(_translate("MainWindow", "Состояние:"))
        self.pushButton_98.setText(_translate("MainWindow", "Распечатать"))
        self.label_9.setText(_translate("MainWindow", "Описание:"))
        self.pushButton.setText(_translate("MainWindow", "Убрать из проката"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить в прокат"))
        self.label_10.setText(_translate("MainWindow", "Выберите фильм:"))
        self.label_31.setText(_translate("MainWindow", "Выберите дату трансляции:"))
        self.label_13.setText(_translate("MainWindow", "1"))
        self.label_15.setText(_translate("MainWindow", "2"))
        self.label_17.setText(_translate("MainWindow", "3"))
        self.label_16.setText(_translate("MainWindow", "4"))
        self.label_14.setText(_translate("MainWindow", "5"))
        self.label_11.setText(_translate("MainWindow", "6"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "7"))
        self.pushButton_10.setText(_translate("MainWindow", "8"))
        self.pushButton_11.setText(_translate("MainWindow", "9"))
        self.pushButton_12.setText(_translate("MainWindow", "10"))
        self.pushButton_17.setText(_translate("MainWindow", "11"))
        self.pushButton_16.setText(_translate("MainWindow", "12"))
        self.pushButton_15.setText(_translate("MainWindow", "13"))
        self.pushButton_14.setText(_translate("MainWindow", "14"))
        self.pushButton_13.setText(_translate("MainWindow", "15"))
        self.pushButton_20.setText(_translate("MainWindow", "1"))
        self.pushButton_28.setText(_translate("MainWindow", "2"))
        self.pushButton_26.setText(_translate("MainWindow", "3"))
        self.pushButton_19.setText(_translate("MainWindow", "4"))
        self.pushButton_32.setText(_translate("MainWindow", "5"))
        self.pushButton_29.setText(_translate("MainWindow", "6"))
        self.pushButton_30.setText(_translate("MainWindow", "7"))
        self.pushButton_21.setText(_translate("MainWindow", "8"))
        self.pushButton_22.setText(_translate("MainWindow", "9"))
        self.pushButton_23.setText(_translate("MainWindow", "10"))
        self.pushButton_31.setText(_translate("MainWindow", "11"))
        self.pushButton_24.setText(_translate("MainWindow", "12"))
        self.pushButton_25.setText(_translate("MainWindow", "13"))
        self.pushButton_27.setText(_translate("MainWindow", "14"))
        self.pushButton_18.setText(_translate("MainWindow", "15"))
        self.pushButton_35.setText(_translate("MainWindow", "1"))
        self.pushButton_43.setText(_translate("MainWindow", "2"))
        self.pushButton_41.setText(_translate("MainWindow", "3"))
        self.pushButton_34.setText(_translate("MainWindow", "4"))
        self.pushButton_47.setText(_translate("MainWindow", "5"))
        self.pushButton_44.setText(_translate("MainWindow", "6"))
        self.pushButton_45.setText(_translate("MainWindow", "7"))
        self.pushButton_36.setText(_translate("MainWindow", "8"))
        self.pushButton_37.setText(_translate("MainWindow", "9"))
        self.pushButton_38.setText(_translate("MainWindow", "10"))
        self.pushButton_46.setText(_translate("MainWindow", "11"))
        self.pushButton_39.setText(_translate("MainWindow", "12"))
        self.pushButton_40.setText(_translate("MainWindow", "13"))
        self.pushButton_42.setText(_translate("MainWindow", "14"))
        self.pushButton_33.setText(_translate("MainWindow", "15"))
        self.pushButton_50.setText(_translate("MainWindow", "1"))
        self.pushButton_58.setText(_translate("MainWindow", "2"))
        self.pushButton_56.setText(_translate("MainWindow", "3"))
        self.pushButton_49.setText(_translate("MainWindow", "4"))
        self.pushButton_62.setText(_translate("MainWindow", "5"))
        self.pushButton_59.setText(_translate("MainWindow", "6"))
        self.pushButton_60.setText(_translate("MainWindow", "7"))
        self.pushButton_51.setText(_translate("MainWindow", "8"))
        self.pushButton_52.setText(_translate("MainWindow", "9"))
        self.pushButton_53.setText(_translate("MainWindow", "10"))
        self.pushButton_61.setText(_translate("MainWindow", "11"))
        self.pushButton_54.setText(_translate("MainWindow", "12"))
        self.pushButton_55.setText(_translate("MainWindow", "13"))
        self.pushButton_57.setText(_translate("MainWindow", "14"))
        self.pushButton_48.setText(_translate("MainWindow", "15"))
        self.pushButton_65.setText(_translate("MainWindow", "1"))
        self.pushButton_73.setText(_translate("MainWindow", "2"))
        self.pushButton_71.setText(_translate("MainWindow", "3"))
        self.pushButton_64.setText(_translate("MainWindow", "4"))
        self.pushButton_77.setText(_translate("MainWindow", "5"))
        self.pushButton_74.setText(_translate("MainWindow", "6"))
        self.pushButton_75.setText(_translate("MainWindow", "7"))
        self.pushButton_66.setText(_translate("MainWindow", "8"))
        self.pushButton_67.setText(_translate("MainWindow", "9"))
        self.pushButton_68.setText(_translate("MainWindow", "10"))
        self.pushButton_76.setText(_translate("MainWindow", "11"))
        self.pushButton_69.setText(_translate("MainWindow", "12"))
        self.pushButton_70.setText(_translate("MainWindow", "13"))
        self.pushButton_72.setText(_translate("MainWindow", "14"))
        self.pushButton_63.setText(_translate("MainWindow", "15"))
        self.pushButton_80.setText(_translate("MainWindow", "1"))
        self.pushButton_88.setText(_translate("MainWindow", "2"))
        self.pushButton_86.setText(_translate("MainWindow", "3"))
        self.pushButton_79.setText(_translate("MainWindow", "4"))
        self.pushButton_92.setText(_translate("MainWindow", "5"))
        self.pushButton_89.setText(_translate("MainWindow", "6"))
        self.pushButton_90.setText(_translate("MainWindow", "7"))
        self.pushButton_81.setText(_translate("MainWindow", "8"))
        self.pushButton_82.setText(_translate("MainWindow", "9"))
        self.pushButton_83.setText(_translate("MainWindow", "10"))
        self.pushButton_91.setText(_translate("MainWindow", "11"))
        self.pushButton_84.setText(_translate("MainWindow", "12"))
        self.pushButton_85.setText(_translate("MainWindow", "13"))
        self.pushButton_87.setText(_translate("MainWindow", "14"))
        self.pushButton_78.setText(_translate("MainWindow", "15"))
        self.label_19.setText(_translate("MainWindow", "1"))
        self.label_21.setText(_translate("MainWindow", "2"))
        self.label_22.setText(_translate("MainWindow", "3"))
        self.label_18.setText(_translate("MainWindow", "4"))
        self.label_20.setText(_translate("MainWindow", "5"))
        self.label_12.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата трансляции"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Посещаемость"))
        self.label_23.setText(_translate("MainWindow", "Введите номер записи для удаления:"))
        self.pushButton_95.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_94.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButton_93.setText(_translate("MainWindow", "Сохранить изменения"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Фильмы, которые транслировались в указанную дату."))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Посещаемость больше указанного числа."))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Посещаемость меньше указанного числа."))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Посещаемость равна указанному числу."))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Фильмы из указанной странны."))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Запрос по указанному жанру фильма."))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Фильмы с рейтингом больше указанного числа."))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Фильмы с рейтингом меньше указанного числа. "))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Фильмы с рейтингом указанного числа."))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Все фильмы, которые в прокате."))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Все фильмы, которые выбыли из проката."))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Все фильмы, которые ожидают проката."))
        # self.comboBox_3.setItemText(12, _translate("MainWindow", "Все фильмы, которые ожидают проката."))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Бюджет фильмов, который равен указанному числу."))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Бюджет фильмов, который больше указанного числа."))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Бюджет фильмов, который меньше указанного числа."))
        # self.comboBox_3.setItemText(15, _translate("MainWindow", "Все фильмы в алфавитном порядке."))
        # self.comboBox_3.setItemText(16, _translate("MainWindow", "Рейтинг фильмов по возрастанию."))
        # self.comboBox_3.setItemText(17, _translate("MainWindow", "Рейтинг фильмов по убыванию."))
        self.pushButton_97.setText(_translate("MainWindow", "Вывести"))
        self.label_24.setText(_translate("MainWindow", "В базе данных фильмов:"))
        self.label_25.setText(_translate("MainWindow", "В ожидание релиза:"))
        self.label_26.setText(_translate("MainWindow", "Выбыли из проката:"))
        self.label_27.setText(_translate("MainWindow", "В прокате:"))
        self.pushButton_96.setText(_translate("MainWindow", "Обновить информацию"))
        self.label_28.setText(_translate("MainWindow", "О программе:"))
        self.label_29.setText(_translate("MainWindow", "Об авторе:"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "О программе"))
        self.action_3.setText(_translate("MainWindow", "Об авторе"))

