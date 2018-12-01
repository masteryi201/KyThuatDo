
import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp\\ThongSoKhauTang.py")

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

		scrollLayout.addWidget(QLabel('_____________________     Khâu 1      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt1 = QLineEdit()
		scrollLayout.addWidget(self.kt1)
		scrollLayout.addWidget(QLabel('Giới hạn trên (mm):'))
		self.ght1 = QLineEdit()
		scrollLayout.addWidget(self.ght1)
		scrollLayout.addWidget(QLabel('Giới hạn dưới (mm):'))
		self.ghd1 = QLineEdit()
		scrollLayout.addWidget(self.ghd1)
		
		scrollLayout.addWidget(QLabel('_____________________     Khâu 2      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt2 = QLineEdit()
		scrollLayout.addWidget(self.kt2)
		scrollLayout.addWidget(QLabel('Giới hạn trên (mm):'))
		self.ght2 = QLineEdit()
		scrollLayout.addWidget(self.ght2)
		scrollLayout.addWidget(QLabel('Giới hạn dưới (mm):'))
		self.ghd2 = QLineEdit()
		scrollLayout.addWidget(self.ghd2)
		
##############################################     
		scrollLayout.addWidget(QLabel(''))     
		scroll.setWidget(scrollContent)
		self.button = (QPushButton("Nhập"))
		box.addWidget(self.button)
		self.setGeometry(200,50,400,600)
		self.setMaximumSize(400, 600)
		self.setWindowTitle("Nhập thông số các khâu tăng")
		self.button.clicked.connect(self.send_value)
		self.show()

	def send_value(self):
		file_object = open(join_path, mode='w')
		file_object.close()
		lst = []
		lst2 = []
		i = 1
		Total_size = 0
		Total_Dung_Sai = 0
		Total_Lim_medium = 0


		a = float(self.kt1.text())
		b = float(self.ght1.text())
		c = float(self.ghd1.text())
		lst.append([a, b-c, b, c, (b+c)/2, 1 , 0])
		Total_Dung_Sai += (b-c) 
		Total_Lim_medium += (b+c)/2
		Total_size += a
			
		a = float(self.kt2.text())
		b = float(self.ght2.text())
		c = float(self.ghd2.text())
		lst.append([a, b-c, b, c, (b+c)/2, 1 , 0])
		Total_Dung_Sai += (b-c) 
		Total_Lim_medium += (b+c)/2
		Total_size += a
			
		file_object_lst = open(join_path, mode='a')
		lst2.extend([Total_size, Total_Dung_Sai, Total_Lim_medium])
		file_object_lst.write("tup_in_creScript1 = (%s,%s)" %(lst,lst2))	
		file_object_lst.close()
		self.close()

app = QApplication(sys.argv)
a_windows = Window()
sys.exit(app.exec_())
	