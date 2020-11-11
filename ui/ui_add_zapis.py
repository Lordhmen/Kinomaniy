# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt, QPoint)
from PySide2.QtGui import (QBrush, QColor, QFont,
                           QIcon, QPalette, QPixmap)
from PySide2.QtWidgets import *


class Ui_mMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1353, 382)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "    color: #ffffff;\n"
                                 "    background-color: rgba(27, 29, 35, 160);\n"
                                 "    border: 1px solid rgb(40, 40, 40);\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "/* LINE EDIT */\n"
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
                                 "    background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
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
                                 "    background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
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
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                 "border-radius: 5px;\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                   "border-radius: 5px;\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.frame_2)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tableWidget = QTableWidget(self.frame_2)
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
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(1)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 11, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QPushButton(self.frame_4)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
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
        self.verticalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QLabel(self.frame_6)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.tableWidget_2 = QTableWidget(self.frame_6)
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
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(1)
        item = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        # item = QTableWidgetItem()
        # self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setContentsMargins(0, 11, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_2 = QPushButton(self.frame_8)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
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
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Заполните таблицу данными"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название фильма"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Жанр"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Длительность"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Бюджет"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Рейтинг"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата выхода"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Состояние"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Продолжить"))
        self.label_2.setText(_translate("MainWindow", "Заполните таблицу данными"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата трансляции"))
        # item = self.tableWidget_2.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "Посещаемость"))
        self.pushButton_2.setText(_translate("MainWindow", "Продолжить"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
