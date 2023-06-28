import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication ,QWidget,QTabWidget

class main_window(QTabWidget):
    def __init__(self):
        super(main_window,self).__init__()
        self.setWindowTitle("机器操作1.0")

        self.operation1 = QWidget()
        self.operation2 = QWidget()
        self.operation3 = QWidget()
        self.addTab(self.operation1,"施工操作")
        self.addTab(self.operation2,"保养操作")
        self.addTab(self.operation3,"参数修改操作")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = main_window()
    mainwindow.show()
    sys.exit(app.exec_())