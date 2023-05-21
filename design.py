# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import filemanagment

from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 732)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(153, 215, 255, 255), stop:1 rgba(128, 145, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 10, 150, 60))
        self.addButton.setStyleSheet("background-color: rgb(145, 188, 125);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;")
        self.addButton.setObjectName("addButton")
        self.currButton = QtWidgets.QPushButton(self.centralwidget)
        self.currButton.setGeometry(QtCore.QRect(200, 10, 150, 60))
        self.currButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(84, 175, 255);\n"
"border-radius: 15px;")
        self.currButton.setObjectName("currButton")
        self.fireTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.fireTaskButton.setGeometry(QtCore.QRect(390, 10, 150, 60))
        self.fireTaskButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(32, 147, 255);\n"
"border-radius: 15px;\n"
"border-color: rgb(255, 115, 0);")
        self.fireTaskButton.setObjectName("fireTaskButton")
        self.weekButton = QtWidgets.QPushButton(self.centralwidget)
        self.weekButton.setGeometry(QtCore.QRect(580, 10, 150, 60))
        self.weekButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(32, 147, 255);\n"
"border-radius: 15px;")
        self.weekButton.setObjectName("weekButton")
        self.archiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.archiveButton.setGeometry(QtCore.QRect(770, 10, 150, 60))
        self.archiveButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(32, 147, 255);\n"
"border-radius:15px;")
        self.archiveButton.setObjectName("archiveButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 861, 591))
        self.tableWidget.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 255, 213, 255), stop:1 rgba(184, 170, 255, 255));\n"
"border-radius:15px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(filemanagment.read_curr()))
        item = QtWidgets.QTableWidgetItem()
        for i in range(len(filemanagment.read_curr())):
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 90, 821, 681))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame.setObjectName("frame")
        self.lblTaskName = QtWidgets.QLabel(self.frame)
        self.lblTaskName.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.lblTaskName.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(118, 141, 206,0);\n"
"border-radius: 15px;")
        self.lblTaskName.setObjectName("lblTaskName")
        self.deadlineTask = QtWidgets.QLabel(self.frame)
        self.deadlineTask.setGeometry(QtCore.QRect(10, 90, 101, 41))
        self.deadlineTask.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(118, 141, 206,0);\n"
"border-radius: 15px;")
        self.deadlineTask.setObjectName("deadlineTask")
        self.lblDiff = QtWidgets.QLabel(self.frame)
        self.lblDiff.setGeometry(QtCore.QRect(10, 160, 101, 41))
        self.lblDiff.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(118, 141, 206,0);\n"
"border-radius: 15px;")
        self.lblDiff.setObjectName("lblDiff")
        self.resoursesLbl = QtWidgets.QLabel(self.frame)
        self.resoursesLbl.setGeometry(QtCore.QRect(10, 230, 111, 41))
        self.resoursesLbl.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(118, 141, 206,0);\n"
"border-radius: 15px;")
        self.resoursesLbl.setObjectName("resoursesLbl")
        self.lineInputTask = QtWidgets.QLineEdit(self.frame)
        self.lineInputTask.setGeometry(QtCore.QRect(160, 20, 501, 51))
        self.lineInputTask.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(166, 168, 255);;\n"
"border-radius: 15px;")
        self.lineInputTask.setObjectName("lineInputTask")
        self.deadlineTime = QtWidgets.QDateTimeEdit(self.frame)
        currentTime = QtCore.QDateTime.currentDateTime()
        self.deadlineTime.setDateTime(currentTime.addDays(7))
        self.deadlineTime.setGeometry(QtCore.QRect(160, 90, 251, 41))
        self.deadlineTime.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(166, 168, 255);\n"
"border-radius: 15px;")
        self.deadlineTime.setObjectName("deadlineTime")
        self.difficultSlider = QtWidgets.QSlider(self.frame)
        self.difficultSlider.setGeometry(QtCore.QRect(170, 170, 160, 22))
        self.difficultSlider.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(166, 168, 255);\n"
"border-radius: 15px;")
        self.difficultSlider.setOrientation(QtCore.Qt.Horizontal)
        self.difficultSlider.setObjectName("difficultSlider")
        self.resoursesList = QtWidgets.QTextEdit(self.frame)
        self.resoursesList.setGeometry(QtCore.QRect(160, 230, 471, 231))
        self.resoursesList.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(166, 168, 255);\n"
"border-radius:15px;")
        self.resoursesList.setObjectName("resoursesList")
        self.bthAdd = QtWidgets.QPushButton(self.frame)
        self.bthAdd.setGeometry(QtCore.QRect(330, 500, 250, 80))
        self.bthAdd.setStyleSheet("background-color: rgb(145, 188, 125);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;")
        self.bthAdd.setObjectName("bthAdd")

        self.weekFrame = QtWidgets.QFrame(self.centralwidget)
        self.weekFrame.setGeometry(QtCore.QRect(-30, 110, 981, 521))
        self.weekFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weekFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weekFrame.setObjectName("weekFrame")
        self.maintaskLbl = QtWidgets.QLabel(self.weekFrame)
        self.maintaskLbl.setGeometry(QtCore.QRect(40, 300, 71, 31))
        self.maintaskLbl.setStyleSheet("border-radius: 15px;\n"
"background-color: rgba(0,0,0,0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.maintaskLbl.setObjectName("maintaskLbl")
        self.mainTasksView = QtWidgets.QTableWidget(self.weekFrame)
        self.mainTasksView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mainTasksView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainTasksView.setShowGrid(False)
        self.mainTasksView.setGeometry(QtCore.QRect(150, 30, 701, 400))
        self.mainTasksView.setStyleSheet("border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.630682, x2:1, y2:0.688, stop:0 rgba(253, 220, 220, 255), stop:1 rgba(204, 194, 255, 255));\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.mainTasksView.setObjectName("mainTasksView")
        self.mainTasksView.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.mainTasksView.setRowCount(len(filemanagment.week_tasks()))
        for i in range(len(filemanagment.week_tasks())):
            self.mainTasksView.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
        item = QtWidgets.QTableWidgetItem()
        self.mainTasksView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTasksView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTasksView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTasksView.setHorizontalHeaderItem(3, item)
        self.fireTasksFrame = QtWidgets.QFrame(self.centralwidget)
        self.fireTasksFrame.setGeometry(QtCore.QRect(-20, 80, 901, 671))
        self.fireTasksFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fireTasksFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fireTasksFrame.setObjectName("fireTasksFrame")
        self.firedTable = QtWidgets.QTableWidget(self.fireTasksFrame)
        self.firedTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.firedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.firedTable.setShowGrid(False)
        self.firedTable.setGeometry(QtCore.QRect(50, 100, 861, 491))
        self.firedTable.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 251, 134, 255), stop:1 rgba(255, 169, 112, 255));\n"
"border-radius:15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.firedTable.setObjectName("firedTable")
        self.firedTable.setColumnCount(4)
        self.firedTable.setRowCount(len(filemanagment.read_fired()))
        item = QtWidgets.QTableWidgetItem()
        for i in range(len(filemanagment.read_fired())):
            self.firedTable.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
        item = QtWidgets.QTableWidgetItem()
        self.firedTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.firedTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.firedTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.firedTable.setHorizontalHeaderItem(3, item)
        self.firePng = QtWidgets.QLabel(self.fireTasksFrame)
        self.firePng.setGeometry(QtCore.QRect(60, 430, 71, 71))
        self.firePng.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.firePng.setText("")
        self.firePng.setPixmap(QtGui.QPixmap("D:/Apps/imgonline-com-ua-Resize-SaP3ra2s6GBPUg.png"))
        self.firePng.setObjectName("firePng")
        self.firePng_2 = QtWidgets.QLabel(self.fireTasksFrame)
        self.firePng_2.setGeometry(QtCore.QRect(140, 430, 71, 71))
        self.firePng_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.firePng_2.setText("")
        self.firePng_2.setPixmap(QtGui.QPixmap("D:/Apps/imgonline-com-ua-Resize-SaP3ra2s6GBPUg.png"))
        self.firePng_2.setObjectName("firePng_2")
        self.firePng_3 = QtWidgets.QLabel(self.fireTasksFrame)
        self.firePng_3.setGeometry(QtCore.QRect(240, 430, 71, 71))
        self.firePng_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.firePng_3.setText("")
        self.firePng_3.setPixmap(QtGui.QPixmap("D:/Apps/imgonline-com-ua-Resize-SaP3ra2s6GBPUg.png"))
        self.firePng_3.setObjectName("firePng_3")
        self.firePng_4 = QtWidgets.QLabel(self.fireTasksFrame)
        self.firePng_4.setGeometry(QtCore.QRect(330, 430, 71, 71))
        self.firePng_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.firePng_4.setText("")
        self.firePng_4.setPixmap(QtGui.QPixmap("D:/Apps/imgonline-com-ua-Resize-SaP3ra2s6GBPUg.png"))
        self.firePng_4.setObjectName("firePng_4")
        self.archiveData = QtWidgets.QFrame(self.centralwidget)
        self.archiveData.setGeometry(QtCore.QRect(-11, 79, 1021, 641))
        self.archiveData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.archiveData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.archiveData.setObjectName("archiveData")
        self.delArchive = QtWidgets.QPushButton(self.archiveData)
        self.delArchive.setGeometry(QtCore.QRect(690, 560, 151, 41))
        self.delArchive.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 124, 115);\n"
"border-radius: 15px;\n"
"border-color: rgb(255, 115, 0);")
        self.delArchive.setObjectName("delArchive")
        self.arcTaskView = QtWidgets.QTextBrowser(self.archiveData)
        self.arcTaskView.setGeometry(QtCore.QRect(40, 110, 891, 421))
        self.arcTaskView.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(250, 255, 144);\n"
"border-radius:15px;")
        self.arcTaskView.setObjectName("arcTaskView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PlanerJet Alone", "PlanerJet Alone"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.currButton.setText(_translate("MainWindow", "Current"))
        self.fireTaskButton.setText(_translate("MainWindow", "Fire tasks"))
        self.weekButton.setText(_translate("MainWindow", "Week"))
        self.archiveButton.setText(_translate("MainWindow", "Archive"))
        item = self.tableWidget.verticalHeaderItem(0)
        for i in range(len(filemanagment.read_curr())):
            item.setText(_translate("MainWindow", str(i)))
            item = self.tableWidget.verticalHeaderItem(i)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "task"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "deadline"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "difficult"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resources"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "time"))
        self.lblTaskName.setText(_translate("MainWindow", "Task name"))
        self.deadlineTask.setText(_translate("MainWindow", "Deadline"))
        self.lblDiff.setText(_translate("MainWindow", "Difficulty"))
        self.resoursesLbl.setText(_translate("MainWindow", "Resourses"))
        self.bthAdd.setText(_translate("MainWindow", "Add task"))
        self.maintaskLbl.setText(_translate("MainWindow", "Week: "))
        item = self.mainTasksView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "task"))
        item = self.mainTasksView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "deadline"))
        item = self.mainTasksView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "diff"))
        item = self.mainTasksView.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "res"))
        item = self.firedTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "task"))
        item = self.firedTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "deadline"))
        item = self.firedTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "difficult"))
        item = self.firedTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "resources"))
        self.delArchive.setText(_translate("MainWindow", "delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
