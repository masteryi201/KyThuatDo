
import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
from subprocess import call

mypath = Path().absolute()
join = os.path.join(mypath, "..\\Temp")
join_path = os.path.join(mypath, "..\\Temp\\ThongSoKhauTang.py")
path_ThietKe_inputScript = os.path.join(mypath, "ThietKe_inputScript.py")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join)  
from config import *

value = value
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.backgroud()




	def backgroud(self):

		box = QVBoxLayout(self)
		scroll = QScrollArea(self)
		box.addWidget(scroll)
		scroll.setWidgetResizable(True)
		scrollContent = QWidget(scroll)
		scrollLayout = QVBoxLayout(scrollContent)
		scrollContent.setLayout(scrollLayout)

##############################################
	# nhập các  thông số khâu tổng

		scrollLayout.addWidget(QLabel('____________________     Khâu khép kín      _____________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa của khâu khép kín (mm)::'))
		self.kt_tong = QLineEdit()
		scrollLayout.addWidget(self.kt_tong)
		scrollLayout.addWidget(QLabel('Giới hạn trên của khâu khép kín (mm):'))
		self.ght_tong = QLineEdit()
		scrollLayout.addWidget(self.ght_tong)
		scrollLayout.addWidget(QLabel('Giới hạn dưới của khâu khép kín (mm):'))
		self.ghd_tong = QLineEdit()
		scrollLayout.addWidget(self.ghd_tong)
		if value == 1 :
			scrollLayout.addWidget(QLabel('Hệ số k của khâu khép kín:'))
			self.k_tong = QLineEdit()
			scrollLayout.addWidget(self.k_tong)
			scrollLayout.addWidget(QLabel('Hệ số alpha của khâu khép kín:'))
			self.alpha_tong = QLineEdit()
			scrollLayout.addWidget(self.alpha_tong)
		
		scrollLayout.addWidget(QLabel(''))
		scrollLayout.addWidget(QLabel(''))
##############################################          
		scroll.setWidget(scrollContent)
		self.button = (QPushButton("Nhập"))
		box.addWidget(self.button)
		self.setGeometry(200,50,400,600)
		self.setMaximumSize(400, 600)
		self.setWindowTitle("Nhập thông số các khâu tăng")
		self.button.clicked.connect(self.send_value)
		self.show()

	def send_value(self):
		lst = []
		a = float(self.kt_tong.text())
		b = float(self.ght_tong.text())
		c = float(self.ghd_tong.text())
		DungSai_tong = b - c
		if value == 0 :
			lst.extend([a, DungSai_tong, b, c])
			file_object_lst = open(path_config, mode='a')
			file_object_lst.write("\ntup_in_ThietKe_NhapKhauTong = %s" %(lst))	
			file_object_lst.close()
		elif value == 1 :
			d = float(self.k_tong.text())
			e =float(self.alpha_tong.text())
			lst.extend([a, DungSai_tong, b, c, d, e])
			file_object_lst = open(path_config, mode='a')
			file_object_lst.write("\ntup_in_ThietKe_NhapKhauTong = %s" %(lst))	
			file_object_lst.close()
		self.close()
		call(["python", path_ThietKe_inputScript])

app = QApplication(sys.argv)
a_windows = Window()
sys.exit(app.exec_())
	