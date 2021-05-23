import sys
import pickle
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


form_class = uic.loadUiType("MyAdmin.ui")[0]

class MyAdmin(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.date_info.setText(date.today().isoformat())

        self.daily_sales = {}

        self.read_sales()
        self.show_sales()

    def read_sales(self):
        try:
            with open("{}_sales.pickle".format(date.today().isoformat()), "rb") as iFile:
                self.daily_sales = pickle.load(iFile)
        except FileNotFoundError:
            pass

    def show_sales(self):
        total = 0
        self.tableWidget.clearContents()
        self.total_sum.setText("￦0")
        if self.daily_sales:
            for i, (k, v) in enumerate(self.daily_sales.items()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(v[0])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(v[1])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(v[2])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(v[1] * v[2])))
                total += v[1] * v[2]
            if len(str(total)) > 3:
                str_total = "￦" + str(total)[:-3] + "," + str(total)[-3:]
            self.total_sum.setText(str_total)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyAdmin()
    myWindow.show()
    app.exec_()