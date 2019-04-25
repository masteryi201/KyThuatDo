import sys
import os
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join = os.path.join(mypath, "..\\Temp")
join_path = os.path.join(mypath, "..\\Modules\\Warning_Resend.py")
join_path_Resend = os.path.join(mypath, "..\\Modules\\ThietKe_TinhToanKiemTra.py")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join)  
from config import *

number = SoKhauTang
number1 = SoKhauGiam
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
mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
join_path_tang = os.path.join(mypath, "..\\\Temp\\\ThietKe_ThongSoKhauTang.py")
join_path_giam = os.path.join(mypath, "..\\\Temp\\\ThietKe_ThongSoKhauGiam.py")
sys.path.append(join_path)  
from config import *

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.backgroud()
		qtRectangle = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())




	def backgroud(self):

		box = QVBoxLayout(self)
		scroll = QScrollArea(self)
		box.addWidget(scroll)
		scroll.setWidgetResizable(True)
		scrollContent = QWidget(scroll)
		scrollLayout = QVBoxLayout(scrollContent)
		scrollContent.setLayout(scrollLayout)
		scrollLayout.addWidget(QLabel('Vì dung sai đã tính âm nên hãy chọn khâu khác để làm khâu bồi thường :'))

##############################################
""")

file_object.close()
file_object2 = open(join_path, mode='a',encoding="utf-8")
if check_true == 0:
		file_object2.write("""
		scrollLayout.addWidget(QLabel('Khâu bồi thường tăng :'))
			""")
		for i in range(1, number):
			file_object2.write("""
		kt = str(ktt%s)
		self.ChonKhauBoiThuong%s = QCheckBox('Chọn khâu tăng có A = ' + kt + ' làm khâu bồi thường.')
		scrollLayout.addWidget(self.ChonKhauBoiThuong%s)
			""" %(i-1,i,i))
		file_object2.write("""
		scrollLayout.addWidget(QLabel(''))
		scrollLayout.addWidget(QLabel(''))
		scrollLayout.addWidget(QLabel(''))
			""")
elif check_true == 1:
		file_object2.write("""
		scrollLayout.addWidget(QLabel('Khâu bồi thường giảm :'))
			""")
		for i in range(1, number1):
			file_object2.write("""
		kd = str(ktd%s)
		self.ChonKhauBoiThuong%s = QCheckBox('Chọn khâu giảm có A = ' + kd + ' làm khâu bồi thường.')
		scrollLayout.addWidget(self.ChonKhauBoiThuong%s)
			""" %(i-1,i,i))
		file_object2.write("""
		scrollLayout.addWidget(QLabel(''))
		scrollLayout.addWidget(QLabel(''))
		scrollLayout.addWidget(QLabel(''))

			""")
file_object2.close()
file_object3 = open(join_path, mode='a',encoding="utf-8")
file_object3.write("""
##############################################    
		scrollLayout.addWidget(QLabel(''))
		scroll.setWidget(scrollContent)
		self.button = (QPushButton("Chọn"))
		box.addWidget(self.button)
		self.setGeometry(200,50,400,600)
		self.setMaximumSize(400, 600)
		self.setWindowTitle("Chọn lại khâu bồi thường")
		self.button.clicked.connect(self.send_value)
""")
file_object3.close()
if check_true == 0:
	file_object4 = open(join_path, mode='a',encoding="utf-8")
	for j in range(1, number+1):
		file_object4.write("""
		self.ChonKhauBoiThuong%s.clicked.connect(self.send_value)
		""" %j)
	file_object4.close()	
file_object5 = open(join_path, mode='a',encoding="utf-8")
file_object5.write("""
		self.show()

	def send_value(self):

	""")
file_object5.close()

file_object9 = open(join_path, mode='a',encoding="utf-8")
if check_true == 0 :
	for j in range(1, number):
		file_object9.write("""

		value_checkbox = open(join_path_tang, mode='a')
		if self.ChonKhauBoiThuong%s.isChecked() == True:
			KhauBoiThuongTang%s = %s
			if  KhauBoiThuongGiam%s < Vitri_khauboithuong:
				value_checkbox.write('\\nKhauBoiThuongTang = %s')
			elif KhauBoiThuongGiam%s > Vitri_khauboithuong:
				value_checkbox.write('\\nKhauBoiThuongTang = %s')
			""" %(j,j,j,j,j,j,j+1))
elif check_true == 1 :
	for j in range(1, number1):
		file_object9.write("""

		value_checkbox = open(join_path_giam, mode='a')
		if self.ChonKhauBoiThuong%s.isChecked() == True:
			KhauBoiThuongGiam%s = %s
			if  KhauBoiThuongGiam%s < Vitri_khauboithuong:
				value_checkbox.write('\\nKhauBoiThuongGiam = %s')
			elif KhauBoiThuongGiam%s > Vitri_khauboithuong:
				value_checkbox.write('\\nKhauBoiThuongGiam = %s')

			""" %(j,j,j,j,j,j,j+1))
file_object9.close()
file_object10 = open(join_path, mode='a',encoding="utf-8")
file_object10.write("""
		value_checkbox.close()

		self.close()
app = QApplication(sys.argv)
a_windows = Window()
sys.exit(app.exec_())

	""")
file_object10.close()

call(["python", join_path])
call(["python", join_path_Resend])
