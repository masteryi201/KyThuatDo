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
		self.line = QLineEdit()
		self.line1 = QLineEdit()
		self.b = QPushButton("OK")
		h_box  = QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.label)
		h_box.addWidget(self.line)
		h_box1  = QHBoxLayout()
		h_box1.addStretch()
		h_box1.addWidget(self.label1)
		h_box1.addWidget(self.line1)
		v_box = QVBoxLayout()
		v_box.addLayout(h_box)
		v_box.addLayout(h_box1)
		v_box.addWidget(self.b)
		self.setLayout(v_box)
		self.setWindowTitle("")
		self.setMaximumSize(200,100)
		qtRectangle = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())
		self.b.clicked.connect(self.bnt_clear)
		self.show()


	def bnt_clear(self):
		if self.line.text() == "0" and self.line1.text() == "0":
			QMessageBox.question(self, 'Message', "Are you kidding me?",QMessageBox.No)
		elif self.line.text() == "" and self.line1.text() == "":
			QMessageBox.question(self, 'Message', "Are you kidding me?",QMessageBox.No)
		else :
			file_object = open(join_path, mode='a',encoding="utf-8")
			file_object.write("""
SoKhauTang = int('%s')
SoKhauGiam = int('%s')""" %(self.line.text(),self.line1.text()))
			file_object.close()
		self.close()

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
