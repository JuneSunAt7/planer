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

        self.difficultSlider.setRange(0, 5)
        self.difficultSlider.setValue(3)

        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)
        for j in range(len(filemanagment.read_curr())):
            for i in range(4):
                data = filemanagment.read_curr()[j].split('.')
                self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))
        filemanagment.m_to_fired()
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
                data = filemanagment.read_fired()[j].split('.')
                self.firedTable.setItem(j, i, QTableWidgetItem(data[i]))

    def week_task(self):
        self.__clear()
        self.weekFrame.setVisible(True)

    def arc_task(self):
        self.__clear()
        self.archiveData.setVisible(True)

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


def main():
    filemanagment.read_curr()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    window.setFixedSize(940, 732)
    app.exec_()


if __name__ == '__main__':
    main()
