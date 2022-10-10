import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter
 
from vector import vector
from threading import Thread
import time
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
class CWidget(QWidget):
 
    def __init__(self):
        super().__init__()
        #��ġ����
        self.location = vector(self.width()/2, self.height()/2)
        #�ӵ�����
        self.velocity = vector()
        #���ӵ�����
        self.acceleration = vector()
        #���콺 ��ǥ
        self.pt = vector(self.width()/2, self.height()/2)
        self.d = 50
        self.r = self.d/2
 
        self.thread = Thread(target=self.threadFunc)
        self.bThread = False
 
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('move')
        self.setMouseTracking(True)
        self.bThread = True
        self.thread.start()
        self.show()        
 
    def mouseMoveEvent(self, e):
        self.pt.x = e.x()
        self.pt.y = e.y()
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        rect = QRectF(self.location.x-self.r, self.location.y-self.r, self.d, self.d)
        qp.drawEllipse(rect)     
 
        self.showInfo(qp)
 
        qp.end()
 
    def showInfo(self, qp):
        pos = 'Position\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.location.x, self.location.y)
        mousepos = 'Mouse\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.pt.x, self.pt.y)
        velocity = 'Velocity\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.velocity.x, self.velocity.y)
        accel = 'Accel\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.acceleration.x, self.acceleration.y)
        text = pos+'\n'+mousepos+'\n'+velocity+'\n'+accel
 
        qp.drawText(self.rect(), Qt.AlignLeft|Qt.AlignTop|Qt.TextExpandTabs, text)
 
    def threadFunc(self):
        while self.bThread:
 
            # ���� ��ġ���� ���콺�� ���ϴ� ���͸� ���
            self.acceleration = self.pt - self.location
            # ���ͱ��̸� ����ȭ(�ʹ����� ���ӵ�����)
            self.acceleration.normalize()
            # ������ ������ ���̷� ���� (���Ͱ�)
            self.acceleration *= vector(0.5, 0.5)
 
            #���ӵ��� �ӵ��� ����
            self.velocity += self.acceleration
            #�ִ� �ӵ� ����
            self.velocity.setLimit(5)
            #�ӵ��� ��ġ�� ����
            self.location += self.velocity            
 
            #ȭ�鳡�� ������ ƨ���
            if self.location.x+self.r > self.width() or self.location.x-self.r < 0:
                self.velocity.x *= -1
            if self.location.y+self.r > self.height() or self.location.y-self.r < 0:
                self.velocity.y *= -1
 
            self.update()
 
            time.sleep(0.01)
             
    def closeEvent(self, e):
        self.bThread = False
          
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())