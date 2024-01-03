from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys
import sqlite3


class Espresso(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 170)
        self.tableWidget.setColumnWidth(4, 140)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 150)
        self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("coffee.sqlite")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM cofees LIMIT 50"
        self.tableWidget.setRowCount(50)
        tablerow = 0
        for row in cur.execute(sqlquery):
            for i in range(7):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(row[i]))
            tablerow += 1


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec_())