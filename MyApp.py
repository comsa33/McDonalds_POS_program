import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic
from MyCal import *
from MyOrder import *
from MyAdmin import *


form_class = uic.loadUiType("MyApp.ui")[0]


class cal_app(MyCal):
    def __init__(self):
        super().__init__()
        self.show()

class order_app(MyOrder):
    def __init__(self):
        super().__init__()
        self.show()

class admin_app(MyAdmin):
    def __init__(self):
        super(admin_app, self).__init__()


class MyApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.admin = admin_app()

        self.btn_cal.clicked.connect(cal_app)
        self.btn_order.clicked.connect(order_app)
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_admin.clicked.connect(self.admin.show)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyApp()
    myWindow.show()
    app.exec_()