import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests

class First_account(QTabWidget):
    def __init__(self):
        super(First_account, self).__init__()
        self.initUI()

    def initUI(self): 
        '''  
        # self.resize(400, 300)
        # self.setWindowTitle('驗證帳密')
        # # Button #排版要重新來
        # self.button = QPushButton(self)
        # self.button.setGeometry(150, 180, 100, 40)
        # self.button.setText('送出帳密')
        # self.textEditAccount = QTextEdit(self)
        # self.textEditAccount.setGeometry(120, 50, 160, 40)
        # self.textEditAccount.setPlaceholderText("帳號")
        # self.textEditPassword = QTextEdit(self)
        # self.textEditPassword.setGeometry(120, 100, 160, 40)
        # self.textEditPassword.setPlaceholderText("密碼")
        
        # self.mybutton = QPushButton(self)
        # self.button.setGeometry(50, 50, 50, 100)
        '''
        self.resize(400, 200)
        # Elements
        self.accountEdit =  QLineEdit()
        self.passwordEdit =  QLineEdit()
        self.authenticationBtn  = QPushButton("送出帳密")
        self.Result1 = QLabel("Authentication Result")
        self.Result2 = QLabel("")
        #self.predictResult2 = QLabel("correct or not")

        #Layout
        self.inputLayout = QFormLayout()
        self.inputLayout.addRow("account: ",self.accountEdit)
        self.inputLayout.addRow("password: ",self.passwordEdit)
        

        self.accountEdit.setPlaceholderText('輸入帳號')
        self.passwordEdit.setPlaceholderText('輸入密碼')
        self.passwordEdit.setEchoMode(QLineEdit.Password) #密碼輸入框不顯示文字
        
        self.inputLayout.addRow(self.authenticationBtn,self.Result2)
        self.inputLayout.addRow(self.Result1) 
        
        self.setLayout(self.inputLayout)
        # Button Event
        self.authenticationBtn.clicked.connect(self.clickme) #未來在這邊接功能



    def clickme(self): 
        #接上keycloak api
        if self.accountEdit.text() == "test" and self.passwordEdit.text() == "test":
            self.Result1.setText("登入成功")
        else:
            self.Result1.setText("登入失敗")
        '''
        # self.sub_window.textEditAccount.setPlainText(self.textEditAccount.toPlainText())
        # self.sub_window.textEditAccount.setReadOnly(True)
        # url = "http://localhost:8081/get_token"
        # payload={'account': self.textEditAccount.toPlainText(),'password': self.textEditPassword.toPlainText()}
        # response = requests.request("POST", url,data=payload)
        # if response.text == 'success':
        #    self.sub_window.show()
        # else:
        #    QMessageBox.critical(self, "Title", response.text)
        '''
        #FOR OTP: 
        # reply = QMessageBox.information(self, 'my messagebox', 'hello world',
        #     QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        # if reply == QMessageBox.Ok:
        #     self.Result1.setText("登入成功")
        #     #self.Result2.setText("Ok clicked.")
        # else:
        #     print('Close clicked.')
        #     self.Result1.setText("登入失敗")
        #     #self.Result2.setText("Close clicked.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = First_account()
    a.show()
    sys.exit(app.exec_())