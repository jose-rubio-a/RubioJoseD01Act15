# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1863, 1015)
        MainWindow.setMinimumSize(QSize(1863, 1015))
        MainWindow.setMaximumSize(QSize(1863, 1015))
        icon = QIcon()
        icon.addFile(u"../assets/icon/batch.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"    background-color: #F6F6F6;\n"
"}\n"
"QFrame\n"
"{\n"
"	border: 2px solid #6D9886;\n"
"}\n"
"QLabel\n"
"{\n"
"	color: #212121;\n"
"	border: 0px;\n"
"	font-family: constantia;\n"
"}\n"
"QLCDNumber\n"
"{\n"
"	border: 0px;\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(200, 10, 771, 41))
        font = QFont()
        font.setFamily(u"constantia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 220, 411, 341))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.captura_tableWidget = QTableWidget(self.frame)
        if (self.captura_tableWidget.columnCount() < 3):
            self.captura_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.captura_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.captura_tableWidget.setObjectName(u"captura_tableWidget")
        self.captura_tableWidget.setGeometry(QRect(10, 40, 391, 261))
        self.captura_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.iniciar_pushButton = QPushButton(self.frame)
        self.iniciar_pushButton.setObjectName(u"iniciar_pushButton")
        self.iniciar_pushButton.setEnabled(False)
        self.iniciar_pushButton.setGeometry(QRect(20, 310, 371, 28))
        self.iniciar_pushButton.setChecked(False)
        self.iniciar_pushButton.setFlat(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 20))
        font1 = QFont()
        font1.setFamily(u"constantia")
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(430, 60, 381, 611))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.ejecuccion_tableWidget = QTableWidget(self.frame_2)
        if (self.ejecuccion_tableWidget.columnCount() < 5):
            self.ejecuccion_tableWidget.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ejecuccion_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.ejecuccion_tableWidget.setObjectName(u"ejecuccion_tableWidget")
        self.ejecuccion_tableWidget.setGeometry(QRect(10, 50, 361, 201))
        self.ejecuccion_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.transcurrido_lcdNumber = QLCDNumber(self.frame_2)
        self.transcurrido_lcdNumber.setObjectName(u"transcurrido_lcdNumber")
        self.transcurrido_lcdNumber.setGeometry(QRect(210, 452, 71, 21))
        self.transcurrido_lcdNumber.setAutoFillBackground(False)
        self.transcurrido_lcdNumber.setStyleSheet(u"background-color: rgb(83, 79, 67);")
        self.transcurrido_lcdNumber.setFrameShape(QFrame.Box)
        self.transcurrido_lcdNumber.setProperty("intValue", 0)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 290, 131, 21))
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 350, 91, 31))
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 390, 141, 21))
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 320, 31, 21))
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 450, 191, 21))
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 480, 191, 21))
        self.restante_lcdNumber = QLCDNumber(self.frame_2)
        self.restante_lcdNumber.setObjectName(u"restante_lcdNumber")
        self.restante_lcdNumber.setGeometry(QRect(210, 480, 71, 21))
        self.restante_lcdNumber.setAutoFillBackground(False)
        self.restante_lcdNumber.setStyleSheet(u"background-color: rgb(83, 79, 67);")
        self.restante_lcdNumber.setFrameShape(QFrame.Box)
        self.restante_lcdNumber.setProperty("intValue", 0)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 530, 191, 31))
        self.total_lcdNumber = QLCDNumber(self.frame_2)
        self.total_lcdNumber.setObjectName(u"total_lcdNumber")
        self.total_lcdNumber.setGeometry(QRect(210, 530, 81, 31))
        self.total_lcdNumber.setAutoFillBackground(False)
        self.total_lcdNumber.setStyleSheet(u"background-color: rgb(83, 79, 67);")
        self.total_lcdNumber.setFrameShape(QFrame.Box)
        self.total_lcdNumber.setProperty("intValue", 0)
        self.Id_label = QLabel(self.frame_2)
        self.Id_label.setObjectName(u"Id_label")
        self.Id_label.setGeometry(QRect(120, 320, 221, 21))
        font2 = QFont()
        font2.setFamily(u"constantia")
        font2.setPointSize(10)
        self.Id_label.setFont(font2)
        self.operacion_label = QLabel(self.frame_2)
        self.operacion_label.setObjectName(u"operacion_label")
        self.operacion_label.setGeometry(QRect(140, 350, 221, 21))
        self.operacion_label.setFont(font2)
        self.tiempo_label = QLabel(self.frame_2)
        self.tiempo_label.setObjectName(u"tiempo_label")
        self.tiempo_label.setGeometry(QRect(170, 390, 191, 21))
        self.tiempo_label.setFont(font2)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 151, 20))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 260, 221, 20))
        self.label_3.setFont(font1)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(810, 60, 1041, 461))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.finalizados_tableWidget = QTableWidget(self.frame_3)
        if (self.finalizados_tableWidget.columnCount() < 9):
            self.finalizados_tableWidget.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.finalizados_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.finalizados_tableWidget.setObjectName(u"finalizados_tableWidget")
        self.finalizados_tableWidget.setGeometry(QRect(10, 50, 1001, 391))
        self.finalizados_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 20, 201, 21))
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 60, 411, 161))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 0, 191, 31))
        self.N_Procesos = QSpinBox(self.frame_4)
        self.N_Procesos.setObjectName(u"N_Procesos")
        self.N_Procesos.setGeometry(QRect(90, 30, 201, 22))
        self.N_Procesos.setWrapping(False)
        self.N_Procesos.setMaximum(1000000)
        self.Empezar_pushButton = QPushButton(self.frame_4)
        self.Empezar_pushButton.setObjectName(u"Empezar_pushButton")
        self.Empezar_pushButton.setGeometry(QRect(70, 120, 251, 28))
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 60, 191, 31))
        self.Quantum = QSpinBox(self.frame_4)
        self.Quantum.setObjectName(u"Quantum")
        self.Quantum.setGeometry(QRect(90, 90, 201, 22))
        self.Quantum.setWrapping(False)
        self.Quantum.setMaximum(16)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(430, 670, 381, 291))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 221, 20))
        self.label_5.setFont(font1)
        self.bloqueados_tableWidget = QTableWidget(self.frame_5)
        if (self.bloqueados_tableWidget.columnCount() < 3):
            self.bloqueados_tableWidget.setColumnCount(3)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.bloqueados_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.bloqueados_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.bloqueados_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        self.bloqueados_tableWidget.setObjectName(u"bloqueados_tableWidget")
        self.bloqueados_tableWidget.setGeometry(QRect(10, 40, 361, 241))
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1030, 520, 821, 441))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 20, 201, 21))
        self.BCP_tableWidget = QTableWidget(self.frame_6)
        if (self.BCP_tableWidget.columnCount() < 11):
            self.BCP_tableWidget.setColumnCount(11)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.BCP_tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem30)
        self.BCP_tableWidget.setObjectName(u"BCP_tableWidget")
        self.BCP_tableWidget.setGeometry(QRect(10, 50, 801, 381))
        self.BCP_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 560, 411, 401))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.memoria_tableWidget = QTableWidget(self.frame_7)
        if (self.memoria_tableWidget.columnCount() < 6):
            self.memoria_tableWidget.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.memoria_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.memoria_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.memoria_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.memoria_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.memoria_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.memoria_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        if (self.memoria_tableWidget.rowCount() < 25):
            self.memoria_tableWidget.setRowCount(25)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(21, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(22, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(23, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.memoria_tableWidget.setVerticalHeaderItem(24, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(0, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(0, 3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(1, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(1, 3, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(2, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(2, 3, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(3, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(3, 3, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(4, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(4, 3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(5, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(5, 3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(6, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(6, 3, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(7, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(7, 3, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(8, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(8, 3, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(9, 0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(9, 3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(10, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(10, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(10, 3, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(10, 4, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(11, 0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(11, 1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(11, 3, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(11, 4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(12, 0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(12, 1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(12, 3, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(12, 4, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(13, 0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(13, 1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(13, 3, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(13, 4, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(14, 0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(14, 1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(14, 3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(14, 4, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(15, 0, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(15, 1, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(15, 3, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(15, 4, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(16, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(16, 1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(16, 3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(16, 4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(17, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(17, 1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(17, 3, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(17, 4, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(18, 0, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(18, 1, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(18, 3, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(18, 4, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(19, 0, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(19, 1, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(19, 3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(19, 4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(20, 0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(20, 1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(20, 3, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(20, 4, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(21, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(21, 1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(21, 3, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(21, 4, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(22, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(22, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(22, 3, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(22, 4, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(23, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(23, 1, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(23, 3, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(23, 4, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(24, 0, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(24, 1, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(24, 3, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.memoria_tableWidget.setItem(24, 4, __qtablewidgetitem141)
        self.memoria_tableWidget.setObjectName(u"memoria_tableWidget")
        self.memoria_tableWidget.setGeometry(QRect(10, 10, 391, 381))
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(810, 520, 221, 441))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 221, 20))
        self.label_7.setFont(font1)
        self.suspendidos_tableWidget = QTableWidget(self.frame_8)
        if (self.suspendidos_tableWidget.columnCount() < 2):
            self.suspendidos_tableWidget.setColumnCount(2)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.suspendidos_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.suspendidos_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem143)
        self.suspendidos_tableWidget.setObjectName(u"suspendidos_tableWidget")
        self.suspendidos_tableWidget.setGeometry(QRect(10, 40, 201, 381))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1863, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simular el Procesamiento por Lotes", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Procesador por lotes</span></p></body></html>", None))
        ___qtablewidgetitem = self.captura_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.captura_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem2 = self.captura_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None));
        self.iniciar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Procesos Nuevos:", None))
        ___qtablewidgetitem3 = self.ejecuccion_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.ejecuccion_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem5 = self.ejecuccion_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None));
        ___qtablewidgetitem6 = self.ejecuccion_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Restante", None));
        ___qtablewidgetitem7 = self.ejecuccion_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tam", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Proceso Actual:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Operacion:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tiempo Estimado: </span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">ID:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tiempo transcurrido: </span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tiempo restante: </span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tiempo total: </span></p></body></html>", None))
        self.Id_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.operacion_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tiempo_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Procesos Listos:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Proceso en Ejecucion:", None))
        ___qtablewidgetitem8 = self.finalizados_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.finalizados_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem10 = self.finalizados_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem11 = self.finalizados_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Tiempo de llegada", None));
        ___qtablewidgetitem12 = self.finalizados_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Tiempo de finalizacion", None));
        ___qtablewidgetitem13 = self.finalizados_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tiempo de retorno", None));
        ___qtablewidgetitem14 = self.finalizados_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tiempo de respuesta", None));
        ___qtablewidgetitem15 = self.finalizados_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Tiempo de espera", None));
        ___qtablewidgetitem16 = self.finalizados_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Tiempo de servicio", None));
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Procesos Terminados:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Numero de procesos:</span></p></body></html>", None))
        self.Empezar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Empezar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Quantum:</span></p><p><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Procesos bloqueados:", None))
        ___qtablewidgetitem17 = self.bloqueados_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem18 = self.bloqueados_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem19 = self.bloqueados_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Tiempo restante bloqueado", None));
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tabla de procesos:</span></p></body></html>", None))
        ___qtablewidgetitem20 = self.BCP_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem21 = self.BCP_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem22 = self.BCP_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem23 = self.BCP_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Tiempo restante", None));
        ___qtablewidgetitem24 = self.BCP_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Tiempo bloqueado", None));
        ___qtablewidgetitem25 = self.BCP_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Tiempo de llegada", None));
        ___qtablewidgetitem26 = self.BCP_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Tiempo de finalizacion", None));
        ___qtablewidgetitem27 = self.BCP_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Tiempo de retorno", None));
        ___qtablewidgetitem28 = self.BCP_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Tiempo de respuesta", None));
        ___qtablewidgetitem29 = self.BCP_tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Tiempo de espera", None));
        ___qtablewidgetitem30 = self.BCP_tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Tiempo de servicio", None));
        ___qtablewidgetitem31 = self.memoria_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem32 = self.memoria_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem33 = self.memoria_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Ocupa", None));
        ___qtablewidgetitem34 = self.memoria_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem35 = self.memoria_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem36 = self.memoria_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Ocupa", None));
        ___qtablewidgetitem37 = self.memoria_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem38 = self.memoria_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem39 = self.memoria_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem40 = self.memoria_tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem41 = self.memoria_tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem42 = self.memoria_tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem43 = self.memoria_tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem44 = self.memoria_tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem45 = self.memoria_tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem46 = self.memoria_tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem47 = self.memoria_tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem48 = self.memoria_tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem49 = self.memoria_tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem50 = self.memoria_tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem51 = self.memoria_tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem52 = self.memoria_tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem53 = self.memoria_tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem54 = self.memoria_tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem55 = self.memoria_tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem56 = self.memoria_tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem57 = self.memoria_tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem58 = self.memoria_tableWidget.verticalHeaderItem(21)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem59 = self.memoria_tableWidget.verticalHeaderItem(22)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem60 = self.memoria_tableWidget.verticalHeaderItem(23)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem61 = self.memoria_tableWidget.verticalHeaderItem(24)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"25", None));

        __sortingEnabled = self.memoria_tableWidget.isSortingEnabled()
        self.memoria_tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem62 = self.memoria_tableWidget.item(0, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem63 = self.memoria_tableWidget.item(0, 3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem64 = self.memoria_tableWidget.item(1, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem65 = self.memoria_tableWidget.item(1, 3)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem66 = self.memoria_tableWidget.item(2, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem67 = self.memoria_tableWidget.item(2, 3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem68 = self.memoria_tableWidget.item(3, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem69 = self.memoria_tableWidget.item(3, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem70 = self.memoria_tableWidget.item(4, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem71 = self.memoria_tableWidget.item(4, 3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem72 = self.memoria_tableWidget.item(5, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem73 = self.memoria_tableWidget.item(5, 3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem74 = self.memoria_tableWidget.item(6, 0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem75 = self.memoria_tableWidget.item(6, 3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem76 = self.memoria_tableWidget.item(7, 0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem77 = self.memoria_tableWidget.item(7, 3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem78 = self.memoria_tableWidget.item(8, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem79 = self.memoria_tableWidget.item(8, 3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem80 = self.memoria_tableWidget.item(9, 0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem81 = self.memoria_tableWidget.item(9, 3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem82 = self.memoria_tableWidget.item(10, 0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem83 = self.memoria_tableWidget.item(10, 3)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem84 = self.memoria_tableWidget.item(11, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem85 = self.memoria_tableWidget.item(11, 3)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem86 = self.memoria_tableWidget.item(12, 0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"25", None));
        ___qtablewidgetitem87 = self.memoria_tableWidget.item(12, 3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem88 = self.memoria_tableWidget.item(13, 0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"27", None));
        ___qtablewidgetitem89 = self.memoria_tableWidget.item(13, 3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"28", None));
        ___qtablewidgetitem90 = self.memoria_tableWidget.item(14, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"29", None));
        ___qtablewidgetitem91 = self.memoria_tableWidget.item(14, 3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem92 = self.memoria_tableWidget.item(15, 0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"31", None));
        ___qtablewidgetitem93 = self.memoria_tableWidget.item(15, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"32", None));
        ___qtablewidgetitem94 = self.memoria_tableWidget.item(16, 0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"33", None));
        ___qtablewidgetitem95 = self.memoria_tableWidget.item(16, 3)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem96 = self.memoria_tableWidget.item(17, 0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"35", None));
        ___qtablewidgetitem97 = self.memoria_tableWidget.item(17, 3)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"36", None));
        ___qtablewidgetitem98 = self.memoria_tableWidget.item(18, 0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"37", None));
        ___qtablewidgetitem99 = self.memoria_tableWidget.item(18, 3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"38", None));
        ___qtablewidgetitem100 = self.memoria_tableWidget.item(19, 0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"39", None));
        ___qtablewidgetitem101 = self.memoria_tableWidget.item(19, 3)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem102 = self.memoria_tableWidget.item(20, 0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"41", None));
        ___qtablewidgetitem103 = self.memoria_tableWidget.item(20, 3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"42", None));
        ___qtablewidgetitem104 = self.memoria_tableWidget.item(21, 0)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem105 = self.memoria_tableWidget.item(21, 3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"44", None));
        ___qtablewidgetitem106 = self.memoria_tableWidget.item(22, 0)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem107 = self.memoria_tableWidget.item(22, 3)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"46", None));
        ___qtablewidgetitem108 = self.memoria_tableWidget.item(23, 0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"47", None));
        ___qtablewidgetitem109 = self.memoria_tableWidget.item(23, 3)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"48", None));
        ___qtablewidgetitem110 = self.memoria_tableWidget.item(24, 0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"49", None));
        ___qtablewidgetitem111 = self.memoria_tableWidget.item(24, 3)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"50", None));
        self.memoria_tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Procesos suspendidos:", None))
        ___qtablewidgetitem112 = self.suspendidos_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem113 = self.suspendidos_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
    # retranslateUi

