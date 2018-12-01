import sys
import os
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join = os.path.join(mypath, "..\\Temp")
join_path = os.path.join(mypath, "..\\Modules\\NhapKhauGiam.py")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join)  
from config import *

number = SoKhauGiam
value = value

if number != 0:
	file_object = open(join_path, mode='w',encoding="utf-8")
	file_object.write("""
import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\\Temp\\\ThongSoKhauGiam.py")

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

	if value == 0:
		for i in range(1, number+1):
			file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu %s      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt%s = QLineEdit()
		scrollLayout.addWidget(self.kt%s)
		scrollLayout.addWidget(QLabel('Giới hạn trên (mm):'))
		self.ght%s = QLineEdit()
		scrollLayout.addWidget(self.ght%s)
		scrollLayout.addWidget(QLabel('Giới hạn dưới (mm):'))
		self.ghd%s = QLineEdit()
		scrollLayout.addWidget(self.ghd%s)
		""" %(i,i,i,i,i,i,i))
	elif value == 1:
		for i in range(1, number+1):
			file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu %s      ________________________'))
		scrollLayout.addWidget(QLabel('Kích thước danh nghĩa (mm):'))
		self.kt%s = QLineEdit()
		scrollLayout.addWidget(self.kt%s)
		scrollLayout.addWidget(QLabel('Giới hạn trên (mm):'))
		self.ght%s = QLineEdit()
		scrollLayout.addWidget(self.ght%s)
		scrollLayout.addWidget(QLabel('Giới hạn dưới (mm):'))
		self.ghd%s = QLineEdit()
		scrollLayout.addWidget(self.ghd%s)
		scrollLayout.addWidget(QLabel('Hệ số k:'))
		self.k%s = QLineEdit()
		scrollLayout.addWidget(self.k%s)
		scrollLayout.addWidget(QLabel('Hệ số alpha:'))
		self.a%s = QLineEdit()
		scrollLayout.addWidget(self.a%s)
		""" %(i,i,i,i,i,i,i,i,i,i,i))
		file_object2.write("""
		scrollLayout.addWidget(QLabel('_____________________     Khâu tổng    ______________________'))		
		scrollLayout.addWidget(QLabel('Hệ số k:'))
		self.ktong = QLineEdit()
		scrollLayout.addWidget(self.ktong)
		scrollLayout.addWidget(QLabel('Hệ số alpha:'))
		self.atong = QLineEdit()
		scrollLayout.addWidget(self.atong)
		""")
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

""")
	file_object3.close()
	file_object4 = open(join_path, mode='a',encoding="utf-8")
	if value == 0:
		for j in range(1, number+1):
			file_object4.write("""
		a = float(self.kt%s.text())
		b = float(self.ght%s.text())
		c = float(self.ghd%s.text())
		lst.append([a, b-c, b, c, (b+c)/2, 1 , 0])
		Total_Dung_Sai += (b-c) 
		Total_Lim_medium += (b+c)/2
		Total_size += a
			""" %(j,j,j))
	elif value == 1:
		for j in range(1, number+1):
			file_object4.write("""
		a = float(self.kt%s.text())
		b = float(self.ght%s.text())
		c = float(self.ghd%s.text())
		d = float(self.k%s.text())
		e = float(self.a%s.text())
		lst.append([a, b-c, b, c, (b+c)/2, d, e])
		Total_Dung_Sai += (b-c) 
		Total_Lim_medium += (b+c)/2
		Total_size += a
			""" %(j,j,j,j,j))
		file_object4.write("""
		file_objectTong = open(join_path, mode='a')
		file_objectTong.write('ktong = ' + '\"' + self.ktong.text() +'\"\\n')
		file_objectTong.write('atong = ' + '\"' + self.atong.text() +'\"\\n')
		file_objectTong.close()

	""")

	file_object4.close()



	file_object5 = open(join_path, mode='a',encoding="utf-8")
	file_object5.write("""
		file_object_lst = open(join_path, mode='a')
		lst2.extend([Total_size, Total_Dung_Sai, Total_Lim_medium])
		file_object_lst.write("tup_in_creScript2 = (%s,%s)" %(lst,lst2))	
		file_object_lst.close()
		self.close()

app = QApplication(sys.argv)
a_windows = Window()
sys.exit(app.exec_())
	""")
	file_object5.close()
	call(["python", join_path])

else :
	file_object_error = open(join_path, mode='w',encoding="utf-8")
	file_object_error.write("""
import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\\Temp\\\ThongSoKhauGiam.py")

file_object_error = open(join_path, mode='a')
file_object_error.write("tup_in_creScript2 = ([], [0, 0, 0])")	
file_object_error.close()
""")
	file_object_error.close()
	call(["python", join_path])
