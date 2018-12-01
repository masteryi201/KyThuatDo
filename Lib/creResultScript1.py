import sys
import os
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join = os.path.join(mypath, "..\\Temp")
join_path = os.path.join(mypath, "..\\Modules\\Result1.py")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join)  
from config import *

number = SoKhauTang
value = value

file_object = open(join_path, mode='w',encoding="utf-8")
file_object.write("""
import sys
from PyQt5.QtWidgets import *


class MyTable(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)

		self.show()

class Sheet(QMainWindow):
	def __init__(self):
		super().__init__()

		""")

file_object.close()
file_object2 = open(join_path, mode='a',encoding="utf-8")
file_object2.write("""
		self.form_widget = MyTable(1,4)
		self.setCentralWidget(self.form_widget)
		col_headers = ["A", "T", "ES", "EI"]
		row_headers = ["Khâu khép kín"]
		self.form_widget.setHorizontalHeaderLabels(col_headers)
		self.form_widget.setVerticalHeaderLabels(row_headers)
		A = QTableWidgetItem("%0.2f")
		self.form_widget.setItem(0,0, A)
		T = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,1, T)
		ES = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,2, ES)
		EI = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,3, EI)
		""" %(A_tong,T_tong,ES_tong,EI_tong))
file_object2.write("""

		self.setGeometry(100,100,600,200)
		self.setWindowTitle("Kết Quả")

		self.show()
app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())

	""")
file_object2.close()
call(["python", join_path])
