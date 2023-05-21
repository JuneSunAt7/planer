import sys
from PyQt5 import QtWidgets, uic
import design
import filemanagment
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime
from PyQt5 import QtGui
import time
import datetime

# нам понадобится модуль winextras
from PyQt5.QtWinExtras import QWinTaskbarButton,QWinTaskbarProgress


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addButton.clicked.connect(self.add_task)
        self.currButton.clicked.connect(self.current_task)
        self.fireTaskButton.clicked.connect(self.fire_task)
        self.weekButton.clicked.connect(self.week_task)
        self.archiveButton.clicked.connect(self.arc_task)
        self.bthAdd.clicked.connect(self.save)
        self.tableWidget.itemDoubleClicked.connect(self.ready_task)
        self.delArchive.clicked.connect(self.deleteArc)

        self.difficultSlider.setRange(0, 5)
        self.difficultSlider.setValue(3)

        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)
        for j in range(len(filemanagment.read_curr())):
            for i in range(4):
                print(len(filemanagment.read_curr()))
                if len(filemanagment.read_curr()) == 26:
                    self.tableWidget.setItem(0, 0, QTableWidgetItem(''))
                else:
                    data = filemanagment.read_curr()[j].split('.')

                    self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))
                    curr_date = datetime.date.today()
                    date_object = datetime.datetime.strptime(data[1], '%Y-%m-%d').date()
                    timeTask = str((date_object-curr_date).days) + ' days'
                    self.tableWidget.setItem(j, 4, QTableWidgetItem(timeTask))
        filemanagment.m_to_archive()

    def __clear(self):
        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)
        self.tableWidget.setVisible(False)

    def add_task(self):
        self.__clear()
        self.frame.setVisible(True)

    def current_task(self):
        self.__clear()
        self.tableWidget.setVisible(True)

    def fire_task(self):
        self.__clear()
        self.fireTasksFrame.setVisible(True)
        for j in range(len(filemanagment.read_fired())):
            for i in range(4):
                print(len(filemanagment.read_fired()))
                if len(filemanagment.read_fired()) == 1:
                    self.firedTable.setItem(0, 0, QTableWidgetItem(''))
                else:
                    data = filemanagment.read_fired()[j].split('.')
                    self.firedTable.setItem(j, i, QTableWidgetItem(data[i]))

    def week_task(self):
        self.__clear()
        self.weekFrame.setVisible(True)
        for j in range(len(filemanagment.week_tasks())):
            for i in range(4):
                if len(filemanagment.week_tasks()) == 1:
                    self.mainTasksView.setItem(0, 0, QTableWidgetItem(''))
                else:
                    data = filemanagment.week_tasks()[j].split('.')
                    print(data)
                    self.mainTasksView.setItem(j, i, QTableWidgetItem(data[i]))

    def arc_task(self):
        self.__clear()
        self.archiveData.setVisible(True)
        self.arcTaskView.setText(filemanagment.read_arc())

    def save(self):
        times = self.deadlineTime.date().toPyDate()
        filemanagment.wr_to_main_file(str(self.lineInputTask.text()), str(times), str(self.difficultSlider.value()), str(self.resoursesList.toPlainText()).replace("\n", '&'))
        self.__clear()
        self.tableWidget.setVisible(True)
        msg = QtWidgets.QMessageBox()
        msg.setText('Task '+ self.lineInputTask.text() + ' added')
        msg.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 255, 213, 255), stop:1 rgba(184, 170, 255, 255));\n"
"border-radius:15px;")
        msg.exec()

    def ready_task(self):
        row = self.tableWidget.currentRow()
        if row > -1:
            self.tableWidget.removeRow(row)
            self.tableWidget.selectionModel().clearCurrentIndex()

    def deleteArc(self):
        filemanagment.delete()
        self.__clear()
        self.tableWidget.setVisible(True)
        msg = QtWidgets.QMessageBox()
        msg.setText('Archive deleted')
        msg.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 255, 213, 255), stop:1 rgba(184, 170, 255, 255));\n"
                          "border-radius:15px;")
        msg.exec()



def main():
    try:
        from ctypes import windll  # Only exists on Windows.
        myappid = 'gem13.PlanerJet.Alone.1.'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    filemanagment.read_curr()
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('alone.ico'))
    window = ExampleApp()
    window.setWindowIcon(QtGui.QIcon('alone.ico'))
    window.show()
    window.setFixedSize(940, 732)
    app.exec_()


if __name__ == '__main__':
    main()
