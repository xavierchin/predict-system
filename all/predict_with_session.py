import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
sec  = 1
class MyWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.count = 0
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
        self.powerEdit.setPlaceholderText('0W ~ 12W')
        self.speedEdit.setPlaceholderText('0 ~ 100 rate')
        self.timesEdit.setPlaceholderText('0 ~ 50 times')

        self.threadStartBtn  = QPushButton("messageWindow thread start")
        self.threadEndBtn  = QPushButton("messageWindow thread end")
        
        #Layout
        self.inputLayout = QFormLayout()
        self.inputLayout.addRow("power(w): ",self.powerEdit)
        self.inputLayout.addRow("speed: ",self.speedEdit)
        self.inputLayout.addRow("rate: ",self.timesEdit)
        self.inputLayout.addRow(self.predictBtn,self.predictResult1)
        self.inputLayout.addRow(self.predictResult2)
        self.inputLayout.addRow(self.logoutBtn)
        self.inputLayout.addRow(self.threadStartBtn)
        self.inputLayout.addRow(self.threadEndBtn)
        self.setLayout(self.inputLayout)

        self.setThread()

         # Thread_Exit信號
        self.WorkThread_WindowExit = WorkThread_WindowExit()
        self.WorkThread_WindowExit.end_window.connect(self.closeWindow)
                
        #btn 信號
        self.threadStartBtn.clicked.connect(self.threadStart)
        self.threadEndBtn.clicked.connect(self.threadEnd)
    
    def setThread(self):
        # Thread_Qmessage信號
        self.WorkThread_Qmessage = WorkThread_Qmessage()
        self.WorkThread_Qmessage.timer.connect(self.countTime)
        self.WorkThread_Qmessage.end.connect(self.messageWindow)

    
    def countTime(self):
        global sec 
        sec += 1
        self.predictResult2.setText(str(sec))

    def messageWindow(self):
        #想辦法抓到ok事件
        reply = QMessageBox.question(self, '繼續使用系統', '確定繼續使用系統？', QMessageBox.Yes|  QMessageBox.Cancel)
        
        if reply == QMessageBox.Cancel :
            self.WorkThread_Qmessage.terminate()
            self.WorkThread_Qmessage.wait()
            self.count = 1
            self.WorkThread_WindowExit.start()

    def threadStart(self):
        self.WorkThread_Qmessage.start()
    
    def threadEnd(self):
        #強制暫停thread
        self.WorkThread_Qmessage.terminate()
        self.WorkThread_Qmessage.wait()
    
    def closeWindow(self):
        print("exit the window")
        self.close


#每30秒跳出提示框
class WorkThread_Qmessage(QThread):
    timer = pyqtSignal() # 每隔一秒發送一次信號
    end = pyqtSignal()   # 寄送完成後發送一次信號


    def run(self):
        while True:
            self.sleep(1) # 休眠一秒
            print(sec)
            if sec% 30 == 0:
                self.end.emit() #發送end信號
                
            self.timer.emit() #發送timer信號


#十秒後退出視窗
class WorkThread_WindowExit(QThread):
    end_window = pyqtSignal()   

    def run(self):
        #print("exit the window")
        while True:
            self.sleep(1) # 休眠一秒
            print(sec)
            if sec == 5:
                self.end_window.emit() #發送end信號
                #print("exit the window")
                break
            #self.timer.emit() #發送timer信號




    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    if w.count == 1:
        w.close()
    sys.exit(app.exec_())