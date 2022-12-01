#兩顆大button
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
class MyWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.time_close = 0
    def initUI(self):
        self.setWindowTitle('預測線寬系統')
        self.resize(400, 200)

        # Elements
        self.powerEdit =  QLineEdit()
        self.speedEdit =  QLineEdit()
        self.timesEdit =  QLineEdit()
        self.predictBtn  = QPushButton("Prediction")
        self.predictResult1 = QLabel("Prediction Result")
        self.predictResult2 = QLabel("")
        self.logoutBtn  = QPushButton("logout")
        
        #Layout
        self.inputLayout = QFormLayout()
        self.inputLayout.addRow("power(w): ",self.powerEdit)
        self.inputLayout.addRow("speed: ",self.speedEdit)
        self.inputLayout.addRow("rate: ",self.timesEdit)

        self.powerEdit.setPlaceholderText('0W ~ 12W')
        self.speedEdit.setPlaceholderText('0 ~ 100 rate')
        self.timesEdit.setPlaceholderText('0 ~ 50 times')
        

        self.inputLayout.addRow(self.predictBtn,self.predictResult1)
        self.inputLayout.addRow(self.predictResult2)
        self.inputLayout.addRow(self.logoutBtn)
        self.setLayout(self.inputLayout)

        #定時器一，限制message提示框跳出的時間
        self.timer_message()
        
        # self.box = QMessageBox(QMessageBox.Question, '自動登出確認', '繼續使用系統？')
        # self.yes = self.box.addButton('yes', QMessageBox.YesRole)
        

    def timer_message(self):
        print('111')
        self.timer_1 = QTimer()
        min = 0.5
        times = min *60 *1000
        self.timer_1.start(times)
        self.timer_1.timeout.connect(self.showSessionMessage)
        print("out111")


    def showSessionMessage(self):
        print("Show the sesssion message")
        
        #如果介面仍沒有反應，在指定時間後直接退出
        min_out = 0.1
        times_out = min_out *60 *1000
        print("out qqq aaa")

        print(self.time_close)
        if self.time_close == 0:
            self.timer_1.stop()
            print("強制退出")
            # QTimer().singleShot(times_out, self.box.close)
            QTimer().singleShot(times_out, self.close)
            print("莫名閃退?")

        reply = QMessageBox.question(self, '繼續使用系統', '確定繼續使用系統？', QMessageBox.Yes |  QMessageBox.Cancel)
        
        # if reply == QMessageBox.Yes and (len(self.powerEdit.text()) == 0 or len(self.speedEdit.text()) == 0 or len(self.timesEdit.text()) == 0):
        if reply == QMessageBox.Yes :
            self.time_close = 69
            # self.timer_1.stop()
            print('不退出系統')
            self.timer_message()
            print("yes之後重新計時")
            #怪到爆
            

        # if reply == QMessageBox.Cancel:
        #     print('手動退出系統')
        #     self.time_close = 2

        
        # #手動退出，請直接閃退。
        # if self.time_close == 2:
        #     print("閃退")
        #     self.timer_2 = QTimer()
        #     min_2 = 0.01
        #     times_2= min_2 *60 *1000
        #     QTimer().singleShot(times_2, self.box.close)
        #     QTimer().singleShot(times_2, self.close)
        
        #self.timer_1.stop()
        print("out qqq")
        print(self.time_close)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())