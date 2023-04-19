import sys
from PyQt5 import QtWidgets, uic
import design
import filemanagment
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime


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

        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)
        for j in range(len(filemanagment.read_curr())):
            for i in range(4):
                data = filemanagment.read_curr()[j].split(' ')
                self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))

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

    def week_task(self):
        self.__clear()
        self.weekFrame.setVisible(True)

    def arc_task(self):
        self.__clear()
        self.archiveData.setVisible(True)

    def save(self):
        times = self.deadlineTime.date().toPyDate()
        filemanagment.wr_to_main_file(self.lineInputTask.text(), str(times), 'hello', 'hello')


def main():
    filemanagment.read_curr()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
