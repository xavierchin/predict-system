import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import random
class Second_OTP(QTabWidget):
    def __init__(self):
        super(Second_OTP, self).__init__()
        self.setWindowTitle('#OTP Code 驗證')
        self.initUI()

    def initUI(self): 
        
        self.resize(500, 400)
        # Elements
        self.accountEdit =  QLineEdit()
        self.otpEdit =  QLineEdit()
        self.otpBtn  = QPushButton("送出OTP")
        self.Result1 = QLabel("")
        self.Result2 = QLabel("")
        self.systemBtn  = QPushButton("進入系統")
        self.systemBtn.setDisabled(True)

        #Layout
        self.inputLayout = QFormLayout()
        #self.inputLayout.addRow("帳號: ",self.accountEdit)
        self.inputLayout.addRow("OTP code: ",self.otpEdit)
        

        #self.accountEdit.setPlaceholderText('輸入帳號')
        self.otpEdit.setPlaceholderText('輸入OTP碼')
        self.otpEdit.setEchoMode(QLineEdit.Password) #密碼輸入框不顯示文字
        
        self.inputLayout.addRow(self.otpBtn)
        #self.inputLayout.addRow(self.Result1) 
        self.inputLayout.addRow(self.systemBtn)

        self.setLayout(self.inputLayout)
        # Button Event
        self.otpBtn.clicked.connect(self.checkOTP) #未來在這邊接功能
        self.systemBtn.clicked.connect(self.close)



    def checkOTP(self): 
        #OTP+STMP 寄信驗證OPT碼是否正確
        # otp = ''
        # for i in range(0,6):
        #     otp += str(random.randint(0,9))
        
        otp = "kershaw"
        if self.otpEdit.text() == otp:
            #畫面跳轉
            self.Result2.setText("登入成功")
            QMessageBox.information(None, 'congratulation', '驗證成功') #抓不到ok button事件
            self.systemBtn.setDisabled(False)
         
        else:
            self.Result2.setText("登入失敗")
            QMessageBox.critical(self, "Title", '驗證失敗')
            self.systemBtn.setDisabled(True)


class Third_mainUI(QMainWindow):
    def __init__(self):
        super(Third_mainUI, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle('Third_mainUI')
        # Button
        self.button = QPushButton(self)
        self.button.setGeometry(50, 50, 100, 40)
        self.button.setText('train client model')

        self.logoutBtn = QPushButton(self)
        self.logoutBtn.setGeometry(200, 200, 180, 30)
        self.logoutBtn.setText('logout out')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Second_OTP()
    c = Third_mainUI()
    a.show()
    a.systemBtn.clicked.connect(c.show)
    sys.exit(app.exec_())