
import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp\\ThongSoKhauGiam.py")

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

##############################################  
		scrollLayout.addWidget(QLabel(''))        
		scroll.setWidget(scrollContent)
		self.button = (QPushButton("Nhập"))
		box.addWidget(self.button)
		self.setGeometry(200,50,400,600)
		self.setMaximumSize(400, 600)
		self.setWindowTitle("Nhập thông số các khâu giảm")
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

		file_object_lst = open(join_path, mode='a')
		lst2.extend([Total_size, Total_Dung_Sai, Total_Lim_medium])
		file_object_lst.write("tup_in_creScript2 = (%s,%s)" %(lst,lst2))	
		file_object_lst.close()
		self.close()

app = QApplication(sys.argv)
a_windows = Window()
sys.exit(app.exec_())
	