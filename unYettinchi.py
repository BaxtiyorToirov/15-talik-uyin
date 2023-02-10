from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QMessageBox
import random
from PyQt5.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count=0
        self.a=0
        self.c=0  
        self.d=0
        self.e=0
        self.gr_lay=QGridLayout()
        self.v_lay=QVBoxLayout()
        self.h_lay=QHBoxLayout()
        self.setFixedSize(410,550)
        self.setStyleSheet("background-color:yellow")
        self.setWindowTitle("Uyin")
        self.lst=[]

        self.btn1=QPushButton("1")
        self.btn2=QPushButton("2")
        self.btn3=QPushButton("3")
        self.btn4=QPushButton("4")
        self.btn5=QPushButton("5")
        self.btn6=QPushButton("6")
        self.btn7=QPushButton("7")
        self.btn8=QPushButton("8")
        self.btn9=QPushButton("9")
        self.btn10=QPushButton("10")
        self.btn11=QPushButton("11")
        self.btn12=QPushButton("12")
        self.btn13=QPushButton("13")
        self.btn14=QPushButton("14")
        self.btn15=QPushButton("15")
        self.btn16=QPushButton("")

        self.lst=[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]
        k=0
        for i in range(4):
            for j in range(4):
                self.gr_lay.addWidget(self.lst[k],i,j)
                self.lst[k].setFixedSize(95,120)
                self.lst[k].setStyleSheet("background-color:black;color:white;border:1px solid black")
                self.lst[k].setFont(QFont("Times",15))
                k+=1
       
        self.close=QPushButton("close")
        self.close.setStyleSheet("background-color:black;color:white")
        self.close.setFont(QFont("Times",12))
        self.close.clicked.connect(self.son)
        self.start=QPushButton("start")
        self.start.setStyleSheet("background-color:black;color:white")
        self.start.setFont(QFont("Times",12))
        self.start.clicked.connect(self.start2)


        self.h_lay.addWidget(self.close)
        self.h_lay.addWidget(self.start) 

        self.v_lay.addLayout(self.gr_lay)
        self.v_lay.addLayout(self.h_lay)

        self.setLayout(self.v_lay)
    def son(self):
        self.exit
        
    b=0
    def start2(self):
        random.shuffle(self.lst)
        for i in self.lst:
            self.gr_lay.addWidget(i)
            if i.text()=="":
                self.count=self.lst.index(i)
        self.setLayout(self.gr_lay)
        self.hisob()
    def boshqa(self):
        if self.lst[0].text()==1 and self.lst[1].text()==2 and self.lst[2].text()==3 and self.lst[3].text()==4 and self.lst[4].text()==5 and self.lst[5].text()==6 and self.lst[6].text()==7 and self.lst[7].text()==8 and self.lst[8].text()==9 and self.lst[9].text()==10 and self.lst[10].text()==11 and self.lst[11].text()==12 and self.lst[12].text()==13 and self.lst[13].text()==14 and self.lst[14].text()==15 and self.lst[15].text()==16 :
            self.msg=QMessageBox()
            self.msg.setIcon(QMessageBox.information)
            self.setStyleSheet("background-color:yellow;color:white")
            self.msg.setText("You winner !!!!!!")
        else:
            for i in self.lst:
                self.gr_lay.addWidget(i)
                if i.text()=="":
                    self.count=self.lst.index(i)
        self.setLayout(self.gr_lay)
        self.hisob() 
    def hisob(self):
        # print(self.count)
        if self.count==0:
            self.a=self.lst[1]
            self.c=self.lst[4]
            self.a.clicked.connect(self.bir)
            self.c.clicked.connect(self.ikki)    
        if self.count==1:
            self.a=self.lst[0]
            self.c=self.lst[2]
            self.d=self.lst[5]
            self.a.clicked.connect(self.uch)
            self.c.clicked.connect(self.turt)
            self.d.clicked.connect(self.besh)  
        if self.count==2:
            self.a=self.lst[1]
            self.c=self.lst[3]
            self.d=self.lst[6]
            self.a.clicked.connect(self.olti)
            self.c.clicked.connect(self.yetti)
            self.d.clicked.connect(self.sakkiz)
        if self.count==3:
            self.a=self.lst[2]
            self.c=self.lst[7]
            self.a.clicked.connect(self.tuq)
            self.c.clicked.connect(self.un)
           
        if self.count==4:
            self.a=self.lst[0]
            self.c=self.lst[5]
            self.d=self.lst[8]
            self.a.clicked.connect(self.un1)
            self.c.clicked.connect(self.un2)
            self.d.clicked.connect(self.un3)
        if self.count==5:
            self.a=self.lst[1]
            self.c=self.lst[4]
            self.d=self.lst[6]
            self.e=self.lst[9]
            self.a.clicked.connect(self.un4)
            self.c.clicked.connect(self.un5)
            self.d.clicked.connect(self.un6)
            self.e.clicked.connect(self.un7)

        if self.count==6:
            self.a=self.lst[2]
            self.c=self.lst[5]
            self.d=self.lst[7]
            self.e=self.lst[10]
            self.a.clicked.connect(self.un8)
            self.c.clicked.connect(self.un9)
            self.d.clicked.connect(self.un10)
            self.e.clicked.connect(self.un11)
        if self.count==7:
            self.a=self.lst[3]
            self.c=self.lst[6]
            self.d=self.lst[11]
            self.a.clicked.connect(self.un12)
            self.c.clicked.connect(self.un13)
            self.d.clicked.connect(self.un14)
        if self.count==8:
            self.a=self.lst[4]
            self.c=self.lst[9]
            self.d=self.lst[12]
            self.a.clicked.connect(self.un15)
            self.c.clicked.connect(self.un16)
            self.d.clicked.connect(self.un17)
        if self.count==9:
            self.a=self.lst[5]
            self.c=self.lst[8]
            self.d=self.lst[10]
            self.e=self.lst[13]
            self.a.clicked.connect(self.un18)
            self.c.clicked.connect(self.un19)
            self.d.clicked.connect(self.un20)
            self.e.clicked.connect(self.un21)
        if self.count==10:
            self.a=self.lst[6]
            self.c=self.lst[9]
            self.d=self.lst[11]
            self.e=self.lst[14]
            self.a.clicked.connect(self.un22)
            self.c.clicked.connect(self.un23)
            self.d.clicked.connect(self.un24)
            self.e.clicked.connect(self.un25)
        if self.count==11:
            self.a=self.lst[7]
            self.c=self.lst[10]
            self.d=self.lst[15]
            self.a.clicked.connect(self.un26)
            self.c.clicked.connect(self.un27)
            self.d.clicked.connect(self.un28)
        if self.count==12:
            self.a=self.lst[8]
            self.c=self.lst[13]
            self.a.clicked.connect(self.un29)
            self.c.clicked.connect(self.un30)
        if self.count==13:
            self.a=self.lst[9]
            self.c=self.lst[12]
            self.d=self.lst[14]
            self.a.clicked.connect(self.un31)
            self.c.clicked.connect(self.un32)
            self.d.clicked.connect(self.un33)
        if self.count==14:
            self.a=self.lst[10]
            self.c=self.lst[13]
            self.d=self.lst[15]
            self.a.clicked.connect(self.un34)
            self.c.clicked.connect(self.un35)
            self.d.clicked.connect(self.un36)
        if self.count==15:
            self.a=self.lst[11]
            self.c=self.lst[14]
            self.a.clicked.connect(self.un37)
            self.c.clicked.connect(self.un38)
        

    

    def bir(self):
        if self.lst[0].text()=="":
            self.lst[0].setText(self.a.text())
            self.lst[1].setText("")
            self.boshqa()
    def ikki(self):
        if self.lst[0].text()=="":
            self.lst[0].setText(self.c.text())
            self.lst[4].setText("")
            self.boshqa()
    def uch(self):
        if self.lst[1].text()=="":
            self.lst[1].setText(self.a.text())
            self.lst[0].setText("")
            self.boshqa()
    def turt(self):
        if self.lst[1].text()=="":
            self.lst[1].setText(self.c.text())
            self.lst[2].setText("")
            self.boshqa()
    def besh(self):
        if self.lst[1].text()=="":
            self.lst[1].setText(self.d.text())
            self.lst[5].setText("")
            self.boshqa()
    def olti(self):
        if self.lst[2].text()=="":
            self.lst[2].setText(self.a.text())
            self.lst[1].setText("")
            self.boshqa()
    def yetti(self):
        if self.lst[2].text()=="":
            self.lst[2].setText(self.c.text())
            self.lst[3].setText("")
            self.boshqa()
    def sakkiz(self):
        if self.lst[2].text()=="":
            self.lst[2].setText(self.d.text())
            self.lst[6].setText("")
            self.boshqa()
    def tuq(self):
        if self.lst[3].text()=="":
            self.lst[3].setText(self.a.text())
            self.lst[2].setText("")
            self.boshqa()
    def un(self):
        if self.lst[3].text()=="":
            self.lst[3].setText(self.c.text())
            self.lst[7].setText("")
            self.boshqa()
    def un1(self):
        if self.lst[4].text()=="":
            self.lst[4].setText(self.a.text())
            self.lst[0].setText("")
            self.boshqa()
    def un2(self):
        if self.lst[4].text()=="":
            self.lst[4].setText(self.c.text())
            self.lst[5].setText("")
            self.boshqa()
    def un3(self):
        if self.lst[4].text()=="":
            self.lst[4].setText(self.d.text())
            self.lst[8].setText("")
            self.boshqa()
    def un4(self):
        if self.lst[5].text()=="":
            self.lst[5].setText(self.a.text())
            self.lst[1].setText("")
            self.boshqa()
    def un5(self):
        if self.lst[5].text()=="":
            self.lst[5].setText(self.c.text())
            self.lst[4].setText("")
            self.boshqa()
    def un6(self):
        if self.lst[5].text()=="":
            self.lst[5].setText(self.d.text())
            self.lst[6].setText("")
            self.boshqa()
    def un7(self):
        if self.lst[5].text()=="":
            self.lst[5].setText(self.e.text())
            self.lst[9].setText("")
            self.boshqa()
    def un8(self):
        if self.lst[6].text()=="":
            self.lst[6].setText(self.a.text())
            self.lst[2].setText("")
            self.boshqa()
    def un9(self):
        if self.lst[6].text()=="":
            self.lst[6].setText(self.c.text())
            self.lst[5].setText("")
            self.boshqa()
    def un10(self):
        if self.lst[6].text()=="":
            self.lst[6].setText(self.d.text())
            self.lst[7].setText("")
            self.boshqa()
    def un11(self):
        if self.lst[6].text()=="":
            self.lst[6].setText(self.e.text())
            self.lst[10].setText("")
            self.boshqa()
    def un12(self):
        if self.lst[7].text()=="":
            self.lst[7].setText(self.a.text())
            self.lst[3].setText("")
            self.boshqa()
    def un13(self):
        if self.lst[7].text()=="":
            self.lst[7].setText(self.c.text())
            self.lst[6].setText("")
            self.boshqa()
    def un14(self):
        if self.lst[7].text()=="":
            self.lst[7].setText(self.d.text())
            self.lst[11].setText("")
            self.boshqa()
    def un15(self):
        if self.lst[8].text()=="":
            self.lst[8].setText(self.a.text())
            self.lst[4].setText("")
            self.boshqa()
    def un16(self):
        if self.lst[8].text()=="":
            self.lst[8].setText(self.c.text())
            self.lst[9].setText("")
            self.boshqa()
    def un17(self):
        if self.lst[8].text()=="":
            self.lst[8].setText(self.d.text())
            self.lst[12].setText("")
            self.boshqa()
    def un18(self):
        if self.lst[9].text()=="":
            self.lst[9].setText(self.a.text())
            self.lst[5].setText("")
            self.boshqa()
    def un19(self):
        if self.lst[9].text()=="":
            self.lst[9].setText(self.c.text())
            self.lst[8].setText("")
            self.boshqa()
    def un20(self):
        if self.lst[9].text()=="":
            self.lst[9].setText(self.d.text())
            self.lst[10].setText("")
            self.boshqa()
    def un21(self):
        if self.lst[9].text()=="":
            self.lst[9].setText(self.e.text())
            self.lst[13].setText("")
            self.boshqa()
    def un22(self):
        if self.lst[10].text()=="":
            self.lst[10].setText(self.a.text())
            self.lst[6].setText("")
            self.boshqa()
    def un23(self):
        if self.lst[10].text()=="":
            self.lst[10].setText(self.c.text())
            self.lst[9].setText("")
            self.boshqa()
    def un24(self):
        if self.lst[10].text()=="":
            self.lst[10].setText(self.d.text())
            self.lst[11].setText("")
            self.boshqa()
    def un25(self):
        if self.lst[10].text()=="":
            self.lst[10].setText(self.e.text())
            self.lst[14].setText("")
            self.boshqa()
    def un26(self):
        if self.lst[11].text()=="":
            self.lst[11].setText(self.a.text())
            self.lst[7].setText("")
            self.boshqa()
    def un27(self):
        if self.lst[11].text()=="":
            self.lst[11].setText(self.c.text())
            self.lst[10].setText("")
            self.boshqa()
    def un28(self):
        if self.lst[11].text()=="":
            self.lst[11].setText(self.d.text())
            self.lst[15].setText("")
            self.boshqa()
    def un29(self):
        if self.lst[12].text()=="":
            self.lst[12].setText(self.a.text())
            self.lst[8].setText("")
            self.boshqa()
    def un30(self):
        if self.lst[12].text()=="":
            self.lst[12].setText(self.c.text())
            self.lst[13].setText("")
            self.boshqa()
    def un31(self):
        if self.lst[13].text()=="":
            self.lst[13].setText(self.a.text())
            self.lst[9].setText("")
            self.boshqa()
    def un32(self):
        if self.lst[13].text()=="":
            self.lst[13].setText(self.c.text())
            self.lst[12].setText("")
            self.boshqa()
    def un33(self):
        if self.lst[13].text()=="":
            self.lst[13].setText(self.d.text())
            self.lst[14].setText("")
            self.boshqa()
    def un34(self):
        if self.lst[14].text()=="":
            self.lst[14].setText(self.a.text())
            self.lst[10].setText("")
            self.boshqa()
    def un35(self):
        if self.lst[14].text()=="":
            self.lst[14].setText(self.c.text())
            self.lst[13].setText("")
            self.boshqa()
    def un36(self):
        if self.lst[14].text()=="":
            self.lst[14].setText(self.d.text())
            self.lst[15].setText("")
            self.boshqa()
    def un37(self):
        if self.lst[15].text()=="":
            self.lst[15].setText(self.a.text())
            self.lst[11].setText("")
            self.boshqa()
    def un38(self):
        if self.lst[15].text()=="":
            self.lst[15].setText(self.c.text())
            self.lst[14].setText("")
            self.boshqa()

app=QApplication([])
win=Window()
win.show()
app.exec_()

    
    
    
    
    
    
    
    
    

    
    
    

    
       
        



