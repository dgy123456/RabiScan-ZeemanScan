from artiq.experiment import *
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class GUI2(EnvExperiment, object):
    """GUI 2.0"""
    def build(self):
        pass
        
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow) 
        MainWindow.show()
        sys.exit(app.exec_()) 
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 906)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 90, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(-10, 20, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 490, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(50, 480, 631, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(50, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.radioButton_rabi = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_rabi.setGeometry(QtCore.QRect(420, 690, 115, 19))
        self.radioButton_rabi.setObjectName("radioButton_rabi")
        self.radioButton_zeeman = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_zeeman.setGeometry(QtCore.QRect(420, 730, 115, 19))
        self.radioButton_zeeman.setObjectName("radioButton_zeeman")
        self.radioButton_cust = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_cust.setGeometry(QtCore.QRect(420, 770, 115, 19))
        self.radioButton_cust.setObjectName("radioButton_cust")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 700, 111, 111))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_off = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_off.setGeometry(QtCore.QRect(420, 810, 115, 19))
        self.radioButton_off.setObjectName("radioButton_off")
        self.Setting = QtWidgets.QTabWidget(self.centralwidget)
        self.Setting.setGeometry(QtCore.QRect(40, 150, 631, 301))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Setting.setFont(font)
        self.Setting.setObjectName("Setting")
        self.DPL_Cooling = QtWidgets.QWidget()
        self.DPL_Cooling.setObjectName("DPL_Cooling")
        self.doubleSpinBox_DPL = QtWidgets.QDoubleSpinBox(self.DPL_Cooling)
        self.doubleSpinBox_DPL.setGeometry(QtCore.QRect(140, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_DPL.setFont(font)
        self.doubleSpinBox_DPL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_DPL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_DPL.setMaximum(999999.99)
        self.doubleSpinBox_DPL.setObjectName("doubleSpinBox_DPL")
        self.label_36 = QtWidgets.QLabel(self.DPL_Cooling)
        self.label_36.setGeometry(QtCore.QRect(260, 40, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.DPL_Cooling)
        self.label_37.setGeometry(QtCore.QRect(20, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.line_2 = QtWidgets.QFrame(self.DPL_Cooling)
        self.line_2.setGeometry(QtCore.QRect(270, 40, 41, 191))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Laser_397_1 = QtWidgets.QCheckBox(self.DPL_Cooling)
        self.Laser_397_1.setGeometry(QtCore.QRect(310, 110, 91, 19))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Laser_397_1.setFont(font)
        self.Laser_397_1.setObjectName("Laser_397_1")
        self.Laser_397_2 = QtWidgets.QCheckBox(self.DPL_Cooling)
        self.Laser_397_2.setGeometry(QtCore.QRect(310, 150, 91, 19))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Laser_397_2.setFont(font)
        self.Laser_397_2.setObjectName("Laser_397_2")
        self.Laser_397_3 = QtWidgets.QCheckBox(self.DPL_Cooling)
        self.Laser_397_3.setGeometry(QtCore.QRect(310, 190, 91, 19))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Laser_397_3.setFont(font)
        self.Laser_397_3.setObjectName("Laser_397_3")
        self.line_3 = QtWidgets.QFrame(self.DPL_Cooling)
        self.line_3.setGeometry(QtCore.QRect(380, 40, 41, 191))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.DPL_Cooling)
        self.line_5.setGeometry(QtCore.QRect(490, 40, 41, 191))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Laser_397_all = QtWidgets.QCheckBox(self.DPL_Cooling)
        self.Laser_397_all.setGeometry(QtCore.QRect(310, 50, 91, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Laser_397_all.setFont(font)
        self.Laser_397_all.setObjectName("Laser_397_all")
        self.checkBox_12 = QtWidgets.QCheckBox(self.DPL_Cooling)
        self.checkBox_12.setGeometry(QtCore.QRect(430, 50, 91, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.DPL_Cooling)
        self.checkBox_13.setGeometry(QtCore.QRect(540, 50, 91, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.Setting.addTab(self.DPL_Cooling, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.line_8 = QtWidgets.QFrame(self.tab_6)
        self.line_8.setGeometry(QtCore.QRect(480, 50, 41, 181))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_25 = QtWidgets.QLabel(self.tab_6)
        self.label_25.setGeometry(QtCore.QRect(390, 30, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_41 = QtWidgets.QLabel(self.tab_6)
        self.label_41.setGeometry(QtCore.QRect(20, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.line_7 = QtWidgets.QFrame(self.tab_6)
        self.line_7.setGeometry(QtCore.QRect(300, 50, 41, 181))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_26 = QtWidgets.QLabel(self.tab_6)
        self.label_26.setGeometry(QtCore.QRect(530, 30, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_40 = QtWidgets.QLabel(self.tab_6)
        self.label_40.setGeometry(QtCore.QRect(270, 40, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.doubleSpinBox_DPL_2 = QtWidgets.QDoubleSpinBox(self.tab_6)
        self.doubleSpinBox_DPL_2.setGeometry(QtCore.QRect(150, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_DPL_2.setFont(font)
        self.doubleSpinBox_DPL_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_DPL_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_DPL_2.setMaximum(999999.99)
        self.doubleSpinBox_DPL_2.setObjectName("doubleSpinBox_DPL_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_6.setGeometry(QtCore.QRect(340, 99, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_7.setGeometry(QtCore.QRect(420, 100, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_8.setGeometry(QtCore.QRect(340, 150, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_9.setGeometry(QtCore.QRect(420, 150, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_10.setGeometry(QtCore.QRect(520, 100, 91, 19))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.Setting.addTab(self.tab_6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_38 = QtWidgets.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(30, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.doubleSpinBox_SB = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_SB.setGeometry(QtCore.QRect(30, 100, 101, 31))
        self.doubleSpinBox_SB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_SB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_SB.setMaximum(999999.99)
        self.doubleSpinBox_SB.setObjectName("doubleSpinBox_SB")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(150, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.Setting.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.Setting.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.doubleSpinBox_PMT = QtWidgets.QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_PMT.setGeometry(QtCore.QRect(30, 70, 101, 31))
        self.doubleSpinBox_PMT.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_PMT.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_PMT.setMaximum(999999.99)
        self.doubleSpinBox_PMT.setObjectName("doubleSpinBox_PMT")
        self.label_39 = QtWidgets.QLabel(self.tab_8)
        self.label_39.setGeometry(QtCore.QRect(150, 70, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_31 = QtWidgets.QLabel(self.tab_8)
        self.label_31.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.Setting.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.Setting.addTab(self.tab_9, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(50, 540, 341, 301))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(230, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(260, 40, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_rabistep = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_rabistep.setGeometry(QtCore.QRect(140, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_rabistep.setFont(font)
        self.doubleSpinBox_rabistep.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_rabistep.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_rabistep.setMaximum(999999.99)
        self.doubleSpinBox_rabistep.setObjectName("doubleSpinBox_rabistep")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.doubleSpinBox_rabistart = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_rabistart.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_rabistart.setFont(font)
        self.doubleSpinBox_rabistart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_rabistart.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_rabistart.setMaximum(999999.99)
        self.doubleSpinBox_rabistart.setObjectName("doubleSpinBox_rabistart")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(260, 160, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(260, 100, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox_rabiend = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_rabiend.setGeometry(QtCore.QRect(140, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_rabiend.setFont(font)
        self.doubleSpinBox_rabiend.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_rabiend.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_rabiend.setMaximum(999999.99)
        self.doubleSpinBox_rabiend.setObjectName("doubleSpinBox_rabiend")
        self.spinBox_rabirepeat = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_rabirepeat.setGeometry(QtCore.QRect(140, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_rabirepeat.setFont(font)
        self.spinBox_rabirepeat.setObjectName("spinBox_rabirepeat")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(270, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.spinBox_zeemanrepeat = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_zeemanrepeat.setGeometry(QtCore.QRect(180, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_zeemanrepeat.setFont(font)
        self.spinBox_zeemanrepeat.setObjectName("spinBox_zeemanrepeat")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(300, 160, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(20, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(20, 160, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.doubleSpinBox_zeemanend = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_zeemanend.setGeometry(QtCore.QRect(180, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_zeemanend.setFont(font)
        self.doubleSpinBox_zeemanend.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_zeemanend.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_zeemanend.setMaximum(999999.99)
        self.doubleSpinBox_zeemanend.setObjectName("doubleSpinBox_zeemanend")
        self.doubleSpinBox_zeemanstep = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_zeemanstep.setGeometry(QtCore.QRect(180, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_zeemanstep.setFont(font)
        self.doubleSpinBox_zeemanstep.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_zeemanstep.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_zeemanstep.setMaximum(999999.99)
        self.doubleSpinBox_zeemanstep.setObjectName("doubleSpinBox_zeemanstep")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.doubleSpinBox_zeemanstart = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_zeemanstart.setGeometry(QtCore.QRect(180, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_zeemanstart.setFont(font)
        self.doubleSpinBox_zeemanstart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_zeemanstart.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_zeemanstart.setMaximum(999999.99)
        self.doubleSpinBox_zeemanstart.setObjectName("doubleSpinBox_zeemanstart")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(300, 40, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(300, 100, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(20, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setGeometry(QtCore.QRect(260, 40, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setGeometry(QtCore.QRect(20, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.doubleSpinBox_custTime = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_custTime.setGeometry(QtCore.QRect(140, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_custTime.setFont(font)
        self.doubleSpinBox_custTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_custTime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_custTime.setMaximum(999999.99)
        self.doubleSpinBox_custTime.setObjectName("doubleSpinBox_custTime")
        self.doubleSpinBox_custF = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_custF.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_custF.setFont(font)
        self.doubleSpinBox_custF.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_custF.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_custF.setMaximum(999999.99)
        self.doubleSpinBox_custF.setObjectName("doubleSpinBox_custF")
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(260, 100, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.spinBox_custreapeat = QtWidgets.QSpinBox(self.tab_5)
        self.spinBox_custreapeat.setGeometry(QtCore.QRect(140, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_custreapeat.setFont(font)
        self.spinBox_custreapeat.setObjectName("spinBox_custreapeat")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(20, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_27 = QtWidgets.QLabel(self.tab_5)
        self.label_27.setGeometry(QtCore.QRect(230, 165, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.tabWidget_2.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuAdvance = QtWidgets.QMenu(self.menubar)
        self.menuAdvance.setObjectName("menuAdvance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionreset = QtWidgets.QAction(MainWindow)
        self.actionreset.setObjectName("actionreset")
        self.actionClear_Settings = QtWidgets.QAction(MainWindow)
        self.actionClear_Settings.setObjectName("actionClear_Settings")
        self.menuMain.addAction(self.actionreset)
        self.menuMain.addAction(self.actionClear_Settings)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuAdvance.menuAction())

        self.retranslateUi(MainWindow)
        self.Setting.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    #Added by MGQ---------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.Laser_397_all.stateChanged.connect(lambda: self.Laser_397_all_stateChanged(self.Laser_397_all))
        self.Laser_397_1.stateChanged.connect(lambda: self.Laser_397_1_stateChanged(self.Laser_397_1))
        self.Laser_397_2.stateChanged.connect(lambda: self.Laser_397_2_stateChanged(self.Laser_397_2))
        self.Laser_397_3.stateChanged.connect(lambda: self.Laser_397_3_stateChanged(self.Laser_397_3))
        
    def Laser_397_all_stateChanged(self,A):
        if self.Laser_397_all.isChecked() == True:
            self.set_dataset("Para_Laser_All",1, broadcast=True)
        else:
            self.set_dataset("Para_Laser_All",0, broadcast=True)
        
    def Laser_397_1_stateChanged(self,A):
        if self.Laser_397_1.isChecked() == True:
            self.set_dataset("Para_Laser_1",1, broadcast=True)
        else:
            self.set_dataset("Para_Laser_1",0, broadcast=True)
            
    def Laser_397_2_stateChanged(self,A):
        if self.Laser_397_2.isChecked() == True:
            self.set_dataset("Para_Laser_2",1, broadcast=True)
        else:
            self.set_dataset("Para_Laser_2",0, broadcast=True)
            
    def Laser_397_3_stateChanged(self,A):
        if self.Laser_397_3.isChecked() == True:
            self.set_dataset("Para_Laser_3",1, broadcast=True)
        else:
            self.set_dataset("Para_Laser_3",0, broadcast=True)
        
        
        
        
    #END------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#003500;\">Ion Trap QC Control System </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#002800;\">Mode</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#002800;\">Setting</span></p></body></html>"))
        self.radioButton_rabi.setText(_translate("MainWindow", "Rabi Scan"))
        self.radioButton_zeeman.setText(_translate("MainWindow", "Zeeman Scan"))
        self.radioButton_cust.setText(_translate("MainWindow", "Customized"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.radioButton_off.setText(_translate("MainWindow", "OFF"))
        self.label_36.setText(_translate("MainWindow", "us"))
        self.label_37.setText(_translate("MainWindow", "Doppler Cooling"))
        self.Laser_397_1.setText(_translate("MainWindow", "397_1"))
        self.Laser_397_2.setText(_translate("MainWindow", "397_2"))
        self.Laser_397_3.setText(_translate("MainWindow", "397_3"))
        self.Laser_397_all.setText(_translate("MainWindow", "397_All"))
        self.checkBox_12.setText(_translate("MainWindow", "866"))
        self.checkBox_13.setText(_translate("MainWindow", "854"))
        self.Setting.setTabText(self.Setting.indexOf(self.DPL_Cooling), _translate("MainWindow", "DPL Cooling"))
        self.label_25.setText(_translate("MainWindow", "# 729"))
        self.label_41.setText(_translate("MainWindow", "Optical Pump"))
        self.label_26.setText(_translate("MainWindow", "# 854"))
        self.label_40.setText(_translate("MainWindow", "us"))
        self.checkBox_6.setText(_translate("MainWindow", "729_1"))
        self.checkBox_7.setText(_translate("MainWindow", "729_3"))
        self.checkBox_8.setText(_translate("MainWindow", "729_2"))
        self.checkBox_9.setText(_translate("MainWindow", "729_4"))
        self.checkBox_10.setText(_translate("MainWindow", "854_1"))
        self.Setting.setTabText(self.Setting.indexOf(self.tab_6), _translate("MainWindow", "Optical Pump"))
        self.label_38.setText(_translate("MainWindow", "Side Band Cooling"))
        self.label_30.setText(_translate("MainWindow", "us"))
        self.Setting.setTabText(self.Setting.indexOf(self.tab_2), _translate("MainWindow", "SB Cooling"))
        self.Setting.setTabText(self.Setting.indexOf(self.tab_7), _translate("MainWindow", "Opreating"))
        self.label_39.setText(_translate("MainWindow", "us"))
        self.label_31.setText(_translate("MainWindow", "Time for PMT "))
        self.Setting.setTabText(self.Setting.indexOf(self.tab_8), _translate("MainWindow", "Detecting"))
        self.Setting.setTabText(self.Setting.indexOf(self.tab_9), _translate("MainWindow", "Gap"))
        self.label_18.setText(_translate("MainWindow", "times"))
        self.label_5.setText(_translate("MainWindow", "us"))
        self.label_9.setText(_translate("MainWindow", "Repeat"))
        self.label_7.setText(_translate("MainWindow", "us"))
        self.label_4.setText(_translate("MainWindow", "Time for Step"))
        self.label_6.setText(_translate("MainWindow", "us"))
        self.label_2.setText(_translate("MainWindow", "Time to Start"))
        self.label_3.setText(_translate("MainWindow", "Time to End"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Rabi Scan"))
        self.label_19.setText(_translate("MainWindow", "times"))
        self.label_12.setText(_translate("MainWindow", "Hz"))
        self.label_13.setText(_translate("MainWindow", "Repeat"))
        self.label_15.setText(_translate("MainWindow", "Frequency for Step"))
        self.label_14.setText(_translate("MainWindow", "Frequency of End"))
        self.label_16.setText(_translate("MainWindow", "Hz"))
        self.label_17.setText(_translate("MainWindow", "Hz"))
        self.label_11.setText(_translate("MainWindow", "Frequency of Start"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Zeeman Scan"))
        self.label_28.setText(_translate("MainWindow", "Hz"))
        self.label_21.setText(_translate("MainWindow", "Rabi Time"))
        self.label_29.setText(_translate("MainWindow", "Repeat"))
        self.label_23.setText(_translate("MainWindow", "us"))
        self.label_22.setText(_translate("MainWindow", "Frequency "))
        self.label_27.setText(_translate("MainWindow", "times"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Costomized"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuAdvance.setTitle(_translate("MainWindow", "Advance"))
        self.actionreset.setText(_translate("MainWindow", "Clear Data"))
        self.actionClear_Settings.setText(_translate("MainWindow", "Clear Settings"))
        
        
        
    
