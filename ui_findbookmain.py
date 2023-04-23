# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 532)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pb_anay = QPushButton(self.centralwidget)
        self.pb_anay.setObjectName(u"pb_anay")
        self.pb_anay.setGeometry(QRect(620, 10, 75, 23))
        self.le_url = QLineEdit(self.centralwidget)
        self.le_url.setObjectName(u"le_url")
        self.le_url.setGeometry(QRect(100, 10, 511, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 61, 20))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 281, 381))
        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 20, 256, 351))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 70, 91, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 100, 91, 16))
        self.le_bookname = QLineEdit(self.centralwidget)
        self.le_bookname.setObjectName(u"le_bookname")
        self.le_bookname.setGeometry(QRect(410, 70, 241, 21))
        self.le_author = QLineEdit(self.centralwidget)
        self.le_author.setObjectName(u"le_author")
        self.le_author.setGeometry(QRect(410, 100, 241, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 150, 81, 16))
        self.le_conid = QLineEdit(self.centralwidget)
        self.le_conid.setObjectName(u"le_conid")
        self.le_conid.setGeometry(QRect(410, 150, 241, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 180, 81, 161))
        self.te_remove = QTextEdit(self.centralwidget)
        self.te_remove.setObjectName(u"te_remove")
        self.te_remove.setGeometry(QRect(410, 180, 241, 151))
        self.pb_retrieve = QPushButton(self.centralwidget)
        self.pb_retrieve.setObjectName(u"pb_retrieve")
        self.pb_retrieve.setGeometry(QRect(540, 350, 75, 23))
        self.le_retriveln = QLineEdit(self.centralwidget)
        self.le_retriveln.setObjectName(u"le_retriveln")
        self.le_retriveln.setGeometry(QRect(410, 350, 113, 21))
        self.lb_status = QLabel(self.centralwidget)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setGeometry(QRect(20, 430, 661, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 21))
        self.menuFind_Book = QMenu(self.menubar)
        self.menuFind_Book.setObjectName(u"menuFind_Book")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFind_Book.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Find a e-book", None))
        self.le_url.setText('https://www.shuquge9.com/txt/75236/')
        self.le_conid.setText('chaptercontent') # 正文所在的 div id=...
        self.pb_anay.setText(QCoreApplication.translate("MainWindow", u"anaylise", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"menu url:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"book name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"author:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"content id:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"remove tag:", None))
        self.pb_retrieve.setText(QCoreApplication.translate("MainWindow", u"retrieve ", None))
        self.le_retriveln.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"f:\project\\", None))
        self.menuFind_Book.setTitle(QCoreApplication.translate("MainWindow", u"Find Book", None))
    # retranslateUi

