import sys
import os
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call


mypath = Path().absolute()
join_path_image = os.path.join(mypath, "..\\Image\\background.jpg")
join_path = os.path.join(mypath, "..\\Temp")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
path_inputScript = os.path.join(mypath, "inputScript.py")
path_ThietKe_inputScript = os.path.join(mypath, "ThietKe_inputScript.py")
path_NhapSoKhau = os.path.join(mypath, "NhapSoKhau.py")
path_ThietKe_TinhToanKiemTra = os.path.join(mypath, "ThietKe_TinhToanKiemTra.py")
path_ThietKe_NhapKhauTong =  os.path.join(mypath, "ThietKe_NhapKhauTong.py")
path_creScript3 = os.path.join(mypath, "..\\Lib\\creScript3.py")
path_creResultScript1 = os.path.join(mypath, "..\\Lib\\creResultScript1.py")
sys.path.append(join_path)

resize = open(path_config, mode='w',encoding="utf-8")
resize.close()

from config import *
print()
class MainWindow(QWidget):
  def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(100,100,620,500)
       oImage = QImage(join_path_image)
       sImage = oImage.scaled(QSize(1920,1080))
       self.setWindowTitle("Chương trình tính chuỗi kích thước - Kỹ thuật đo")

       self.setGeometry(0, 0, 1000, 600)
       #self.showFullScreen()		
       #self.setMinimumSize(850,600)
       #self.showMaximized()
       qtRectangle = self.frameGeometry()
       centerPoint = QDesktopWidget().availableGeometry().center()
       qtRectangle.moveCenter(centerPoint)
       self.move(qtRectangle.topLeft())                         # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
       self.setPalette(palette)

       font = QtGui.QFont()
       font.setFamily("Tahoma")
       font.setPointSize(7)
       font.setBold(True)   
       font.setWeight(65)
       font1 = QtGui.QFont()
       font1.setFamily("Tahoma")
       font1.setPointSize(60)
       font1.setBold(True)   
       font1.setWeight(80)
       fontdesign = QtGui.QFont()
       fontdesign.setFamily("Tahoma")
       fontdesign.setPointSize(18)
       fontdesign.setBold(True)   
       fontdesign.setWeight(65)
       font2 = QtGui.QFont()
       font2.setFamily("Tahoma")
       font2.setPointSize(9)
       font2.setBold(True)   
       font2.setWeight(65)    
       self.labelNone = QLabel("")
       self.labelNone1 = QLabel("")

       self.labeTitle = QLabel(" Kỹ thuật đo")
       self.labeTitle.setFont(font1)
       self.labeTitle.setStyleSheet("color: red")

       self.labelnamedesign = QLabel(self.print_screen())
       self.labelnamedesign.setFont(fontdesign)
       self.labelnamedesign.setStyleSheet("color: red")

       self.b1 = QPushButton("\n 1: Giải bài toán kiểm tra bằng phương pháp lấp lẫn hoàn toàn.  \n")
       self.b1.setStyleSheet("background-color: rgb(0,255,255)")
       self.b1.setFont(font2)
       self.b2 = QPushButton("\n 2: Giải bài toán thiết kế bằng phương pháp lấp lẫn hoàn toàn.   \n")
       self.b2.setStyleSheet("background-color: rgb(0,255,255)")
       self.b2.setFont(font2)
       self.b3 = QPushButton("\n   3: Giải bài toán kiểm tra bằng phương pháp xác suất .\n")
       self.b3.setStyleSheet("background-color: rgb(0,255,255)")
       self.b3.setFont(font2)
       self.b4 = QPushButton("\n   4: Giải bài toán thiết kế bằng phương pháp xác suất .\n")
       self.b4.setStyleSheet("background-color: rgb(0,255,255)")
       self.b4.setFont(font2)
       self.b5 = QPushButton("\n   5: Thoát chương trình .\n") 
       self.b5.setStyleSheet("background-color: rgb(0,255,255)")
       self.b5.setFont(font2)

       self.h_box_Title  = QHBoxLayout()
       self.h_box_Title.addWidget(self.labelNone)
       self.h_box_Title.addWidget(self.labeTitle)
       self.h_box_Title.addWidget(self.labelNone)

       self.h_box_namedesign  = QHBoxLayout()
       self.h_box_namedesign.addWidget(self.labelNone)
       self.h_box_namedesign.addWidget(self.labelnamedesign)
       self.h_box_namedesign.addWidget(self.labelNone)      

       self.h_box_none  = QHBoxLayout()
       self.h_box_none.addWidget(self.labelNone)

       self.h_box1  = QHBoxLayout()
       self.h_box1.addWidget(self.labelNone)
       self.h_box1.addWidget(self.b1)
       self.h_box1.addWidget(self.labelNone)

       self.h_box2  = QHBoxLayout()
       self.h_box2.addWidget(self.labelNone)
       self.h_box2.addWidget(self.b2)
       self.h_box2.addWidget(self.labelNone)

       self.h_box3  = QHBoxLayout()
       self.h_box3.addWidget(self.labelNone)
       self.h_box3.addWidget(self.b3)
       self.h_box3.addWidget(self.labelNone)

       self.h_box4  = QHBoxLayout()
       self.h_box4.addWidget(self.labelNone)
       self.h_box4.addWidget(self.b4)
       self.h_box4.addWidget(self.labelNone)

       self.h_box5  = QHBoxLayout()
       self.h_box5.addWidget(self.labelNone)
       self.h_box5.addWidget(self.b5)
       self.h_box5.addWidget(self.labelNone)

       self.h_box_none2  = QHBoxLayout()
       self.h_box_none2.addWidget(self.labelNone)

       self.v_box = QVBoxLayout()
       self.v_box.addLayout(self.h_box_Title)
       self.v_box.addLayout(self.h_box_namedesign)
       self.v_box.addLayout(self.h_box_none)
       self.v_box.addLayout(self.h_box1)
       self.v_box.addLayout(self.h_box2)
       self.v_box.addLayout(self.h_box3)
       self.v_box.addLayout(self.h_box4)
       self.v_box.addLayout(self.h_box5)
       #self.v_box.addLayout(self.h_box_none2)

       self.setLayout(self.v_box)


       self.b1.clicked.connect(self.function_check1)
       self.b2.clicked.connect(self.function_design)
       self.b3.clicked.connect(self.function_check2)
       self.b4.clicked.connect(self.function_design_probability)
       self.b5.clicked.connect(self.quit)
       
       self.show()

  def print_screen(self):
       author = "\t\t\tCoder: Nguyễn Ích Thanh Tú\n\t\t\tTester: Nguyễn Văn Nghĩa"
       return author
  def quit(self):
       self.close()
  def function_check1(self):
       file_object = open(path_config, mode='w',encoding="utf-8")
       file_object.write("value = 0")
       file_object.close()
       call(["python", path_inputScript])
       call(["python", path_NhapSoKhau])
       call(["python", path_creResultScript1])

  def function_check2(self):
       file_object = open(path_config, mode='w',encoding="utf-8")
       file_object.write("value = 1")
       file_object.close()
       call(["python", path_inputScript])
       call(["python", path_NhapSoKhau])
       call(["python", path_creResultScript1])

  def function_design(self):
       file_object = open(path_config, mode='w',encoding="utf-8")
       file_object.write("value = 0")
       file_object.close()
       call(["python", path_ThietKe_NhapKhauTong])
       call(["python", path_creScript3])
       call(["python", path_ThietKe_TinhToanKiemTra])

  def function_design_probability(self):
       file_object = open(path_config, mode='w',encoding="utf-8")
       file_object.write("value = 1")
       file_object.close()
       call(["python", path_ThietKe_NhapKhauTong])
       call(["python", path_creScript3])
       call(["python", path_ThietKe_TinhToanKiemTra])

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
