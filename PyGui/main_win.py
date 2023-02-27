# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 800)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(17, 0, 75);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 270, 241, 51))
        self.textEdit.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 3px solid black;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(510, 140, 461, 341))
        self.textEdit_2.setStyleSheet("background-color: white;\n"
                                      "border: 3px solid;\n"
                                      "border-color : rgb(255, 120, 67);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color : rgb(255, 120, 67);")
        self.label.setObjectName("label")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(40, 370, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fontComboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border: 3px solid black;")
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : rgb(255, 120, 67);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 470, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 3px solid black;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 430, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color : rgb(255, 120, 67);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color : rgb(255, 120, 67);")
        self.label_4.setObjectName("label_4")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(
            self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(180, 580, 81, 81))
        self.commandLinkButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image\stop.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(70, 70))
        self.commandLinkButton.setObjectName("Stop_btn")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(
            self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(50, 580, 81, 91))
        self.commandLinkButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image\start.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(70, 70))
        self.commandLinkButton_2.setObjectName("start_btn")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(
            self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(910, 10, 81, 91))
        self.commandLinkButton_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Image\home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon2)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(70, 70))
        self.commandLinkButton_3.setObjectName("home_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(560, 550, 371, 191))
        self.frame.setStyleSheet("background-color: white;\n"
                                 "border: 3px solid;\n"
                                 "border-color : rgb(255, 120, 67);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(100, 30, 51, 51))
        self.commandLinkButton_7.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_7.setStyleSheet("border-color: white")
        self.commandLinkButton_7.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"Image\up.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_7.setIcon(icon3)
        self.commandLinkButton_7.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_7.setObjectName("up_btn")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(150, 60, 61, 61))
        self.commandLinkButton_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_4.setStyleSheet("border-color: white")
        self.commandLinkButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"Image\right.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon4)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton_4.setObjectName("right_btn")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(40, 60, 61, 71))
        self.commandLinkButton_5.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_5.setStyleSheet("border-color: white")
        self.commandLinkButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Image\left.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon5)
        self.commandLinkButton_5.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton_5.setObjectName("left_btn")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(100, 100, 51, 51))
        self.commandLinkButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setStyleSheet("border-color: white")
        self.commandLinkButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Image\down.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon6)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("down_btn")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 170, 0);\n"
                                   "border-color: white")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(210, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 170, 0);\n"
                                   "border-color: white")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 150, 31, 21))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 170, 0);\n"
                                   "border-color: white")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 31, 21))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 170, 0);\n"
                                   "border-color: white")
        self.label_8.setObjectName("label_8")
        self.commandLinkButton_8 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_8.setGeometry(QtCore.QRect(250, 20, 71, 61))
        self.commandLinkButton_8.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_8.setStyleSheet("border-color: white")
        self.commandLinkButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Image\z+.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_8.setIcon(icon7)
        self.commandLinkButton_8.setIconSize(QtCore.QSize(70, 70))
        self.commandLinkButton_8.setObjectName("z+_btn")
        self.commandLinkButton_9 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_9.setGeometry(QtCore.QRect(260, 100, 71, 71))
        self.commandLinkButton_9.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_9.setStyleSheet("border-color: white")
        self.commandLinkButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Image\z-.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_9.setIcon(icon8)
        self.commandLinkButton_9.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton_9.setObjectName("z-_btn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 170, 241, 51))
        self.textBrowser.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border: 3px solid black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color : rgb(255, 120, 67);")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.textEdit.textChanged.connect(self.pb_clicked)
        self.fontComboBox.currentFontChanged.connect(self.pb_clicked)
        self.comboBox.currentTextChanged.connect(self.pb_clicked)

    def pb_clicked(self):
        text = self.textEdit.toPlainText()
        fontt = self.fontComboBox.currentFont()
        sizee = self.comboBox.currentText()
        fontt.setPointSize(int(sizee))
        self.textEdit_2.setFont(fontt)
        self.textEdit_2.setText(text)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Text"))
        self.label_2.setText(_translate("MainWindow", "Font Family"))
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox.setItemText(2, _translate("MainWindow", "12"))
        self.comboBox.setItemText(3, _translate("MainWindow", "16"))
        self.comboBox.setItemText(4, _translate("MainWindow", "20"))
        self.comboBox.setItemText(5, _translate("MainWindow", "24"))
        self.comboBox.setItemText(6, _translate("MainWindow", "32"))
        self.comboBox.setItemText(7, _translate("MainWindow", "36"))
        self.comboBox.setItemText(8, _translate("MainWindow", "48"))
        self.label_3.setText(_translate("MainWindow", "Font Size"))
        self.label_4.setText(_translate("MainWindow", "G-Code Program"))
        self.label_5.setText(_translate("MainWindow", "Y+"))
        self.label_6.setText(_translate("MainWindow", "X+"))
        self.label_7.setText(_translate("MainWindow", "Y-"))
        self.label_8.setText(_translate("MainWindow", "X-"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Browse Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())