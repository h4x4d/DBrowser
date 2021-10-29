import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QStyle, QTableWidgetItem


class Dbrowser(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DBrowser")
        MainWindow.resize(750, 650)
        app_icon = QtGui.QIcon()

        app_icon.addFile('img/db.png', QtCore.QSize(16, 16))
        app_icon.addFile('img/db.png', QtCore.QSize(24, 24))
        app_icon.addFile('img/db.png', QtCore.QSize(32, 32))
        app_icon.addFile('img/db.png', QtCore.QSize(48, 48))
        app_icon.addFile('img/db.png', QtCore.QSize(256, 256))
        MainWindow.setWindowIcon(app_icon)
        font = QtGui.QFont()
        font.setFamily("Golos")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.db = QtWidgets.QTableWidget(self.centralwidget)
        self.db.setGeometry(QtCore.QRect(380, 70, 340, 550))
        font = QtGui.QFont()
        font.setFamily("Golos")
        font.setPointSize(10)
        self.db.setFont(font)
        self.db.setObjectName("db")
        self.db.setColumnCount(0)
        self.db.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(380, 30, 220, 30))
        self.comboBox.setObjectName("comboBox")
        self.bd_r = QtWidgets.QPushButton(self.centralwidget)
        self.bd_r.setGeometry(QtCore.QRect(610, 30, 30, 30))
        self.bd_r.setObjectName("bd_r")
        self.bd_p = QtWidgets.QPushButton(self.centralwidget)
        self.bd_p.setGeometry(QtCore.QRect(650, 30, 30, 30))
        self.bd_p.setObjectName("bd_p")
        self.bd_c = QtWidgets.QPushButton(self.centralwidget)
        self.bd_c.setGeometry(QtCore.QRect(690, 30, 30, 30))
        self.bd_c.setObjectName("bd_c")
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(30, 30, 30, 30))
        self.btn_create.setObjectName("btn_create")
        self.btn_load = QtWidgets.QToolButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(70, 30, 30, 30))
        self.btn_load.setObjectName("btn_load")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(110, 30, 30, 30))
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(150, 30, 30, 30))
        self.btn_save.setObjectName("btn_save")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(190, 30, 30, 30))
        self.btn_close.setObjectName("btn_close")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 70, 191, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 85, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Golos")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sql = QtWidgets.QTextEdit(self.centralwidget)
        self.sql.setGeometry(QtCore.QRect(30, 110, 330, 120))
        self.sql.setObjectName("sql")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 245, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Golos")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.redact = QtWidgets.QTextEdit(self.centralwidget)
        self.redact.setGeometry(QtCore.QRect(30, 270, 330, 120))
        self.redact.setObjectName("redact")
        self.datas = QtWidgets.QListWidget(self.centralwidget)
        self.datas.setGeometry(QtCore.QRect(30, 430, 330, 190))
        self.datas.setObjectName("datas")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 405, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Golos")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sql_c = QtWidgets.QPushButton(self.centralwidget)
        self.sql_c.setGeometry(QtCore.QRect(331, 81, 30, 30))
        self.sql_c.setObjectName("sql_c")
        self.sql_l = QtWidgets.QPushButton(self.centralwidget)
        self.sql_l.setGeometry(QtCore.QRect(303, 81, 30, 30))
        self.sql_l.setObjectName("sql_l")
        self.redact_s = QtWidgets.QPushButton(self.centralwidget)
        self.redact_s.setGeometry(QtCore.QRect(331, 241, 30, 30))
        self.redact_s.setObjectName("redact_s")
        self.bd_close = QtWidgets.QPushButton(self.centralwidget)
        self.bd_close.setGeometry(QtCore.QRect(331, 401, 30, 30))
        self.bd_close.setObjectName("bd_close")
        self.bd_redact = QtWidgets.QPushButton(self.centralwidget)
        self.bd_redact.setGeometry(QtCore.QRect(303, 401, 30, 30))
        self.bd_redact.setObjectName("bd_redact")
        self.bd_plus = QtWidgets.QPushButton(self.centralwidget)
        self.bd_plus.setGeometry(QtCore.QRect(275, 401, 30, 30))
        self.bd_plus.setObjectName("bd_plus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        icon = QIcon("img/bx-window-close 2.png")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBrowser"))
        self.label.setText(_translate("MainWindow", "Выполнение SQL кода: "))
        self.label_2.setText(_translate("MainWindow", "Заполнение таблицы:"))
        self.label_3.setText(_translate("MainWindow", "Изменение структуры:"))
        icon = QIcon("img/create-bd.png")
        self.btn_create.setIcon(icon)
        icon = QIcon("img/open_bd.png")
        self.btn_load.setIcon(icon)
        icon = QIcon("img/refresh_bd.png")
        self.btn_refresh.setIcon(icon)
        icon = QIcon("img/close_bd.png")
        self.btn_close.setIcon(icon)
        icon = QIcon("img/save_bd.png")
        self.btn_save.setIcon(icon)
        self.btn_create.setIconSize(QSize(22, 22))
        self.btn_save.setIconSize(QSize(22, 22))
        self.btn_refresh.setIconSize(QSize(22, 22))
        self.btn_close.setIconSize(QSize(22, 22))
        self.btn_load.setIconSize(QSize(22, 22))

        icon = QIcon("img/run.png")
        self.sql_l.setIcon(icon)
        icon = QIcon("img/close.png")
        self.sql_c.setIcon(icon)
        icon = QIcon("img/save.png")
        self.redact_s.setIcon(icon)
        self.redact_s.setIconSize(QSize(20, 20))

        icon = QIcon("img/plus.png")
        self.bd_plus.setIcon(icon)
        icon = QIcon("img/pen.png")
        self.bd_redact.setIcon(icon)
        icon = QIcon("img/close.png")
        self.bd_close.setIcon(icon)

        icon = QIcon("img/refresh.png")
        self.bd_r.setIcon(icon)
        self.bd_r.setIconSize(QSize(22, 22))
        icon = QIcon("img/plus.png")
        self.bd_p.setIcon(icon)
        icon = QIcon("img/close.png")
        self.bd_c.setIcon(icon)
        self.btn_load.clicked.connect(self.table)
        self.db.itemSelectionChanged.connect(self.editor)

        self.comboBox.currentTextChanged.connect(self.baseselected)
        self.btn_save.clicked.connect(self.saver)


    def table(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            MainWindow, 'Открыть базу данных', '',
            'База данных (*.db);;Базы данных (*.sqlite);;Все файлы (*)')[0]
        self.conn = sqlite3.connect(fname)
        self.cur = self.conn.cursor()
        self.comboBox.clear()
        tables = self.cur.execute("""SELECT * FROM sqlite_master where type='table'""").fetchall()
        tables =[i[1] for i in tables]
        for i in tables:
            self.comboBox.addItem(i)

    def baseselected(self):
        a = self.comboBox.currentText()

        self.db.setRowCount(0)
        data = self.cur.execute(f"""SELECT * FROM {a}""").fetchall()
        column = [i[0] for i in self.cur.description]
        self.db.setColumnCount(len(column))
        column = [i for i in column]
        self.columns = column
        self.db.setHorizontalHeaderLabels(column)
        self.changed = {}
        for i, row in enumerate(data):
            self.db.insertRow(i)
            for j, elem in enumerate(row):
                self.db.setItem(i, j, QTableWidgetItem(str(elem)))
        self.db.itemChanged.connect(self.changer)

    def editor(self):
        b = [[i.column(), i.row()] for i in self.db.selectedIndexes()]
        res = {}
        for i in b:
            if i[1] in res:
                res[i[1]].append(self.db.item(i[1], i[0]).text())
            else:
                res[i[1]] = [self.db.item(i[1], i[0]).text()]
        n = []
        for i in res:
            n.append('; '.join(res[i]))
        self.redact.setText('\n'.join(n))

    def changer(self, changed):
        self.changed[(self.db.row(changed), self.db.column(changed))] = changed.text()

    def saver(self):
        print(self.changed)
        for i in self.changed:
            base = self.cur.execute(f'''SELECT * FROM {self.comboBox.currentText()}''').fetchall()[i[0]]
            a = f"""UPDATE {self.comboBox.currentText()} SET {self.columns[i[1]]} = '{self.changed[i]}' WHERE """
            b = ' AND '.join([f'{self.columns[j]} = "{i}"' for j, i in enumerate(base)])
            a = a + b
            print(a)
            self.cur.execute(a)
            self.conn.commit()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Dbrowser()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
