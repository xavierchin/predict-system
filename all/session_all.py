import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 100)
        self.setWindowTitle('Auto logout sign')
        self.signLabel = QLabel("請點選按鈕，否則一分鐘後系統將自動登出。") #可另外去設定顯示時間
        self.sessionCheckBtn  = QPushButton("ok")
        
        self.inputLayout = QFormLayout()
        self.inputLayout.addRow(self.signLabel)
        self.inputLayout.addRow(self.sessionCheckBtn)
        self.setLayout(self.inputLayout)

        self.sessionCheckBtn.clicked.connect(self.close) #未來在這邊接功能
        # 初始的計時器
        self.timer = QTimer()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())