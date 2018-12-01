import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp\\config.py")

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()
	def init_ui(self):
		self.label = QLabel("Nhập khâu số tăng:")
		self.label1 = QLabel("Nhập khâu số giảm:")
		self.checkbox1  = QCheckBox("Chọn khâu tăng làm khâu bồi thường")
		self.checkbox2  = QCheckBox("Chọn khâu giảm làm khâu bồi thường")		
		self.line = QLineEdit()
		self.line1 = QLineEdit()
		self.b = QPushButton("OK")
		h_box1  = QHBoxLayout()
		h_box1.addStretch()
		h_box1.addWidget(self.label)
		h_box1.addWidget(self.line)
		h_box2  = QHBoxLayout()
		h_box2.addStretch()
		h_box2.addWidget(self.label1)
		h_box2.addWidget(self.line1)
		h_box3  = QHBoxLayout()
		h_box3.addStretch()
		h_box3.addWidget(self.checkbox1)
		h_box4  = QHBoxLayout()
		h_box4.addStretch()
		h_box4.addWidget(self.checkbox2)
		v_box = QVBoxLayout()
		v_box.addLayout(h_box1)
		v_box.addLayout(h_box2)
		v_box.addLayout(h_box3)
		v_box.addLayout(h_box4)		
		v_box.addWidget(self.b)
		self.setLayout(v_box)
		self.setWindowTitle("")
		self.setMaximumSize(200,100)

		self.b.clicked.connect(self.bnt_clear)
		self.checkbox1.clicked.connect(self.check_singer)
		self.checkbox2.clicked.connect(self.check_singer)

		self.show()


	def bnt_clear(self):
		if self.line.text() == "0" and self.line1.text() == "0":
			QMessageBox.question(self, 'Message', "Are you kidding me?",QMessageBox.No)
			
		else :
			file_object = open(join_path, mode='a',encoding="utf-8")
			file_object.write("""
SoKhauTang = int('%s')
SoKhauGiam = int('%s')
			""" %(self.line.text(),self.line1.text()))

		self.close()
	def check_singer(self):
		if self.checkbox1.isChecked() == True:
			check_singer = open(join_path, mode='a')
			check_singer.write('\ncheck_true = 0')
			check_singer.close()
		if self.checkbox2.isChecked() == True:
			check_singer = open(join_path, mode='a')
			check_singer.write('\ncheck_true = 1')
			check_singer.close()
app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())