import sys
import os
from PyQt5 import QtWidgets, uic
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_task)
        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)

    def add_task(self):
        self.tableWidget.setVisible(False)
        self.frame.setVisible(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()