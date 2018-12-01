
import sys
from PyQt5.QtWidgets import *


class MyTable(QTableWidget):
	def __init__(self,r,c):
		super().__init__(r,c)

		self.show()

class Sheet(QMainWindow):
	def __init__(self):
		super().__init__()

		
		self.form_widget = MyTable(1,4)
		self.setCentralWidget(self.form_widget)
		col_headers = ["A", "T", "ES", "EI"]
		row_headers = ["Khâu khép kín"]
		self.form_widget.setHorizontalHeaderLabels(col_headers)
		self.form_widget.setVerticalHeaderLabels(row_headers)
		A = QTableWidgetItem("200.00")
		self.form_widget.setItem(0,0, A)
		T = QTableWidgetItem("0.1720")
		self.form_widget.setItem(0,1, T)
		ES = QTableWidgetItem("0.0860")
		self.form_widget.setItem(0,2, ES)
		EI = QTableWidgetItem("-0.0860")
		self.form_widget.setItem(0,3, EI)
		

		self.setGeometry(100,100,600,200)
		self.setWindowTitle("Kết Quả")

		self.show()
app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())

	