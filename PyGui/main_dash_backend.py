from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import os
import subprocess
import sys
from main_dash import Ui_MainWindow

class Dashboard(QtWidgets.QMainWindow):
    clk_time = QtCore.QTimer()
    my_signal = pyqtSignal(int)  # Create a signal instance here

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText(time.strftime('%I:%M %p'))
        self.ui.label_2.setText(time.strftime('%b %d %Y'))
        self.ui.label_3.setText(time.strftime('%A'))
        self.clk_time.timeout.connect(self.update_clock)
        self.clk_time.start(1000)
        self.clk_time.setSingleShot(False)
        self.ui.commandLinkButton_5.clicked.connect(self.handle_shutdown)
        self.ui.commandLinkButton_4.clicked.connect(self.loadAnotherFile)

        # Connect the signal to a slot
        self.my_signal.connect(self.my_slot)

    def handle_shutdown(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText('Do you really want to Shutdown the system..!!!')
        msg.setWindowTitle('System Shutdown')
        msg.addButton('Shutdown', QtWidgets.QMessageBox.YesRole)
        msg.addButton('Reboot', QtWidgets.QMessageBox.ResetRole)
        msg.addButton('Cancel', QtWidgets.QMessageBox.NoRole)
        retval = msg.exec_()
        print('value of pressed message box button:{0}'.format(retval))
        if retval == 1:
            os.system('shutdown /s /t 1')

        elif retval == 0:
            os.system('shutdown /r /t 1')

        self.my_signal.emit(1)

    def my_slot(self, value):
        # This function will be called when the signal is emitted
        print("Signal emitted with value:", value)

    def loadAnotherFile(self):
        subprocess.Popen([sys.executable, "PyGui/main_win.py"])

    def update_clock(self):
        self.ui.label.setText(time.strftime('%I:%M:%S %p'))
        self.ui.label_2.setText(time.strftime('%b %d %Y'))
        self.ui.label_3.setText(time.strftime('%A'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
