# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
import sys
import os
from PyQt4 import QtCore, QtGui
import socketserver
from os.path import exists
import time, datetime
import threading
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PyQt4.QtCore import *

HOST = ''
PORT = 7777
progressBar_statusValue =0

# MyDiag.py 모듈 import
import test1

class MySignal(QtCore.QObject):
    signal1 = QtCore.pyqtSignal(QtCore.QObject)
    def run(self):
        self.signal1.emit(self)

class MySignal2(QtCore.QObject):
    signal2 = QtCore.pyqtSignal(QtCore.QObject)
    def run(self):
        self.signal2.emit(self)

mysignal = MySignal()
mysignal2 = MySignal2()

# MyDiag 모듈 안의 Ui_MyDialog 클래스로부터 파생
class XDialog(QDialog, test1.Ui_Dialog):
    global progressBar_statusValue

    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        #self.pushButton_2.clicked.connect(self.imageRefresh) 
        
        mysignal.signal1.connect(self.imageRefresh)
        mysignal2.signal2.connect(self.resetProgressbar)

    def run(self):
        runServer()
        #while progressBar_statusValue < 100:
        #    self.progressBar.setValue(progressBar_statusValue)
        #self.progressBar.setValue(100)
		
    @pyqtSlot()
    def imageRefresh(self):
        #self.setupUi.label.setText("첫번째 버튼")
        im = Image.open('download/test.jpg') # Image Open & Resize
        size = (500,500)
        im.thumbnail(size)
        im.save('download/test.jpg')         # added by tom
        self.label.setPixmap(QPixmap("download/test.jpg"))

    @pyqtSlot()
    def resetProgressbar(self):
        while progressBar_statusValue < 100:
            self.progressBar.setValue(progressBar_statusValue)
        self.progressBar.setValue(100)

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global progressBar_statusValue
        dataTransferred = 0
        print('[Connected to: %s]' %self.client_address[0])
		
        fileInfo = self.request.recv(1024) # 클라이언트로 부터 파일이름을 전달받음
        fileInfo = fileInfo.decode() # 파일이름 이진 바이트 스트림 데이터를 일반 문자열로 변환
		
        fileInfo_parsing = fileInfo.split(',')
        fileName = fileInfo_parsing[0]
        fileSize = fileInfo_parsing[1]
        print('[fileSize] : ', str(fileSize))

        f = open('download/' + fileName, 'wb')
        data = self.request.recv(4096)
        cur_time = datetime.datetime.now()
        mysignal2.run()
        while  data:
            f.write(data)
            dataTransferred += len(data)
            progressBar_statusValue = ( dataTransferred/int(fileSize) ) * 100
            data = self.request.recv(4096)
        cur_time1 = datetime.datetime.now()

        print('[recved time] : ', str(cur_time))
        print('[recved1 time] : ', str(cur_time1))
        print('[File]: %s , [Size]: %d Bytes' %(fileName, dataTransferred))
        print('[Comeplete]')
        print('[recving time] : ', str(cur_time1-cur_time))
        mysignal.run()
        
def runServer():
    print('[Server Start]')
    print("[To terminate, Press 'Ctrl + C']")
	
    try:
        server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
        #server.serve_forever()
        threading.Thread(target=server.serve_forever).start()
    except KeyboardInterrupt:
        print('[Terminate]')	

app = QApplication(sys.argv)
dlg = XDialog()
dlg.show()
app.exec_()