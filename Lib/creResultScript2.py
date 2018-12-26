import sys
import os
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join = os.path.join(mypath, "..\\Temp")
join_path = os.path.join(mypath, "..\\Modules\\Result2.py")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
path_ThongSoKhauTang = os.path.join(mypath, "..\\Temp\\ThietKe_ThongSoKhauTang.py")
path_ThongSoKhauGiam = os.path.join(mypath, "..\\Temp\\ThietKe_ThongSoKhauGiam.py")
sys.path.append(join)  
from config import *
from ThietKe_ThongSoKhauTang import *
from ThietKe_ThongSoKhauGiam import *

number1 = SoKhauTang
number2 = SoKhauGiam
value = value
tong = SoKhauTang + SoKhauGiam +2
symboi = "%0"
symboi1 = "%"
file_object = open(join_path, mode='w',encoding="utf-8")
if value == 0:
	if check_true == 0 :
		file_object.write("""
import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *
mypath = Path().absolute()
join = os.path.join(mypath, "..\\\Temp")
path_config = os.path.join(mypath, "..\\\Temp\\\config.py")
sys.path.append(join)  
from config import *
def list_args(number):
    lst1 = []
    cont = 1
    while cont <= number:
        kichthuoc = "A" + str(cont)
        lst1.extend([kichthuoc])

        cont += 1
    return lst1

number1 = %s
number2 = %s
lst1 = list_args(number1)
lst2 = list_args(number2)
class MyTable(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)

		self.show()

class Sheet(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(100,100,500,(number1+number2+3)*37)

		self.form_widget = MyTable(%s,4)
		self.setCentralWidget(self.form_widget)
		col_headers = ["A", "T", "ES", "EI"]
		row_headers = ["Khâu bồi thường"]
		row_headers = row_headers + ["Khâu tăng"] + lst1 + ["Khâu giảm"] + lst2
		self.form_widget.setHorizontalHeaderLabels(col_headers)
		self.form_widget.setVerticalHeaderLabels(row_headers)
		Aboithuong = QTableWidgetItem("%0.2f")
		self.form_widget.setItem(0,0, Aboithuong)
		Tboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,1, Tboithuong)
		ESboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,2, ESboithuong)
		EIboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,3, EIboithuong)
		""" %(SoKhauTang-1,SoKhauGiam,tong,kt_boithuong,ds_boithuong,es_boithuong,ei_boithuong))
	elif check_true == 1:
		file_object.write("""
import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *
mypath = Path().absolute()
join = os.path.join(mypath, "..\\\Temp")
path_config = os.path.join(mypath, "..\\\Temp\\\config.py")
sys.path.append(join)  
from config import *
def list_args(number):
    lst1 = []
    cont = 1
    while cont <= number:
        kichthuoc = "A" + str(cont)
        lst1.extend([kichthuoc])

        cont += 1
    return lst1

number1 = %s
number2 = %s
lst1 = list_args(number1)
lst2 = list_args(number2)
class MyTable(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)

		self.show()

class Sheet(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(100,100,500,(number1+number2+3)*37)

		self.form_widget = MyTable(%s,4)
		self.setCentralWidget(self.form_widget)
		col_headers = ["A", "T", "ES", "EI"]
		row_headers = ["Khâu bồi thường"]
		row_headers = row_headers + ["Khâu tăng"] + lst1 + ["Khâu giảm"] + lst2
		self.form_widget.setHorizontalHeaderLabels(col_headers)
		self.form_widget.setVerticalHeaderLabels(row_headers)
		Aboithuong = QTableWidgetItem("%0.2f")
		self.form_widget.setItem(0,0, Aboithuong)
		Tboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,1, Tboithuong)
		ESboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,2, ESboithuong)
		EIboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,3, EIboithuong)
		""" %(SoKhauTang,SoKhauGiam-1,tong,kt_boithuong,ds_boithuong,es_boithuong,ei_boithuong))
if value == 1:
	if check_true == 0 :
		file_object.write("""
import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *
mypath = Path().absolute()
join = os.path.join(mypath, "..\\\Temp")
path_config = os.path.join(mypath, "..\\\Temp\\\config.py")
sys.path.append(join)  
from config import *
def list_args(number):
    lst1 = []
    cont = 1
    while cont <= number:
        kichthuoc = "A" + str(cont)
        lst1.extend([kichthuoc])

        cont += 1
    return lst1

number1 = %s
number2 = %s
lst1 = list_args(number1)
lst2 = list_args(number2)
class MyTable(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)

		self.show()

class Sheet(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(100,100,700,(number1+number2+3)*37)


		self.form_widget = MyTable(%s,6)
		self.setCentralWidget(self.form_widget)
		col_headers = ["A", "T", "ES", "EI", "k", "alpha"]
		row_headers = ["Khâu bồi thường"]
		row_headers = row_headers + ["Khâu tăng"] + lst1 + ["Khâu giảm"] + lst2
		self.form_widget.setHorizontalHeaderLabels(col_headers)
		self.form_widget.setVerticalHeaderLabels(row_headers)
		Aboithuong = QTableWidgetItem("%0.2f")
		self.form_widget.setItem(0,0, Aboithuong)
		Tboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,1, Tboithuong)
		ESboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,2, ESboithuong)
		EIboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,3, EIboithuong)
		kboithuong = QTableWidgetItem("%0.3f")
		self.form_widget.setItem(0,4, kboithuong)
		aboithuong = QTableWidgetItem("%0.3f")
		self.form_widget.setItem(0,5, aboithuong)
		""" %(SoKhauTang-1,SoKhauGiam,tong,kt_boithuong,ds_boithuong,es_boithuong,ei_boithuong,k_boithuong,a_boithuong))
	elif check_true == 1:
		file_object.write("""
import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *
mypath = Path().absolute()
join = os.path.join(mypath, "..\\\Temp")
path_config = os.path.join(mypath, "..\\\Temp\\\config.py")
sys.path.append(join)  
from config import *
def list_args(number):
    lst1 = []
    cont = 1
    while cont <= number:
        kichthuoc = "A" + str(cont)
        lst1.extend([kichthuoc])

        cont += 1
    return lst1

number1 = %s
number2 = %s
lst1 = list_args(number1)
lst2 = list_args(number2)
class MyTable(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)

		self.show()

class Sheet(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(100,100,700,(number1+number2+3)*37)

		self.form_widget = MyTable(%s,6)
		self.setCentralWidget(self.form_widget)
		col_headers = ["A", "T", "ES", "EI", "k", "alpha"]
		row_headers = ["Khâu bồi thường"]
		row_headers = row_headers + ["Khâu tăng"] + lst1 + ["Khâu giảm"] + lst2
		self.form_widget.setHorizontalHeaderLabels(col_headers)
		self.form_widget.setVerticalHeaderLabels(row_headers)
		Aboithuong = QTableWidgetItem("%0.2f")
		self.form_widget.setItem(0,0, Aboithuong)
		Tboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,1, Tboithuong)
		ESboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,2, ESboithuong)
		EIboithuong = QTableWidgetItem("%0.4f")
		self.form_widget.setItem(0,3, EIboithuong)
		kboithuong = QTableWidgetItem("%0.3f")
		self.form_widget.setItem(0,4, kboithuong)
		aboithuong = QTableWidgetItem("%0.3f")
		self.form_widget.setItem(0,5, aboithuong)
		""" %(SoKhauTang,SoKhauGiam-1,tong,kt_boithuong,ds_boithuong,es_boithuong,ei_boithuong,k_boithuong,a_boithuong))
file_object.close()
file_object1 = open(join_path, mode='a',encoding="utf-8")
if value == 0:
	if check_true == 0 :
		for i in range(0, number1 - 1):
			file_object1.write("""
		At%s = QTableWidgetItem("%s.2f" %sktt%s)
		self.form_widget.setItem(%s,0, At%s)
		Tt%s = QTableWidgetItem("%s.2f" %sdst%s)
		self.form_widget.setItem(%s,1, Tt%s)
		ESt%s = QTableWidgetItem("%s.2f" %sest%s)
		self.form_widget.setItem(%s,2, ESt%s)
		EIt%s = QTableWidgetItem("%s.2f" %seit%s)
		self.form_widget.setItem(%s,3, EIt%s)
			""" %(i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i))

		for i in range(0, number2):
			file_object1.write("""
		Ad%s = QTableWidgetItem("%s.2f" %sktd%s)
		self.form_widget.setItem(%s,0, Ad%s)
		Td%s = QTableWidgetItem("%s.2f" %sdsd%s)
		self.form_widget.setItem(%s,1, Td%s)
		ESd%s = QTableWidgetItem("%s.2f" %sesd%s)
		self.form_widget.setItem(%s,2, ESd%s)
		EId%s = QTableWidgetItem("%s.2f" %seid%s)
		self.form_widget.setItem(%s,3, EId%s)
			""" %(i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i))
	elif check_true == 1 :
		for i in range(0, number1):
			file_object1.write("""
		At%s = QTableWidgetItem("%s.2f" %sktt%s)
		self.form_widget.setItem(%s,0, At%s)
		Tt%s = QTableWidgetItem("%s.2f" %sdst%s)
		self.form_widget.setItem(%s,1, Tt%s)
		ESt%s = QTableWidgetItem("%s.2f" %sest%s)
		self.form_widget.setItem(%s,2, ESt%s)
		EIt%s = QTableWidgetItem("%s.2f" %seit%s)
		self.form_widget.setItem(%s,3, EIt%s)
			""" %(i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i))

		for i in range(0, number2-1):
			file_object1.write("""
		Ad%s = QTableWidgetItem("%s.2f" %sktd%s)
		self.form_widget.setItem(%s,0, Ad%s)
		Td%s = QTableWidgetItem("%s.2f" %sdsd%s)
		self.form_widget.setItem(%s,1, Td%s)
		ESd%s = QTableWidgetItem("%s.2f" %sesd%s)
		self.form_widget.setItem(%s,2, ESd%s)
		EId%s = QTableWidgetItem("%s.2f" %seid%s)
		self.form_widget.setItem(%s,3, EId%s)
			""" %(i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i))
elif value == 1:
	if check_true == 0 :
		for i in range(0, number1-1):
			file_object1.write("""
		At%s = QTableWidgetItem("%s.2f" %sktt%s)
		self.form_widget.setItem(%s,0, At%s)
		Tt%s = QTableWidgetItem("%s.2f" %sdst%s)
		self.form_widget.setItem(%s,1, Tt%s)
		ESt%s = QTableWidgetItem("%s.2f" %sest%s)
		self.form_widget.setItem(%s,2, ESt%s)
		EIt%s = QTableWidgetItem("%s.2f" %seit%s)
		self.form_widget.setItem(%s,3, EIt%s)
		kt_%s = QTableWidgetItem("%s.2f" %skt%s)
		self.form_widget.setItem(%s,4, kt_%s)
		at_%s = QTableWidgetItem("%s.2f" %sat%s)
		self.form_widget.setItem(%s,5, at_%s)
			""" %(i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i))

		for i in range(0, number2):
			file_object1.write("""
		Ad%s = QTableWidgetItem("%s.2f" %sktd%s)
		self.form_widget.setItem(%s,0, Ad%s)
		Td%s = QTableWidgetItem("%s.2f" %sdsd%s)
		self.form_widget.setItem(%s,1, Td%s)
		ESd%s = QTableWidgetItem("%s.2f" %sesd%s)
		self.form_widget.setItem(%s,2, ESd%s)
		EId%s = QTableWidgetItem("%s.2f" %seid%s)
		self.form_widget.setItem(%s,3, EId%s)
		kd_%s = QTableWidgetItem("%s.2f" %skd%s)
		self.form_widget.setItem(%s,4, kd_%s)
		ad_%s = QTableWidgetItem("%s.2f" %sad%s)
		self.form_widget.setItem(%s,5, ad_%s)
			""" %(i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i,i,symboi,symboi1,i,i+number1+2,i))
	if check_true == 1 :
		for i in range(0, number1):
			file_object1.write("""
		At%s = QTableWidgetItem("%s.2f" %sktt%s)
		self.form_widget.setItem(%s,0, At%s)
		Tt%s = QTableWidgetItem("%s.2f" %sdst%s)
		self.form_widget.setItem(%s,1, Tt%s)
		ESt%s = QTableWidgetItem("%s.2f" %sest%s)
		self.form_widget.setItem(%s,2, ESt%s)
		EIt%s = QTableWidgetItem("%s.2f" %seit%s)
		self.form_widget.setItem(%s,3, EIt%s)
		kt_%s = QTableWidgetItem("%s.2f" %skt%s)
		self.form_widget.setItem(%s,4, kt_%s)
		at_%s = QTableWidgetItem("%s.2f" %sat%s)
		self.form_widget.setItem(%s,5, at_%s)
			""" %(i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i,i,symboi,symboi1,i,i+2,i))

		for i in range(0, number2-1):
			file_object1.write("""
		Ad%s = QTableWidgetItem("%s.2f" %sktd%s)
		self.form_widget.setItem(%s,0, Ad%s)
		Td%s = QTableWidgetItem("%s.2f" %sdsd%s)
		self.form_widget.setItem(%s,1, Td%s)
		ESd%s = QTableWidgetItem("%s.2f" %sesd%s)
		self.form_widget.setItem(%s,2, ESd%s)
		EId%s = QTableWidgetItem("%s.2f" %seid%s)
		self.form_widget.setItem(%s,3, EId%s)
		kd_%s = QTableWidgetItem("%s.2f" %skd%s)
		self.form_widget.setItem(%s,4, kd_%s)
		ad_%s = QTableWidgetItem("%s.2f" %sad%s)
		self.form_widget.setItem(%s,5, ad_%s)
			""" %(i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i,i,symboi,symboi1,i,i+number1+3,i))

file_object1.write("""

		self.setWindowTitle("Kết Quả")

		self.show()
app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())


	""")
file_object1.close()
call(["python", join_path])
