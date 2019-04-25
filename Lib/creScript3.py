import sys
import os
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join = os.path.join(mypath, "..\\Temp")
join_path = os.path.join(mypath, "..\\Modules\\ThietKe_NhapKhauTang.py")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join)  
from config import *

number = SoKhauTang
value = value

file_object = open(join_path, mode='w',encoding="utf-8")
file_object.write("""
import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
from subprocess import call

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\\Temp\\\ThietKe_ThongSoKhauTang.py")
join_path_config = os.path.join(mypath, "..\\\Temp\\\config.py")
path_creScript4 = os.path.join(mypath, "..\\Lib\\creScript4.py")

file_object = open(join_path, mode='w')
file_object.close()
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
""")

file_object.close()
file_object2 = open(join_path, mode='a',encoding="utf-8")
if check_true == 0:
	if value == 0:
		for i in range(1, number+1):
			file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu %s      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt%s = QLineEdit()
		scrollLayout.addWidget(self.kt%s)
		self.ChonKhauBoiThuong%s = QCheckBox("Chọn khâu này làm khâu bồi thường")
		scrollLayout.addWidget(self.ChonKhauBoiThuong%s)
			""" %(i,i,i,i,i))
	elif value == 1:
		for i in range(1, number+1):
			file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu %s      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt%s = QLineEdit()
		scrollLayout.addWidget(self.kt%s)
		scrollLayout.addWidget(QLabel('Hệ số k:'))
		self.k%s = QLineEdit()
		scrollLayout.addWidget(self.k%s)
		scrollLayout.addWidget(QLabel('Hệ số alpha:'))
		self.a%s = QLineEdit()
		scrollLayout.addWidget(self.a%s)
		self.ChonKhauBoiThuong%s = QCheckBox("Chọn khâu này làm khâu bồi thường")
		scrollLayout.addWidget(self.ChonKhauBoiThuong%s)
			""" %(i,i,i,i,i,i,i,i,i))
elif check_true == 1:
	if value == 0:
		for i in range(1, number+1):
				file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu %s      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt%s = QLineEdit()
		scrollLayout.addWidget(self.kt%s)
		""" %(i,i,i))
	elif value == 1:
		for i in range(1, number+1):
			file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu %s      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt%s = QLineEdit()
		scrollLayout.addWidget(self.kt%s)
		scrollLayout.addWidget(QLabel('Hệ số k:'))
		self.k%s = QLineEdit()
		scrollLayout.addWidget(self.k%s)
		scrollLayout.addWidget(QLabel('Hệ số alpha:'))
		self.a%s = QLineEdit()
		scrollLayout.addWidget(self.a%s)
		""" %(i,i,i,i,i,i,i))
file_object2.close()
file_object3 = open(join_path, mode='a',encoding="utf-8")
file_object3.write("""
##############################################    
		scrollLayout.addWidget(QLabel(''))
		scroll.setWidget(scrollContent)
		self.button = (QPushButton("Nhập"))
		box.addWidget(self.button)
		self.setGeometry(200,50,400,600)
		self.setMaximumSize(400, 600)
		self.setWindowTitle("Nhập thông số các khâu tăng")
		self.button.clicked.connect(self.send_value)
""")
file_object3.close()
file_object5 = open(join_path, mode='a',encoding="utf-8")
file_object5.write("""
		self.show()

	def send_value(self):
		lst = []
	""")
file_object5.close()

file_object6 = open(join_path, mode='a',encoding="utf-8")
if value == 0:
	for i in range(1, number+1):
		file_object6.write("""
		a = float(self.kt%s.text())
		lst.extend([a])
		""" %(i))
elif value == 1:
	for i in range(1, number+1):
		file_object6.write("""
		a = float(self.kt%s.text())
		b = float(self.k%s.text())
		c = float(self.a%s.text())
		lst.append([a, b, c])
		""" %(i, i, i))
file_object6.close()
file_object7 = open(join_path, mode='a',encoding="utf-8")
file_object7.write("""
		file_object_lst = open(join_path, mode='a')
		file_object_lst.write('tup_in_creScript3 = %s\\n' %(lst))	
		file_object_lst.close()
	""")
file_object7.close()
file_object9 = open(join_path, mode='a',encoding="utf-8")
if check_true == 0 :
	for j in range(1, number+1):
		file_object9.write("""
		if self.ChonKhauBoiThuong%s.isChecked() == True:
			value_checkbox = open(join_path, mode='a')
			value_checkbox.write('KhauBoiThuongTang = %s\\n')
			value_checkbox.close()
			""" %(j,j))
elif check_true == 1 :
		file_object9.write("""
		pass""")	
file_object9.close()
file_object10 = open(join_path, mode='a',encoding="utf-8")
file_object10.write("""
		self.close()
		call(["python", path_creScript4])

app = QApplication(sys.argv)
a_windows = Window()
sys.exit(app.exec_())
	""")
file_object10.close()
if SoKhauTang != 0:
	call(["python", join_path])
