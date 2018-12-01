# -*- coding: utf-8 -*-
# Import
import math
import time
# Value
error = "Chương trình không có lựa chọn này"
Mess_1 = "Bạn muốn làm gì: "

# Functions
def table1 ():
	print ("""
	   .-----------------------------------------------------------------------------------------------.
          |                             Các cấp chính xác tiêu chuẩn với D<= 500 mm                        |               
          |------------------------------------------------------------------------------------------------.
          | IT 5 | IT6 | IT7 | IT8 | IT9 | IT10 | IT11 | IT12 | IT13 | IT14 | UT15 | IT16 | IT17 | IT18    |
          |------------------------------------------------------------------------------------------------.
          |                             Các công thức tính toán dung sai tiêu chuẩn                        |
          |------------------------------------------------------------------------------------------------|
          | 7.i  | 10.i| 16.i| 25.i| 40.i| 64.i | 100.i| 160.i| 250.i| 400.i| 640.i| 1000.i| 1600.i| 2500.i|
          '------------------------------------------------------------------------------------------------' 
          """) 
def table2 ():
	print ("""
         .-------------------------------------------------------------------------------------------------------.
         | khoang | Den 3 | >3  | >6   | >10  | >18  | >30  | >50  | >80  | >120  | >180  | >250 | >315  | >400  |
         | kich   |       |->6  |-> 10 | ->18 | ->30 | ->50 | ->80 | ->120| ->180 | ->250 | ->315| ->400 | ->500 |
         | thuoc  |       |     |      |      |      |      |      |      |       |       |      |       |       |
         |--------+-------+-----+------+------+------+------+------+------+-------+-------+------+-------+-------|
         | i      |0.55   | 0.73| 0.90 | 1.08 | 1.31 | 1.56 | 1.86 | 2.17 | 2.52  | 2.89  | 3.22 | 3.54  |3.89   |
         '-------------------------------------------------------------------------------------------------------'
         """)
def table3 ():
	print ("""
    --------------------------------------------------------------------------------------------------------------------------------
   |kt danh  |                                       Cấp dung sai tiêu chuẩn                                                        |
   | nghĩa   |----------------------------------------------------------------------------------------------------------------------|
   | (mm)    | IT1 | IT2 | IT3 | IT4 | IT5 | IT6 | IT7 | IT8 | IT9 | IT10 | IT11 | I12 | IT 13 | IT14 | IT15 | IT16 | IT17 | IT18   |
   |---------|----------------------------------------------------------------------------------------------------------------------|
   |         |                                         Giá trị dung sai                                                             |
   |---------|----------------------------------------------------------------------------------------------------------------------|
   |         |               micromet                                           |                milimet                            |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   | -  |3   | 0.8 | 1.2 |  2  |  3  |  4  |  6  | 10  | 14  | 25  | 40   |  60 | 0.1  | 0.14 | 0.25 |  0.4 | 0.6  |  1   |  1.4    |
   |---------|------------------------------------------------------------+-----|------+------+-------------------------------------|
   | 3  |6   | 1   | 1.5 | 2.5 | 4   | 5   | 8   | 12  | 18  | 30  | 48   | 75  | 0.12 | 0.18 | 0.3  | 0.48 | 0.75 | 1.2  | 1.8     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   | 6  |10  | 1   | 1.5 | 2.5 | 4   | 6   | 9   | 15  | 22  | 36  | 58   | 90  | 0.15 | 0.22 | 0.36 | 0.58 | 0.9  | 1.5  | 2.2     |
   |---------|-----------------------------------+------------------------------|---------------------------------------------------|
   |10  |18  | 1.2 | 2   | 3   | 5   | 8   | 11  | 18  | 27  | 43  | 70   | 110 | 0.18 | 0.27 | 0.43 | 0.7  | 1.1  | 1.8  | 2.7     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |18  |30  | 1.5 | 2.5 | 4   | 6   | 9   | 13  | 21  | 33  | 52  | 84   | 130 | 0.21 | 0.33 | 0.52 | 0.84 | 1.3  | 2.1  | 3.3     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |30  |50  | 1.5 | 2.5 | 4   | 7   | 11  | 16  | 25  | 39  | 62  |100   | 160 | 0.25 | 0.39 | 0.62 | 1    | 1.6  | 2.5  | 3.9     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |50  |80  | 2   | 3   | 5   | 8   | 13  | 19  | 30  | 46  | 74  | 120  | 190 | 0.3  | 0.46 | 0.74 | 1.2  | 1.9  | 3    | 4.6     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |80  |120 | 2.5 | 4   | 6   | 10  | 15  | 22  | 35  | 54  | 87  | 140  | 220 | 0.35 | 0.54 | 0.87 | 1.4  | 2.2  | 3.5  |5.4      |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |120 |180 | 3.5 | 5   | 8   | 12  | 18  | 25  | 40  |  63 | 100 | 160  | 250 | 0.4  | 0.63 | 1    | 1.6  | 2.5  | 4    | 6.3     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |180 |250 | 4.5 | 7   | 10  | 14  | 20  | 29  | 46  | 72  | 115 | 185  | 290 | 0.46 | 0.72 | 1.15 | 1.85 | 2.9  | 4.6  |2.7      |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |250 |315 |  6  | 8   | 12  | 16  | 23  | 32  | 52  | 81  | 130 | 210  | 320 | 0.52 | 0.81 | 1.3  | 2.1  | 3.2  | 5.2  | 8.1     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |315 |400 |  7  | 9   | 13  | 18  | 25  | 36  | 57  | 89  | 140 | 230  | 360 | 0.57 | 0.89 | 1.4  | 2.3  | 3.6  | 5.7  | 8.9     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |400 |500 |  8  | 10  | 15  | 20  | 27  | 40  | 63  | 97  | 155 | 250  | 400 | 0.63 | 0.97 | 1.55 | 2.5  | 4    | 6.3  | 9.7     |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |500 |630 |  9  | 11  | 16  | 22  | 32  | 44  | 70  | 110 | 175 | 280  | 440 | 0.7  | 1.1  | 1.75 | 2.8  | 4.4  | 7    | 11      |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |630 |800 |  10 | 13  | 18  | 25  | 36  | 50  | 80  | 125 | 200 | 320  | 500 | 0.8  | 1.25 | 2    | 3.2  | 5    | 8    | 12.5    |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |800 |1000|  11 | 15  | 21  | 28  | 40  | 56  | 90  | 140 | 230 | 360  | 560 | 0.9  | 1.4  | 2.3  | 3.6  | 5.6  | 9    | 14      |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |1000|1250|  13 | 18  | 24  | 33  | 47  | 66  | 105 | 165 | 260 | 420  | 660 | 1.05 | 1.65 | 2.6  | 4.2  | 6.6  | 10.5 | 16.5    |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |1250|1600|  15 | 21  | 29  | 39  | 55  | 78  | 125 | 195 | 310 | 500  | 780 | 1.25 | 1.95 | 3.1  | 5    | 7.8  | 12.5 | 19.5    |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |1600|2000|  18 | 25  | 35  | 46  | 65  | 92  | 150 | 230 | 370 | 600  | 920 | 1.5  | 2.3  | 3.7  | 6    | 9.2  | 15   | 23      |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |2000|2500|  22 | 30  | 41  | 55  | 78  | 110 | 175 | 280 | 440 | 700  | 1100| 1.75 | 2.8  | 4.4  | 7    | 11   | 17.5 | 28      |
   |---------|------------------------------------------------------------------|---------------------------------------------------|
   |2500|3150| 26  | 36  | 50  | 68  | 96  | 135 | 210 | 330 | 540 | 860  | 1350| 2.1  | 3.3  | 5.4  | 8.6  | 13.5 | 21   | 33      |
   '--------------------------------------------------------------------------------------------------------------------------------'
    """)
# function banner
def banner():
	print ("""
		 _   __        _____ _                 _     _____      
		| | / /       |_   _| |               | |   |  _  \\     
		| |/ / _   _    | | | |__  _   _  __ _| |_  | | | |___  
		|    \\| | | |   | | | '_ \\| | | |/ _` | __| | | | / _ \\ 
		| |\\  \\ |_| |   | | | | | | |_| | (_| | |_  | |/ / (_) |
		\\_| \\_/\\__, |   \\_/ |_| |_|\\__,_|\\__,_|\\__| |___/ \\___/ 
		        __/ |                                           
		       |___/                                            	     						                                              
			                        Coder : Nguyễn Ích Thanh Tú
			                        Tester: Nguyễn Văn Nghĩa                          

		1: Tính toán
		2: Tra bảng
		0: Thoát chương trình
	""")
######### functions tính bài toán kiểm tra #########
def function_check(args):

	# function tính các thông số khâu tăng
	def Total_SizeUp(number, parameter):
		i = 1
		Total_size = 0
		Total_Dung_Sai = 0
		Total_Lim_medium = 0
		list1 = []
		list2 = []
		while i <= number:
			Size = float(input("Kích thước danh nghĩa của khâu %s (mm):" % i))
			Limit_max = float(input("Giới hạn trên của khâu %s (mm):" % i))
			Limit_min = float(input("Giới hạn dưới của khâu %s (mm):" % i))
			if parameter == 1:
				k = float(input("Hệ số k của khâu %s (mm):" % i))
				alpha = float(input("Hệ số alpha của khâu %s (mm):" % i))
			else :
				k = 1
				alpha = 0
			Dung_Sai = Limit_max - Limit_min
			Limit_medium = (Limit_max + Limit_min) / 2
			Total_size += Size
			list1.append([Size, Dung_Sai, Limit_max, Limit_min, Limit_medium, k , alpha])
			i += 1
		list2.extend([Total_size, Total_Dung_Sai, Limit_medium])
		return list1 , list2

	# function tính các thông số khâu giảm
	def Total_SizeDown(number, parameter):
		i = 1
		Total_size = 0
		Total_Dung_Sai = 0
		Total_Lim_medium = 0
		list1 = []
		list2 = []
		while i <= number:
			Size = float(input("Kích thước danh nghĩa của khâu %s (mm):" % i))
			Limit_max = float(input("Giới hạn trên của khâu %s (mm):" % i))
			Limit_min = float(input("Giới hạn dưới của khâu %s (mm):" % i))
			if parameter == 1:
				k = float(input("Hệ số k của khâu %s (mm):" % i))
				alpha = float(input("Hệ số alpha của khâu %s (mm):" % i))
			else :
				k = 1
				alpha = 0
			Dung_Sai = Limit_max - Limit_min
			Limit_medium = (Limit_max + Limit_min) / 2
			Total_size += Size
			list1.append([Size, Dung_Sai, Limit_max, Limit_min, Limit_medium, k , alpha])
			i += 1
		list2.extend([Total_size, Total_Dung_Sai, Limit_medium])
		return list1 , list2

	# Nhập số khâu tăng và giảm
	print ("Bạn có bao nhiêu khâu tăng")
	input_args_SizeUp = int(input("   > "))
	if input_args_SizeUp != 0:
		if args == 1 :
			list_SizeUp = Total_SizeUp(input_args_SizeUp, 1)
		elif args == 0 :
			list_SizeUp = Total_SizeUp(input_args_SizeUp, 0)
	else : 
		list_SizeUp = ([[0, 0, 0, 0, 0, 1, 0]], [0, 0, 0])
	print ("Bạn có bao nhiêu khâu giảm")
	input_args_SizeDown = int(input("   > "))
	if input_args_SizeDown != 0:
		if args == 1 :
			list_SizeDown = Total_SizeDown(input_args_SizeDown, 1)
		elif args == 0:
			list_SizeDown = Total_SizeDown(input_args_SizeDown, 0)
	else :
		list_SizeDown = ([[0, 0, 0, 0, 0, 1, 0]], [0, 0, 0])
	if input_args_SizeUp == 0 and input_args_SizeDown ==0:
		print ("")
		print ("Are you kidding me?")
		print ("\n" * 3)
		time.sleep(1)
		banner()

	else :	
		if args == 1 :
			ktong = float(raw_input("Hệ số k của khâu tổng (mm):"))
			alpha_tong = float(raw_input("Hệ số alpha của khâu tổng (mm):"))
		elif args ==0 :
			ktong = 1
			alpha_tong = 0
		A_tong = list_SizeUp[-1][0] - list_SizeDown[-1][0]
		i = 1
		j = 1
		T_SizeUp = 0
		T_SizeDown = 0
		kT_SizeUp = 0
		kT_SizeDown = 0
		Em_SizeUp = 0
		Em_SizeDown = 0
		while i <= input_args_SizeUp:
			T_SizeUp += list_SizeUp[0][i-1][1]
			kT_SizeUp += math.pow(list_SizeUp[0][i-1][1]*list_SizeUp[0][i-1][5],2)
			Em_SizeUp += list_SizeUp[0][i-1][4] + 0.5*list_SizeUp[0][i-1][6]*list_SizeUp[0][i-1][1]
			i += 1
		while j <= input_args_SizeDown:
			T_SizeDown += list_SizeDown[0][j-1][1]
			kT_SizeDown += math.pow(list_SizeDown[0][j-1][1]*list_SizeDown[0][j-1][5],2)
			Em_SizeDown += list_SizeDown[0][j-1][4] + 0.5*list_SizeDown[0][j-1][6]*list_SizeDown[0][j-1][1]
			j += 1
		if args == 1 :
			T_tong = ( 1 / ktong )*(math.sqrt(kT_SizeUp + kT_SizeDown))
		elif args == 0 :
			T_tong = T_SizeUp + T_SizeDown
		Em_tong = Em_SizeUp - Em_SizeDown - 0.5*alpha_tong*T_tong
		ES_tong = Em_tong + 0.5*T_tong
		EI_tong = ES_tong - T_tong
		print ("\n" * 2)
		print (" --------------------------------")
		print ("|         | Kích thước           |")
		print ("|---------+----------------------|")
		print ("| A tổng  | %0.1f		 |" % A_tong)
		print ("|---------+----------------------|")
		print ("| T tổng  | %0.3f		 |" % T_tong)
		print ("|---------+----------------------|")
		print ("| ES tổng | %0.3f		 |" % ES_tong)
		print ("|---------+----------------------|")
		print ("| EI tổng | %0.3f		 |" % EI_tong)
		print (" -------------------------------")
		print ("\n" * 2)
		time.sleep(5)
######### functions tính bài toán thiết kế #########
# Ham lay gia tri tu list
def PutOut_keyword(stuff):
	keywords = stuff.split(' ')
	return keywords
# Ham Gia tri dung sai don vi i doi voi kich thuoc danh nghia den 500mm
def DungSai_i(number):
	if number == 0:
		DungSai_DonVi = 0
	elif number > 0 and number <= 3:
		DungSai_DonVi = 0.55
	elif number > 3 and number <= 6:
		DungSai_DonVi = 0.73
	elif number > 6 and number <= 10:
		DungSai_DonVi = 0.90
	elif number > 10 and number <= 18:
		DungSai_DonVi = 1.08
	elif number > 18 and number <= 30:
		DungSai_DonVi = 1.31
	elif number > 30 and number <= 50:
		DungSai_DonVi = 1.56
	elif number > 50 and number <= 80:
		DungSai_DonVi = 1.86
	elif number > 80 and number <= 120:
		DungSai_DonVi = 2.17
	elif number > 120 and number <= 180:
		DungSai_DonVi = 2.52
	elif number > 180 and number <= 250:
		DungSai_DonVi = 2.89
	elif number > 250 and number <= 315:
		DungSai_DonVi = 3.22
	elif number > 315 and number <= 400:
		DungSai_DonVi = 3.54
	elif number > 400 and number <= 500:
		DungSai_DonVi = 3.89
	return DungSai_DonVi

# Ham Tinh dung sai tieu chuan voi D <= 500mm
def DungSai_IT(HeSo_CCX):
	if HeSo_CCX >= 7 and HeSo_CCX < 8.5 :
		IT = 5
	elif HeSo_CCX > 8.5 and HeSo_CCX <= 13:
		IT = 6
	elif HeSo_CCX > 13 and HeSo_CCX <= 20.5:
		IT = 7
	elif HeSo_CCX > 20.5 and HeSo_CCX <= 32.5:
		IT = 8
	elif HeSo_CCX > 32.5 and HeSo_CCX <= 52:
		IT = 9
	elif HeSo_CCX > 52 and HeSo_CCX <= 82:
		IT = 10
	elif HeSo_CCX > 82 and HeSo_CCX <= 130:
		IT = 11
	elif HeSo_CCX > 130 and HeSo_CCX <= 205:
		IT = 12
	elif HeSo_CCX > 205 and HeSo_CCX <= 325:
		IT = 13
	elif HeSo_CCX > 325 and HeSo_CCX <= 520:
		IT = 14
	elif HeSo_CCX > 520 and HeSo_CCX <= 820:
		IT = 15
	elif HeSo_CCX > 820 and HeSo_CCX <= 1300:
		IT = 16
	elif HeSo_CCX > 1300 and HeSo_CCX <= 2050:
		IT = 17
	elif HeSo_CCX > 2050 and HeSo_CCX <= 2500:
		IT = 18
	else: print("Nam ngoai gia tri trong bang dung sai tieu chuan voi D <= 500mm")
	return IT
# Ham Tri so dung sai kich thuoc thang tieu chuan
def DungSai_TieuChuan(Size, ccx_IT):
	if Size > 0 and Size <= 3:
		DungSai = PutOut_keyword("0.8 1.2 2 3 4 6 10 14 25 40 60 100 140 250 400 600 1000 1400")
	elif Size > 3 and Size <= 6:
		DungSai = PutOut_keyword("1 1.5 2.5 4 5 8 12 18 30 48 75 120 180 300 480 750 1200 1800")
	elif Size > 6 and Size <= 10:
		DungSai = PutOut_keyword("1 1.5 2.5 4 6 9 15 22 36 58 90 150 220 360 580 900 1500 2200")
	elif Size > 10 and Size <= 18:
		DungSai = PutOut_keyword("1.2 2 3 5 8 11 18 27 43 70 110 180 270 430 700 1100 1800 2700")
	elif Size > 18 and Size <= 30:
		DungSai = PutOut_keyword("1.5 2.5 4 6 9 13 21 33 52 84 130 210 330 520 840 1300 2100 3300")
	elif Size > 30 and Size <= 50:
		DungSai = PutOut_keyword("1.5 2.5 4 7 11 16 25 39 62 100 160 250 390 620 1000 1600 2500 3900")
	elif Size > 50 and Size <= 80:
		DungSai = PutOut_keyword("2 3 5 8 13 19 30 46 74 120 190 300 460 740 1200 1900 3000 4600")
	elif Size > 80 and Size <= 120:
		DungSai = PutOut_keyword("2.5 4 6 10 15 22 35 54 87 140 220 350 540 870 1400 2200 3500 5400")
	elif Size > 120 and Size <= 180:
		DungSai = PutOut_keyword("3.5 5 8 12 18 25 40 63 100 160 250 400 630 1000 1600 2500 4000 6300")
	elif Size > 180 and Size <= 250:
		DungSai = PutOut_keyword("4.5 7 10 14 20 29 46 72 115 185 290 460 720 1150 1850 2900 4600 7200")
	elif Size > 250 and Size <= 315:
		DungSai = PutOut_keyword("6 8 12 16 23 32 52 81 130 210 320 520 810 1300 2100 3200 5200 8100")
	elif Size > 315 and Size <= 400:
		DungSai = PutOut_keyword("7 9 13 18 25 36 57 89 140 230 360 570 890 1400 2300 3600 5700 8900")
	elif Size > 400 and Size <= 500:
		DungSai = PutOut_keyword("8 10 15 20 27 40 63 97 155 250 400 630 970 1550 2500 4000 6300 9700")
	elif Size > 500 and Size <= 630:
		DungSai = PutOut_keyword("9 11 16 22 32 44 70 110 175 280 440 700 1100 1750 2800 4400 7000 11000")
	elif Size > 630 and Size <= 800:
		DungSai = PutOut_keyword("10 13 18 25 36 50 80 125 200 320 500 800 1250 2000 3200 5000 8000 12500")
	elif Size > 800 and Size <= 1000:
		DungSai = PutOut_keyword("11 15 21 28 40 56 90 140 230 360 560 900 1400 2300 3600 5600 9000 14000")
	elif Size > 1000 and Size <= 1250:
		DungSai = PutOut_keyword("13 18 24 33 47 66 105 165 260 420 660 1050 1650 2600 4200 6600 10500 16500")
	elif Size > 1250 and Size <= 1600:
		DungSai = PutOut_keyword("15 21 29 39 55 78 125 195 310 500 780 1250 1950 3100 5000 7800 12500 19500")
	elif Size > 1600 and Size <= 2000:
		DungSai = PutOut_keyword("18 25 35 46 65 92 150 230 370 600 920 1500 2300 3700 6000 9200 15000 23000")
	elif Size > 2000 and Size <= 2500:
		DungSai = PutOut_keyword("22 30 41 55 78 110 175 280 440 700 1100 1750 2800 4400 7000 11000 17500 28000")
	elif Size > 2500 and Size <= 3150:
		DungSai = PutOut_keyword("26 36 50 68 96 135 210 330 540 860 1350 2100 3300 5400 8600 13500 21000 33000")

	return DungSai[ccx_IT]

# Ham tra bang cho khau tang
def PutOut_SizeUp(Size, ccx_IT, k = 1, alpha = 0):
	list1 = []
	Dung_Sai = float(DungSai_TieuChuan(Size, ccx_IT -1 )) / 1000
	ES = Dung_Sai
	EI = 0
	Em = ES / 2.0
	list1.append([Size, Dung_Sai, ES, EI, Em, k, alpha])
	return list1

# Ham tra bang cho khau giam
def PutOut_SizeDown(Size, ccx_IT, k = 1, alpha = 0):
	list1 = []
	Dung_Sai = float(DungSai_TieuChuan(Size, ccx_IT -1 )) / 1000
	es = 0
	ei = -Dung_Sai
	em = ei / 2.0
	list1.append([Size, Dung_Sai, es, ei, em, k, alpha])
	return list1
def function_design():

	# function tính các thông số khâu tăng
	def Import_Total_SizeUp(number):
		i = 1
		list1 = []
		while i <= number:
			Size = float(input("Kích thước danh nghĩa của khâu %s (mm):" % i))
			list1.append(Size)
			i += 1
		return list1

	# function tính các thông số khâu giảm
	def Import_Total_SizeDown(number):
		i = 1
		list1 = []
		while i <= number:
			Size = float(input("Kích thước danh nghĩa của khâu %s (mm):" % i))
			list1.append(Size)
			i += 1
		return list1

	# nhập các  thông số khâu tổng
	Size_total = float(input("Kích thước danh nghĩa của khâu tổng (mm):"))
	Limit_max_total = float(input("Giới hạn trên của khâu tổng (mm):"))
	Limit_min_total = float(input("Giới hạn dưới của khâu tổng (mm):"))
	Dung_Sai_Total = Limit_max_total - Limit_min_total
	if Dung_Sai_Total <= 0:
		print ("Dung sai khong the nho hon 0")
		print ("\n" * 2)

	else:
		Limit_mediumTotal = (Limit_max_total + Limit_min_total) / 2
		list_SizeTotal = [Size_total, Dung_Sai_Total, Limit_max_total, Limit_min_total]
		# Nhập số khâu tăng và giảm
		print ("Bạn có bao nhiêu khâu tăng")
		input_args_SizeUp = int(input("   > "))
		if input_args_SizeUp == 0:
			list_SizeUp = ([0])
		else :
			list_SizeUp = Import_Total_SizeUp(input_args_SizeUp)
		
		print ("Bạn có bao nhiêu khâu giảm")
		input_args_SizeDown = int(input("   > "))
		if input_args_SizeDown == 0:
			list_SizeDown = ([0])
		else :
			list_SizeDown = Import_Total_SizeDown(input_args_SizeDown)
		Tong_khau = input_args_SizeUp + input_args_SizeDown
		if input_args_SizeUp == 0 and input_args_SizeDown == 0:
			print ("")
			print ("Are you kidding me?")
			print ("\n" * 3)
			time.sleep(1)
			banner()
		else :
			x = 1
			y = 1
			Tong_i_tang = 0
			Tong_i_giam = 0
			while x <= input_args_SizeUp:
				Tong_i_tang += DungSai_i(list_SizeUp[x-1])
				x += 1
			while y <= input_args_SizeDown:
				Tong_i_giam += DungSai_i(list_SizeDown[y-1])
				y += 1
			Tong_i = Tong_i_tang + Tong_i_giam	
			ccx_chung = ((1000 * Dung_Sai_Total) / Tong_i)
			HeSo_IT = DungSai_IT(ccx_chung)
		Mess_2 = raw_input("Chọn khâu tăng làm khâu bồi thường ? (yes or no): ")
		if Mess_2 == "y" or Mess_2 == "Y" or Mess_2 == "yes" or Mess_2 == "Yes" or Mess_2 == "YES":
			Khau_boi_thuong = int(raw_input("Bạn muốn chọn khâu tăng nào làm khâu bồi thường? :"))
			Size_boithuong = list_SizeUp[Khau_boi_thuong - 1]
			Size_remove = list_SizeUp[Khau_boi_thuong - 1]
			list_SizeUp.remove(Size_remove)
			a = 1
			b = 1 
			list3 = []
			list4 = []
			Tong_DungSai_giam = 0
			Tong_DungSai_tang = 0
			tong_DungSai = 0
			Tong_em_giam = 0
			Tong_em_tang = 0
			while a <= input_args_SizeUp -1 : 
				data_A = PutOut_SizeUp(list_SizeUp[a -1], HeSo_IT)
				list3.extend(data_A)
				a += 1
			while b <= input_args_SizeDown :
				data_A = PutOut_SizeDown(list_SizeDown[b -1], HeSo_IT)
				list4.extend(data_A)
				b += 1
			for args1 in range(input_args_SizeUp - 1):
				Tong_DungSai_tang += list3[args1][1]
				Tong_em_tang += list3[args1][4]
			for args2 in range(input_args_SizeDown):
				Tong_DungSai_giam += list4[args2][1]
				Tong_em_giam += list4[args2][4]
			DungSai_boithuong = Dung_Sai_Total -  (Tong_DungSai_tang + Tong_DungSai_giam)
			if DungSai_boithuong >= 0: 
				em_khau_boithuong = Limit_mediumTotal - Tong_em_tang + Tong_em_giam
				es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
				ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong


				print ("\n" * 2)
				print ("Thông số các Khâu tăng:")
				print (" .-----------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |")
				print ("|----------------+---------------+-------+-------|")
				for inra1 in range(input_args_SizeUp -1):
					print ("| %s		 |	%s 	 | %s  | %s 	 |" %(list3[inra1][0], list3[inra1][1], list3[inra1][2], list3[inra1][3]))
					print ("|----------------+---------------+-------+-------|")
				print (" '-----------------------------------------------'")

				print ("Thông số các Khâu giảm:")
				print (" .-----------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |")
				print ("|----------------+---------------+-------+-------|")
				for inra2 in range(input_args_SizeDown):
					print ("| %s		 |	%s 	 | %s     | %s |" %(list4[inra2][0], list4[inra2][1], list4[inra2][2], list4[inra2][3]))
					print ("|----------------+---------------+-------+-------|")
				print (" '------------------------------------------------'")
				print ("Thông số Khâu bồi thường:")
				print (" .---------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD     |")
				print ("|----------------+---------------+-------+-----------|")
				print ("| %s		 |	%0.3f 	 | %0.3f  | %0.3f  |" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong))
				print (" '---------------------------------------------------'")
				print ("\n" * 2)
				time.sleep(5)
			else :
				print ("Dung sai khâu bồi thường âm")
				print ("\n" * 2)

		elif Mess_2 == "n" or Mess_2 == "N" or Mess_2 == "no" or Mess_2 == "NO" :
			Khau_boi_thuong = int(raw_input("Bạn muốn chọn khâu giảm nào làm khâu bồi thường? :"))
			print(list_SizeDown)
			Size_boithuong = list_SizeDown[Khau_boi_thuong - 1]
			Size_remove = list_SizeDown[Khau_boi_thuong - 1]
			list_SizeDown.remove(Size_remove)
			a = 1
			b = 1
			list3 = []
			list4 = []
			tong_DungSai = 0
			Tong_DungSai_giam = 0
			Tong_DungSai_tang = 0
			Tong_em_giam = 0
			Tong_em_tang = 0
			while a <= input_args_SizeDown -1 : 
				data_A = PutOut_SizeDown(list_SizeDown[a -1], HeSo_IT)
				list3.extend(data_A)
				a += 1
			while b <= input_args_SizeUp :
				data_A = PutOut_SizeUp(list_SizeUp[b -1], HeSo_IT)
				list4.extend(data_A)
				b += 1
			for args1 in range(input_args_SizeDown - 1):
				Tong_DungSai_giam += list3[args1][1]
				Tong_em_giam += list3[args1][4]
			for args2 in range(input_args_SizeUp):
				Tong_DungSai_tang += list4[args2][1]
				Tong_em_tang += list4[args2][4]
			DungSai_boithuong = Dung_Sai_Total -  (Tong_DungSai_tang + Tong_DungSai_giam)
			if DungSai_boithuong >= 0: 
				em_khau_boithuong = -Limit_mediumTotal + Tong_em_tang - Tong_em_giam
				es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
				ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong

				print ("\n" * 2)
				print ("Thông số các Khâu tăng:")
				print (" .-----------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |")
				print ("|----------------+---------------+-------+-------|")
				for inra1 in range(input_args_SizeUp):
					print ("| %s		 |	%s 	 | %s  | %s 	 |" %(list4[inra1][0], list4[inra1][1], list4[inra1][2], list4[inra1][3]))
					print ("|----------------+---------------+-------+-------|")
				print (" '-------------------------------------------'")

				print ("Thông số các Khâu giảm:")
				print (" .-------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |")
				print ("|----------------+---------------+-------+-------|")
				for inra2 in range(input_args_SizeDown -1):
					print ("| %s		 |	%s 	 | %s     | %s |" %(list3[inra2][0], list3[inra2][1], list3[inra2][2], list3[inra2][3]))
					print ("|----------------+---------------+-------+-------|")
				print (" '------------------------------------------'")

				print (" .---------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD     |")
				print ("|----------------+---------------+-------+-----------|")
				print ("| %s		 |	%0.3f 	 | %0.3f    | %0.3f  |" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong))
				print ("'----------------------------------------------------'")
				print ("\n" * 2)
				time.sleep(5)
			else :
				print ("Dung sai khâu bồi thường âm")
				print ("\n" * 2)


		else :
			print (error)
			print ("\n" * 2)


def function_design_probability():

	# function tính các thông số khâu tăng
	def Import_Total_SizeUp(number):
		i = 1
		list1 = []
		while i <= number:
			Size = float(input("Kích thước danh nghĩa của khâu %s (mm):" % i))
			k = float(input("Hệ số k của khâu %s (mm):" % i))
			alpha = float(input("Hệ số alpha của khâu %s (mm):" % i))			
			list1.append([Size, k, alpha])
			i += 1
		return list1

	# function tính các thông số khâu giảm
	def Import_Total_SizeDown(number):
		i = 1
		list1 = []
		while i <= number:
			Size = float(input("Kích thước danh nghĩa của khâu %s (mm):" % i))
			k = float(input("Hệ số k của khâu %s (mm):" % i))
			alpha = float(input("Hệ số alpha của khâu %s (mm):" % i))			
			list1.append([Size, k, alpha])
			i += 1
		return list1

	# nhập các  thông số khâu tổng
	Size_total = float(input("Kích thước danh nghĩa của khâu tổng (mm):"))
	Limit_max_total = float(input("Giới hạn trên của khâu tổng (mm):"))
	Limit_min_total = float(input("Giới hạn dưới của khâu tổng (mm):"))
	ktong = float(raw_input("Hệ số k của khâu tổng (mm):"))
	alpha_tong = float(raw_input("Hệ số alpha của khâu tổng (mm):"))
	Dung_Sai_Total = Limit_max_total - Limit_min_total
	if Dung_Sai_Total <= 0:
		print ("Dung sai không thể nhỏ hơn 0.")
		print ("\n" * 2)

	else:
		Limit_mediumTotal = (Limit_max_total + Limit_min_total) / 2
		#list_SizeTotal = [Size_total, Dung_Sai_Total, Limit_max_total, Limit_min_total, ktong, alpha_tong]
		# Nhập số khâu tăng và giảm
		print ("Bạn có bao nhiêu khâu tăng")
		input_args_SizeUp = int(input("   > "))
		if input_args_SizeUp == 0:
			list_SizeUp = ([0])
		else :
			list_SizeUp = Import_Total_SizeUp(input_args_SizeUp)
		
		print ("Bạn có bao nhiêu khâu giảm")
		input_args_SizeDown = int(input("   > "))
		if input_args_SizeDown == 0:
			list_SizeDown = ([0])
		else :
			list_SizeDown = Import_Total_SizeDown(input_args_SizeDown)
		Tong_khau = input_args_SizeUp + input_args_SizeDown
		if input_args_SizeUp == 0 and input_args_SizeDown == 0:
			print ("")
			print ("Are you kidding me?")
			print ("\n" * 3)
			time.sleep(1)
			banner()
		else :
			x = 1
			y = 1
			Tong_ki_tang = 0
			Tong_ki_giam = 0
			while x <= input_args_SizeUp:
				Tong_ki_tang += pow(DungSai_i(list_SizeUp[x-1][0]) * list_SizeUp[x-1][1],2)
				x += 1
			while y <= input_args_SizeDown:
				Tong_ki_giam += pow(DungSai_i(list_SizeDown[y-1][0]) * list_SizeDown[y-1][1],2)
				y += 1
			Tong_ki = Tong_ki_tang + Tong_ki_giam
			ccx_chung = (1000 * Dung_Sai_Total * ktong) / math.sqrt(Tong_ki)
			HeSo_IT = DungSai_IT(ccx_chung)
		Mess_2 = raw_input("Chọn khâu tăng làm khâu bồi thường ? (yes or no): ")
		if Mess_2 == "y" or Mess_2 == "Y" or Mess_2 == "yes" or Mess_2 == "Yes" or Mess_2 == "YES":
			Khau_boi_thuong = int(raw_input("Bạn muốn chọn khâu tăng nào làm khâu bồi thường? :"))
			Size_boithuong = list_SizeUp[Khau_boi_thuong - 1][0]
			k_boithuong = list_SizeUp[Khau_boi_thuong - 1][1]
			alpha_boithuong = list_SizeUp[Khau_boi_thuong - 1][2]
			Size_remove = list_SizeUp[Khau_boi_thuong - 1]
			list_SizeUp.remove(Size_remove)
			a = 1
			b = 1 
			list3 = []
			list4 = []
			Tk_giam = 0
			Tk_tang = 0
			tong_DungSai = 0
			Tong_em_tang = 0
			Tong_em_giam = 0
			while a <= input_args_SizeUp -1 : 
				data_A = PutOut_SizeUp(list_SizeUp[a -1][0], HeSo_IT, list_SizeUp[a -1][1], list_SizeUp[a -1][2])
				list3.extend(data_A)
				a += 1
			while b <= input_args_SizeDown :
				data_A = PutOut_SizeDown(list_SizeDown[b -1][0], HeSo_IT, list_SizeDown[b -1][1], list_SizeDown[b -1][2])
				list4.extend(data_A)
				b += 1
			for args1 in range(input_args_SizeUp - 1):
				Tk_tang += math.pow(list3[args1][1] * list3[args1][5],2)
				Tong_em_tang += list3[args1][4] + 0.5 * list3[args1][6] * list3[args1][1]
			for args2 in range(input_args_SizeDown):
				Tk_giam += math.pow(list4[args2][1] * list4[args2][5],2)
				Tong_em_giam += list4[args2][4] + 0.5 * list4[args2][6] * list4[args2][1]
			Tong_binhphuong = math.pow(ktong * Dung_Sai_Total,2)
			K_binhphuong = math.pow(k_boithuong,2)
			DungSai_boithuong = math.sqrt((Tong_binhphuong - (Tk_tang + Tk_giam)) / K_binhphuong)
			if DungSai_boithuong >= 0:
				em_khau_boithuong = Limit_mediumTotal - Tong_em_tang + Tong_em_giam - 0.5 * alpha_boithuong * DungSai_boithuong + 0.5 * alpha_tong * Dung_Sai_Total
				es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
				ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong

				print ("\n" * 2)
				print ("Thông số các Khâu tăng:")
				print (" .------------------------------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |   k   	|  alpha  |")
				print ("|----------------+---------------+-------+-------+--------------+---------|")
				for inra1 in range(input_args_SizeUp -1):
					print ("| %s		 |	%s 	 | %s  | %s 	 | %s 	| %s	  |" %(list3[inra1][0], list3[inra1][1], list3[inra1][2], list3[inra1][3] ,list3[inra1][5], list3[inra1][6]))
					print ("|----------------+---------------+-------+-------+--------------+---------|")
				print (" '------------------------------------------------------------------------'")
	
				print ("Thông số các Khâu giảm:")	
				print (" .------------------------------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD   |   k          |  alpha  |")
				print ("|----------------+---------------+-------+-------+--------------+---------|")
				for inra2 in range(input_args_SizeDown):
					print ("| %s		 |	%s 	 | %s     | %s | %s 	| %s 	  |" %(list4[inra2][0], list4[inra2][1], list4[inra2][2], list4[inra2][3] ,list4[inra2][5], list4[inra2][6]))
					print ("|----------------+---------------+-------+---------+--------------+--------|")
				print (" '--------------------------------------------------------------------'")
		
				print ("Thông số Khâu bồi thường:")
				print (" .------------------------------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD   |   k          |  alpha  |")
				print ("|----------------+---------------+-------+-------+--------------+---------|")
				print ("| %s		 |	%0.2f 	 | %0.3f | %0.3f  | %0.2f 	| %0.2f	 |" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong, k_boithuong, alpha_boithuong))
				print (" '------------------------------------------------------------------------'")
				print ("\n" * 2)
			else:
				print ("Dung sai khâu bồi thường âm")
				print ("\n" * 2)


		elif Mess_2 == "n" or Mess_2 == "N" or Mess_2 == "no" or Mess_2 == "NO" :
			Khau_boi_thuong = int(raw_input("Bạn muốn chọn khâu giảm nào làm khâu bồi thường? :"))
			Size_boithuong = list_SizeDown[Khau_boi_thuong - 1][0]
			k_boithuong = list_SizeDown[Khau_boi_thuong - 1][1]
			alpha_boithuong = list_SizeDown[Khau_boi_thuong - 1][2]
			Size_remove = list_SizeDown[Khau_boi_thuong - 1]
			list_SizeDown.remove(Size_remove)
			a = 1
			b = 1 
			list3 = []
			list4 = []
			Tk_giam = 0
			Tk_tang = 0
			tong_DungSai = 0
			Tong_em_tang = 0
			Tong_em_giam = 0
			while a <= input_args_SizeDown -1 : 
				data_A = PutOut_SizeDown(list_SizeDown[a -1][0], HeSo_IT, list_SizeDown[a -1][1], list_SizeDown[a -1][2])
				list3.extend(data_A)
				a += 1
			while b <= input_args_SizeUp :
				data_A = PutOut_SizeUp(list_SizeUp[b -1][0], HeSo_IT, list_SizeUp[b -1][1], list_SizeUp[b -1][2])
				list4.extend(data_A)
				b += 1
			for args1 in range(input_args_SizeDown - 1):
				Tk_giam += math.pow(list3[args1][1] * list3[args1][5],2)
				Tong_em_giam += list3[args1][4] + 0.5 * list3[args1][6] * list3[args1][1]
			for args2 in range(input_args_SizeUp):
				Tk_tang += math.pow(list4[args2][1] * list4[args2][5],2)
				Tong_em_tang += list4[args2][4] + 0.5 * list4[args2][6] * list4[args2][1]
			Tong_binhphuong = math.pow(ktong * Dung_Sai_Total,2)
			K_binhphuong = math.pow(k_boithuong,2)
			DungSai_boithuong = math.sqrt((Tong_binhphuong - (Tk_tang + Tk_giam)) / K_binhphuong)
			if DungSai_boithuong >= 0:
				em_khau_boithuong = -Limit_mediumTotal + Tong_em_tang - Tong_em_giam - 0.5 * alpha_boithuong * DungSai_boithuong - 0.5 * alpha_tong * Dung_Sai_Total
				es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
				ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong
				
				print ("\n" * 2)
				print ("Thông số các Khâu tăng:")
				print (" .------------------------------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |   k   	|  alpha  |")
				print ("|----------------+---------------+-------+-------+--------------+---------|")
				for inra1 in range(input_args_SizeUp):
					print ("| %s		 |	%s 	 | %s  | %s 	 | %0.2f 	| %s	  |" %(list4[inra1][0], list4[inra1][1], list4[inra1][2], list4[inra1][3] ,list4[inra1][5], list4[inra1][6]))
					print ("|----------------+---------------+-------+-------+--------------+---------|")
				print (" '------------------------------------------------------------------------'")
	
				print ("Thông số các Khâu giảm:")	
				print (" .------------------------------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |   k          |  alpha  |")
				print ("|----------------+---------------+-------+-------+--------------+---------|")
				for inra2 in range(input_args_SizeDown -1):
					print ("| %s		 |	%s 	 | %s     | %s | %s 	| %s 	  |" %(list3[inra2][0], list3[inra2][1], list3[inra2][2], list3[inra2][3] ,list3[inra2][5], list3[inra2][6]))
					print ("|----------------+---------------+-------+-------+--------------+---------|")
				print (" '------------------------------------------------------------------------'")

				print ("Thông số Khâu bồi thường:")
				print (" .------------------------------------------------------------------------.")
				print ("| Kích thước     | 	Dung Sai | SLGHT | SLGHD |   k          |  alpha  |")
				print ("|----------------+---------------+-------+-------+--------------+---------|")
				print ("| %s		 |	%0.2f 	 | %0.3f | %0.3f| %0.2f 	| %0.2f   |" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong, k_boithuong, alpha_boithuong))
				print (" '------------------------------------------------------------------------'")
				print ("\n" * 2)

			else:
				print ("Dung sai khâu bồi thường âm")
				print ("\n" * 2)
		else :
			print (error)
			print ("\n" * 2)


####################
#       Body       #
####################
banner()
choice = int(input(Mess_1))

while choice != 0:
	
	if choice == 1:
		# hàm tính toán
		print ("1: Giải bài toán kiểm tra bằng phương pháp lấp lẫn hoàn toàn")
		print ("2: Giải bài toán thiết kế bằng phương pháp lấp lẫn hoàn toàn")
		print ("3: Giải bài toán kiểm tra bằng phương pháp xác suất")
		print ("4: Giải bài toán thiết kế bằng phương pháp xác suất")
		print ("5: Back")
		choice_1 = int(input(Mess_1))
		if choice_1 == 1:
			function_check(0)
		elif choice_1 == 2 :
			function_design()
		elif choice_1 == 3 :
			function_check(1)
		elif choice_1 == 4 :
			function_design_probability()
		elif choice_1 == 5 :
			print ("\n" * 100)
			banner()
			choice = int(input(Mess_1))
		else :
			print (error)
	elif choice == 2:
		# hàm in bảng số liệu
		print ("1: Bảng dung sai tiêu chuẩn với D<= 500mm")
		print ("2: Bảng giá trị dung sai đơn vị i đối với kích thước danh nghĩa đen 500mm")
		print ("3: Bảng trị số dung sai kích thước thẳng tiêu chuẩn")
		print ("4: Trở về")
		choice_1 = int(input(Mess_1))
		if choice_1 == 1:
			table1()
		elif choice_1 == 2 :
			table2()
		elif choice_1 == 3 :
			table3()
		elif choice_1 == 4 :

			print ("\n" * 100)
			banner()
			choice = int(input(Mess_1))
		else:
			print(error)


	else :
		print  (error)
		choice = int(input(Mess_1))

print ("\n")
print ("Tạm biệt!")
print ("\n" * 3)