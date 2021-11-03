import csv
import os
import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedWidth(459)
        Dialog.setFixedHeight(367)
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 400, 31))

        app_icon = QtGui.QIcon()
        app_icon.addFile('img/db.png', QtCore.QSize(16, 16))
        app_icon.addFile('img/db.png', QtCore.QSize(24, 24))
        app_icon.addFile('img/db.png', QtCore.QSize(32, 32))
        app_icon.addFile('img/db.png', QtCore.QSize(48, 48))
        app_icon.addFile('img/db.png', QtCore.QSize(256, 256))
        MainWindow.setWindowIcon(app_icon)

        font = QtGui.QFont()
        font.setFamily("Golos Text DemiBold")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(20, 70, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.btn_create = QtWidgets.QPushButton(Dialog)
        self.btn_create.setGeometry(QtCore.QRect(20, 99, 23, 23))
        self.btn_create.setText("")
        self.btn_create.setIconSize(QtCore.QSize(20, 20))
        self.btn_create.setObjectName("btn_create")
        self.bases = QtWidgets.QListWidget(Dialog)
        self.bases.setGeometry(QtCore.QRect(20, 130, 421, 191))
        self.bases.setObjectName("bases")
        self.btn_del = QtWidgets.QPushButton(Dialog)
        self.btn_del.setGeometry(QtCore.QRect(50, 99, 23, 23))
        self.btn_del.setText("")
        self.btn_del.setIconSize(QtCore.QSize(20, 20))
        self.btn_del.setObjectName("btn_del")
        self.name_2 = QtWidgets.QLineEdit(Dialog)
        self.name_2.setGeometry(QtCore.QRect(20, 40, 421, 25))
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        self.name_2.setFont(font)
        self.name_2.setObjectName("name_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(80, 100, 79, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.standart = QtWidgets.QLineEdit(Dialog)
        self.standart.setGeometry(QtCore.QRect(336, 100, 105, 20))
        self.standart.setObjectName("standart")
        self.notnull = QtWidgets.QCheckBox(Dialog)
        self.notnull.setGeometry(QtCore.QRect(164, 100, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        font.setPointSize(9)
        self.notnull.setFont(font)
        self.notnull.setObjectName("notnull")
        self.uniq = QtWidgets.QCheckBox(Dialog)
        self.uniq.setGeometry(QtCore.QRect(300, 100, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        font.setPointSize(9)
        self.uniq.setFont(font)
        self.uniq.setObjectName("uniq")
        self.ai = QtWidgets.QCheckBox(Dialog)
        self.ai.setGeometry(QtCore.QRect(255, 100, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        font.setPointSize(9)
        self.ai.setFont(font)
        self.ai.setObjectName("ai")
        self.pr_k = QtWidgets.QCheckBox(Dialog)
        self.pr_k.setGeometry(QtCore.QRect(210, 100, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Golos Text Medium")
        font.setPointSize(9)
        self.pr_k.setFont(font)
        self.pr_k.setObjectName("pr_k")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(20, 300, 421, 21))
        self.error_label.setAutoFillBackground(False)
        self.error_label.setStyleSheet("background-color:red;\nborder:1px solid black;")
        self.error_label.setObjectName("error_label")
        self.error_label.hide()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Создание и изменение таблиц"))
        self.label.setText(_translate("Dialog", "Создание таблицы"))
        self.name.setPlaceholderText(_translate("Dialog", "Название поля"))
        self.name_2.setPlaceholderText(_translate("Dialog", "Название таблицы"))
        self.comboBox.setItemText(0, _translate("Dialog", "INTEGER"))
        self.comboBox.setItemText(1, _translate("Dialog", "TEXT"))
        self.comboBox.setItemText(2, _translate("Dialog", "BLOB"))
        self.comboBox.setItemText(3, _translate("Dialog", "REAL"))
        self.comboBox.setItemText(4, _translate("Dialog", "NUMERIC"))
        self.standart.setPlaceholderText(_translate("Dialog", "Стандартное значение"))
        self.notnull.setText(_translate("Dialog", "НП"))
        self.uniq.setText(_translate("Dialog", "У"))
        self.ai.setText(_translate("Dialog", "АИ"))
        self.pr_k.setText(_translate("Dialog", "ПК"))

        self.bases.itemSelectionChanged.connect(self.selection)
        self.ai.setDisabled(True)
        self.comboBox.setDisabled(True)
        self.notnull.setDisabled(True)
        self.pr_k.setDisabled(True)
        self.uniq.setDisabled(True)
        self.standart.setDisabled(True)
        self.btn_del.setDisabled(True)
        self.btn_create.clicked.connect(self.creator)
        self.btn_del.clicked.connect(self.deleter)
        self.inb = []
        self.notnull.stateChanged.connect(self.params)
        self.pr_k.stateChanged.connect(self.params)
        self.uniq.stateChanged.connect(self.params)
        self.ai.stateChanged.connect(self.params)
        self.standart.textChanged.connect(self.params)
        self.comboBox.currentTextChanged.connect(self.params)

        icon = QtGui.QIcon("img/plus.png")
        self.btn_create.setIcon(icon)
        self.btn_create.setIconSize(QtCore.QSize(15, 15))
        icon = QtGui.QIcon("img/close.png")
        self.btn_del.setIcon(icon)
        self.btn_del.setIconSize(QtCore.QSize(13, 13))

    def selection(self):
        self.ai.setDisabled(False)
        self.notnull.setDisabled(False)
        self.pr_k.setDisabled(False)
        self.uniq.setDisabled(False)
        self.standart.setDisabled(False)
        self.btn_del.setDisabled(False)
        self.comboBox.setDisabled(False)
        select = self.inb[self.bases.selectedIndexes()[0].row()]
        self.comboBox.setCurrentText(select[1])
        self.notnull.setChecked(select[2])
        self.pr_k.setChecked(select[3])
        self.ai.setChecked(select[4])
        self.uniq.setChecked(select[5])
        if select[6]:
            self.standart.setText(select[6])
        else:
            self.standart.setText('')

    def creator(self):
        if self.name.text():
            if self.name.text() not in [i[0] for i in self.inb]:
                self.bases.addItem(self.name.text())
                self.inb.append([self.name.text(), 'INTEGER', False, False, False, False, None])
                self.name.setText('')
                self.error_label.hide()
            else:
                self.error_label.setText('Кажется, название повторяется')
                self.error_label.show()
        else:
            self.error_label.setText('Кажется, вы не указали название')
            self.error_label.show()

    def deleter(self):
        del self.inb[self.bases.selectedIndexes()[0].row()]
        self.bases.takeItem(self.bases.selectedIndexes()[0].row())

    def params(self):
        index = self.bases.selectedIndexes()[0].row()
        self.inb[index] = [self.inb[index][0], self.comboBox.currentText(), self.notnull.isChecked(),
                           True if self.ai.isChecked() else self.pr_k.isChecked(), self.ai.isChecked(),
                           self.uniq.isChecked(), self.standart.text()]
        if type(MainWindow.sender()) != QtWidgets.QComboBox:
            if MainWindow.sender().text() == 'АИ' and self.inb[index][4]:
                self.pr_k.setChecked(True)
                for n, j in enumerate(self.inb):
                    if j[4] and self.inb[index][0] != j[0]:
                        self.inb[n][3] = False
                        self.inb[n][4] = False

            if MainWindow.sender().text() == 'ПК' and self.inb[index][3] and not self.inb[index][4]:
                for n, j in enumerate(self.inb):
                    if j[4] and self.inb[index][0] != j[0]:
                        self.inb[index][3] = False
                        self.pr_k.setChecked(False)


class Dbrowser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DBrowser")
        MainWindow.setFixedHeight(650)
        MainWindow.setFixedWidth(750)
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
        self.comboBox.setGeometry(QtCore.QRect(380, 30, 181, 30))
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
        self.bd_csv = QtWidgets.QPushButton(self.centralwidget)
        self.bd_csv.setGeometry(QtCore.QRect(570, 30, 30, 30))
        self.bd_csv.setObjectName("bd_scv")
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
        self.bd_plus = QtWidgets.QPushButton(self.centralwidget)
        self.bd_plus.setGeometry(QtCore.QRect(303, 401, 30, 30))
        self.bd_plus.setObjectName("bd_plus")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 330, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color:red;\n"
                                   "border:1px solid black;")
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBrowser"))
        self.label.setText(_translate("MainWindow", "Выполнение SQL кода: "))
        self.label_2.setText(_translate("MainWindow", "Заполнение таблицы:"))
        self.label_3.setText(_translate("MainWindow", "Изменение структуры:"))
        icon = QtGui.QIcon("img/create-bd.png")
        self.btn_create.setIcon(icon)
        icon = QtGui.QIcon("img/open_bd.png")
        self.btn_load.setIcon(icon)
        icon = QtGui.QIcon("img/refresh_bd.png")
        self.btn_refresh.setIcon(icon)
        icon = QtGui.QIcon("img/close_bd.png")
        self.btn_close.setIcon(icon)
        icon = QtGui.QIcon("img/save_bd.png")
        self.btn_save.setIcon(icon)
        self.btn_create.setIconSize(QtCore.QSize(22, 22))
        self.btn_save.setIconSize(QtCore.QSize(22, 22))
        self.btn_refresh.setIconSize(QtCore.QSize(22, 22))
        self.btn_close.setIconSize(QtCore.QSize(22, 22))
        self.btn_load.setIconSize(QtCore.QSize(22, 22))

        icon = QtGui.QIcon("img/run.png")
        self.sql_l.setIcon(icon)
        icon = QtGui.QIcon("img/close.png")
        self.sql_c.setIcon(icon)
        icon = QtGui.QIcon("img/save.png")
        self.redact_s.setIcon(icon)
        self.redact_s.setIconSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon("img/plus.png")
        self.bd_plus.setIcon(icon)
        icon = QtGui.QIcon("img/close.png")
        self.bd_close.setIcon(icon)

        icon = QtGui.QIcon("img/refresh.png")
        self.bd_r.setIcon(icon)
        self.bd_r.setIconSize(QtCore.QSize(22, 22))
        icon = QtGui.QIcon("img/plus.png")
        self.bd_p.setIcon(icon)
        icon = QtGui.QIcon("img/close.png")
        self.bd_c.setIcon(icon)
        icon = QtGui.QIcon("img/csv.png")
        self.bd_csv.setIconSize(QtCore.QSize(22, 22))
        self.bd_csv.setIcon(icon)
        self.btn_load.clicked.connect(self.table)
        self.db.itemSelectionChanged.connect(self.editor)

        self.comboBox.currentTextChanged.connect(self.baseselected)
        self.btn_save.clicked.connect(self.saver)
        self.btn_create.clicked.connect(self.creator)
        self.bd_plus.clicked.connect(self.redactor)
        self.sql_c.clicked.connect(self.sql_cleaner)
        self.sql_l.clicked.connect(self.sql_loader)
        self.bd_close.clicked.connect(self.deleter_bases)
        self.btn_close.clicked.connect(self.deleter)
        self.bd_p.clicked.connect(self.line_creator)
        self.bd_r.clicked.connect(self.baseselected)
        self.db.itemChanged.connect(self.changer)
        self.bd_c.clicked.connect(self.line_deleter)
        self.bd_csv.clicked.connect(self.csv_from_table)
        self.btn_refresh.clicked.connect(self.update_table)
        self.redact_s.clicked.connect(self.update_button)
        self.conn = None
        self.cur = None
        self.selected_index = []

    def deleter(self):
        try:
            self.selected_index = []
            self.datas.clear()
            self.redact.clear()
            self.sql.clear()
            self.label_4.hide()
            self.db.setRowCount(0)
            self.db.setColumnCount(0)
            self.comboBox.clear()
            
            self.changerworking = 0
            self.columns = []
            self.conn.close()
            self.cur = None
            self.conn = None
        except:
            pass

    def update_table(self):
        self.deleted = {}
        self.datas.clear()
        self.comboBox.clear()
        tables = self.cur.execute("""SELECT * FROM sqlite_master where type='table'""").fetchall()
        tables = [i[1] for i in tables]
        for i in tables:
            self.datas.addItem(i)
            self.comboBox.addItem(i)

    def table(self):
        self.deleter()
        fname = QtWidgets.QFileDialog.getOpenFileName(
            MainWindow, 'Открыть базу данных', '',
            'База данных (*.db);;Базы данных (*.sqlite);;Все файлы (*)')[0]
        self.fname = fname
        self.conn = sqlite3.connect(fname)
        self.cur = self.conn.cursor()
        self.update_table()
        
        self.db.itemChanged.connect(self.changer)

    def baseselected(self):
        a = self.comboBox.currentText()
        if a == '':
            return

        self.db.setRowCount(0)
        data = self.cur.execute(f"""SELECT * FROM '{a}'""").fetchall()
        column = [i[0] for i in self.cur.description]
        self.db.setColumnCount(len(column))
        column = [i for i in column]
        self.columns = column
        self.changerworking = 1
        self.db.setHorizontalHeaderLabels(column)
        for i, row in enumerate(data):
            self.db.insertRow(i)
            for j, elem in enumerate(row):
                self.db.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))
        self.changerworking = 0

    def editor(self):
        b = [[i.row(), i.column()] for i in self.db.selectedIndexes()]
        if len(b) == 1:
            self.selected_index = b[0]
            self.redact.setText(self.db.item(b[0][0], b[0][1]).text())
        elif len(b) > 0:
            self.redact.setText('Выберите не больше 1 объекта для редактирования!')
        else:
            self.redact.setText('')

    def changer(self, changed):
        if not self.changerworking:
            i = [self.db.row(changed), self.db.column(changed), changed.text()]
            base = self.cur.execute(f"""SELECT * FROM '{self.comboBox.currentText()}'""").fetchall()[i[0]]
            a = f"""UPDATE "{self.comboBox.currentText()}" SET "{self.columns[i[1]]}" = "{i[2]}" WHERE
            ROWID = (SELECT MIN(ROWID) FROM "{self.comboBox.currentText()}" WHERE """
            b = ' AND '.join([f'"{self.columns[j]}" = "{i}"' if i is not None else f'"{self.columns[j]}" IS NULL'
                              for j, i in enumerate(base)])
            a = a + b + ')'
            self.cur.execute(a)

    def update_button(self):
        if self.selected_index:
            selected = self.comboBox.currentText()
            base = self.cur.execute(f"""SELECT * FROM '{selected}'""").fetchall()[
                self.selected_index[0]]
            a = f"""UPDATE "{selected}" SET "{self.columns[self.selected_index[1]]}" = 
            "{self.redact.toPlainText()}" WHERE
                        ROWID = (SELECT MIN(ROWID) FROM "{selected}" WHERE """
            b = ' AND '.join([f'"{self.columns[j]}" = "{i}"' if i is not None else f'"{self.columns[j]}" IS NULL'
                              for j, i in enumerate(base)])
            a = a + b + ')'
            self.cur.execute(a)
            self.update_table()
            self.comboBox.setCurrentText(selected)

    def saver(self):
        self.conn.commit()

    def creator(self):
        self.deleter()
        fname = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, 'Открыть базу данных', '',
            'База данных (*.db);;Базы данных (*.sqlite);;Все файлы (*)')[0]
        self.fname = fname
        if os.path.exists(fname):
            os.remove(fname)
        self.conn = sqlite3.connect(fname)
        self.cur = self.conn.cursor()

    def redactor(self):
        Dialog = QtWidgets.QDialog()
        dlg = Ui_Dialog()
        dlg.setupUi(Dialog)
        button = Dialog.exec_()
        if button:
            names = ',\n'.join([f"'{i[0]}' {i[1]} {'NOT NULL' if i[2] else ''} {f'DEFAULT {i[6]}' if i[6] else ''} "
                                f"{'UNIQUE' if i[5] else ''} {f'DEFAULT {i[6]}' if i[6] else ''}" for i in dlg.inb])
            pkeys = []
            for i in dlg.inb:
                if i[3] and i[4]:
                    pkeys = f'PRIMARY KEY("{i[0]}" AUTOINCREMENT)'
                    break
                elif i[3]:
                    pkeys.append(f'"{i[0]}"')
            if not pkeys:
                pkeys = ''
            elif type(pkeys) == list:
                pkeys = f'PRIMARY KEY({",".join(pkeys)})'

            self.cur.execute(f"""CREATE TABLE '{dlg.name_2.text()}' (
                    {names}{',' if pkeys else ''}
                    {pkeys});
                    """)
            self.update_table()

    def deleter_bases(self):
        n = self.datas.selectedItems()[0].text()
        self.cur.execute(f"""PRAGMA foreign_keys = OFF;""")
        self.cur.execute(f"""DROP TABLE '{n}';""")
        self.cur.execute("""PRAGMA foreign_keys = ON;""")
        self.update_table()

    def sql_cleaner(self):
        self.sql.clear()
        self.label_4.hide()

    def sql_loader(self):
        try:
            self.label_4.hide()
            self.db.setRowCount(0)
            a = self.sql.toPlainText()
            n = self.cur.execute(a)
            if "select" in a.lower():
                self.changerworking = 1
                data = n.fetchall()
                column = [i[0] for i in self.cur.description]
                self.db.setColumnCount(len(column))
                column = [i for i in column]
                self.columns = column
                self.db.setHorizontalHeaderLabels(column)
                for i, row in enumerate(data):
                    self.db.insertRow(i)
                    for j, elem in enumerate(row):
                        self.db.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))
            else:
                self.changerworking = 1
                self.update_table()
            self.label_4.setText('Запрос выполнен успешно!')
            self.label_4.show()
            self.label_4.setStyleSheet("background-color:lightgreen;\n"
                                       "border:1px solid black;")
            self.changerworking = 0

        except AttributeError:
            self.label_4.setText('Кажется, вы не открыли базу данных...')
            self.label_4.setStyleSheet("background-color:red;\n"
                                       "border:1px solid black;")
            self.label_4.show()
        except sqlite3.OperationalError:
            self.label_4.setText('Где-то в запросе ошибка...')
            self.label_4.setStyleSheet("background-color:red;\n"
                                       "border:1px solid black;")
            self.label_4.show()

    def line_creator(self):
        try:
            selected = self.comboBox.currentText()
            self.cur.execute(f'INSERT INTO "{self.comboBox.currentText()}" DEFAULT VALUES;')
            self.changerworking = 1
            self.update_table()
            self.changerworking = 0
            self.comboBox.setCurrentText(selected)
        except sqlite3.IntegrityError:
            fields = self.cur.execute(
                f"""SELECT SQL FROM sqlite_master where type='table' and name ='{self.comboBox.currentText()}'""").fetchall()[
                0][0].split('\n')
            insert_fields = []
            insert_values = []
            for field in fields:
                params = field.split()
                if params[0][1:-1] == self.comboBox.currentText() + 'Id':
                    continue
                if params[0][0] == '[':
                    if params[1][-1] == ',':
                        continue
                    else:
                        field_type = params[1]
                    field_name = params[0][1:-1]
                    insert_fields.append(field_name)
                    field_constraint = ""
                    if field_type == 'INTEGER' or field_type.find('INT') == 0 or field_type == 'TINYINT' or \
                            field_type == 'SMALLINT' or field_type == 'MEDIUMINT' or field_type == 'BIGINT' or \
                            field_type == 'UNSIGNED BIG INT':
                        field_constraint += "1"
                    if field_type == 'DATETIME' or field_type == 'DATE':
                        field_constraint += "CURRENT_TIMESTAMP"
                    if field_type.find('NUMERIC') == 0 or field_type.find('DECIMAL') == 0 or \
                            field_type.find('BOOLEAN') == 0:
                        field_constraint += "0"
                    if field_type.find('NVARCHAR') == 0 or field_type.find('CHARACTER') == 0 or \
                            field_type.find('VARCHAR') == 0 or field_type.find('VARYING CHARACTER') == 0 or \
                            field_type.find('NCHAR') == 0 or field_type.find('NATIVE CHARACTER') == 0 or \
                            field_type == 'TEXT' or field_type == 'CLOB':
                        field_constraint += "' '"
                    insert_values.append(field_constraint)
            a = f"""INSERT INTO "{self.comboBox.currentText()}" ({','.join([f'"{i}"' for i in
                                                                            insert_fields])})
                                            VALUES({','.join([f'{i}' for i in insert_values])})"""
            self.cur.execute(a)
            self.update_table()
            self.comboBox.setCurrentText(selected)

    def line_deleter(self):
        selected = self.comboBox.currentText()
        base = self.db.selectedIndexes()
        base = [i.row() for i in base]
        n = self.cur.execute(f'SELECT * FROM "{selected}"').fetchall()
        for i in base:
            nn = n[i]
            a = f"""DELETE from {selected} WHERE ROWID = (SELECT MIN(ROWID) FROM "{selected}" WHERE """
            b = ' AND '.join([f'"{self.columns[j]}" = "{i}"' if i is not None else f'"{self.columns[j]}" IS NULL'
                              for j, i in enumerate(nn)])
            a = a + b + ')'
            self.cur.execute(a)
        self.changerworking = 1
        self.update_table()
        self.changerworking = 0
        self.comboBox.setCurrentText(selected)

    def csv_from_table(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, 'Сохранить CSV файл', '',
            'CSV файлы (*.csv);;Текстовые файлы (*.txt);;Все файлы (*)')[0]
        if os.path.exists(fname):
            os.remove(fname)
        f = open(fname, 'w', encoding='utf-8')
        write = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = self.cur.execute(f'SELECT * FROM "{self.comboBox.currentText()}"')
        write.writerow(self.columns)
        for i in data:
            write.writerow(i)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Dbrowser()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
