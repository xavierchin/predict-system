import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from authentication_function import authFuction

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainFrame = authFuction()
    mainFrame.show()
    sys.exit(app.exec_())