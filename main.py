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

        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)

        self.tableWidget.setItem(0, 0, QTableWidgetItem(filemanagment.read_curr()[0]))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(filemanagment.read_curr()[1]))
        self.tableWidget.setItem(0,3, QTableWidgetItem(filemanagment.read_curr()[2]))

        date = datetime.strptime(filemanagment.read_curr()[1], "%d.%m.%Y").date()
        today = datetime.today().date()
        print(today)
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(date)))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(filemanagment.read_curr()[3]))

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


def main():
    filemanagment.read_curr()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
