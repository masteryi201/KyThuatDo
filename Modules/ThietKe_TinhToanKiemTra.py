# -*- coding: utf-8 -*-
# Import
import math
import os
import sys
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
path_ThongSoKhauTang = os.path.join(mypath, "..\\Temp\\ThietKe_ThongSoKhauTang.py")
path_ThongSoKhauGiam = os.path.join(mypath, "..\\Temp\\ThietKe_ThongSoKhauGiam.py")
path_intermediate = os.path.join(mypath, "..\\Modules\\intermediate_steps.py")
sys.path.append(join_path)  
from config import *
from ThietKe_ThongSoKhauTang import *
from ThietKe_ThongSoKhauGiam import *

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
if value == 0:
	input_args_SizeUp = SoKhauTang
	input_args_SizeDown = SoKhauGiam
	list_SizeUp = tup_in_creScript3
	list_SizeDown = tup_in_creScript4
	Dung_Sai_Total = tup_in_ThietKe_NhapKhauTong[1]
	Limit_mediumTotal = (tup_in_ThietKe_NhapKhauTong[2] + tup_in_ThietKe_NhapKhauTong[3]) / 2
	Tong_khau = input_args_SizeUp + input_args_SizeDown
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
	if check_true == 0:
		Khau_boi_thuong = KhauBoiThuongTang
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
			file_signal = open(path_config, mode='a')
			file_signal.write("""
T_am_signal = False
			""")
			file_signal.close()			
			em_khau_boithuong = Limit_mediumTotal - Tong_em_tang + Tong_em_giam
			es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
			ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong
		else :
			file_signal = open(path_config, mode='a')
			file_signal.write("""
T_am_signal = True
			""")
			file_signal.close()
		file_resurt = open(path_config, mode='a')
		for  inra1 in range(input_args_SizeUp -1):
			file_resurt.write("""
ktt%s = %s
dst%s = %s
est%s = %s
eit%s = %s\n
			""" %(inra1,list3[inra1][0],inra1,list3[inra1][1],inra1, list3[inra1][2],inra1, list3[inra1][3]))
		for inra2 in range(input_args_SizeDown):
			file_resurt.write("""
ktd%s = %s
dsd%s = %s
esd%s = %s
eid%s = %s\n
			""" %(inra2, list4[inra2][0], inra2, list4[inra2][1], inra2, list4[inra2][2], inra2, list4[inra2][3]))

		file_resurt.write("""
kt_boithuong = %0.5f
ds_boithuong = %0.5f
es_boithuong = %0.5f
ei_boithuong = %0.5f
Vitri_khauboithuong = %s\n
			""" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong,Khau_boi_thuong))
		file_resurt.close()
	elif check_true == 1 :
		Khau_boi_thuong = KhauBoiThuongGiam
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
			file_signal = open(path_config, mode='a')
			file_signal.write("""
T_am_signal = False
			""")
			file_signal.close()
			em_khau_boithuong = -Limit_mediumTotal + Tong_em_tang - Tong_em_giam
			es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
			ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong
		else :
			file_signal = open(path_config, mode='a')
			file_signal.write("""
T_am_signal = True
			""")
			es_khau_boithuong = 0
			ei_khau_boithuong = 0
			file_signal.close()

		file_resurt = open(path_config, mode='a')
		for  inra1 in range(input_args_SizeUp):
			file_resurt.write("""
ktt%s = %s
dst%s = %s
est%s = %s
eit%s = %s\n
			""" %(inra1, list4[inra1][0], inra1, list4[inra1][1], inra1, list4[inra1][2], inra1, list4[inra1][3]))
		for inra2 in range(input_args_SizeDown -1):
			file_resurt.write("""
ktd%s = %s
dsd%s = %s
esd%s = %s
eid%s = %s\n
			""" %(inra2, list3[inra2][0], inra2, list3[inra2][1], inra2, list3[inra2][2], inra2, list3[inra2][3]))

		file_resurt.write("""
kt_boithuong = %0.5f
ds_boithuong = %0.5f
es_boithuong = %0.5f
ei_boithuong = %0.5f
Vitri_khauboithuong = %s\n
			""" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong,Khau_boi_thuong))
		file_resurt.close()

elif value == 1:
	input_args_SizeUp = SoKhauTang
	input_args_SizeDown = SoKhauGiam
	list_SizeUp = tup_in_creScript3
	list_SizeDown = tup_in_creScript4
	Dung_Sai_Total = tup_in_ThietKe_NhapKhauTong[1]
	alpha_tong = tup_in_ThietKe_NhapKhauTong[5]
	ktong = tup_in_ThietKe_NhapKhauTong[4]
	Limit_mediumTotal = (tup_in_ThietKe_NhapKhauTong[2] + tup_in_ThietKe_NhapKhauTong[3]) / 2
	Tong_khau = input_args_SizeUp + input_args_SizeDown
	x = 1
	y = 1
	Tong_ki_tang = 0
	Tong_ki_giam = 0
	print(list_SizeUp)
	print(list_SizeDown)
	while x <= input_args_SizeUp:
		Tong_ki_tang += pow(DungSai_i(list_SizeUp[x-1][0]) * list_SizeUp[x-1][1],2)
		x += 1
	while y <= input_args_SizeDown:
		Tong_ki_giam += pow(DungSai_i(list_SizeDown[y-1][0]) * list_SizeDown[y-1][1],2)
		y += 1
	Tong_ki = Tong_ki_tang + Tong_ki_giam
	ccx_chung = (1000 * Dung_Sai_Total * ktong) / math.sqrt(Tong_ki)
	HeSo_IT = DungSai_IT(ccx_chung)
	print(HeSo_IT)
	if check_true == 0:
		Khau_boi_thuong = KhauBoiThuongTang
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
			file_signal = open(path_config, mode='a')
			file_signal.write("""
T_am_signal = False
			""")
			file_signal.close()
			em_khau_boithuong = Limit_mediumTotal - Tong_em_tang + Tong_em_giam - 0.5 * alpha_boithuong * DungSai_boithuong + 0.5 * alpha_tong * Dung_Sai_Total
			es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
			ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong
		else :
			file_signal = open(path_config, mode='a')
			file_signal.write("""
T_am_signal = True
			""")
			file_signal.close()

		file_resurt = open(path_config, mode='a')
		for  inra1 in range(input_args_SizeUp -1):
			file_resurt.write("""
ktt%s = %s
dst%s = %s
est%s = %s
eit%s = %s
kt%s = %s
at%s = %s\n
			""" %(inra1,list3[inra1][0],inra1,list3[inra1][1],inra1, list3[inra1][2],inra1, list3[inra1][3], inra1, list3[inra1][5], inra1, list3[inra1][6]))
		for inra2 in range(input_args_SizeDown):
			file_resurt.write("""
ktd%s = %s
dsd%s = %s
esd%s = %s
eid%s = %s
kd%s = %s
ad%s = %s\n
			""" %(inra2, list4[inra2][0], inra2, list4[inra2][1], inra2, list4[inra2][2], inra2, list4[inra2][3], inra2, list4[inra2][5], inra2, list4[inra2][6]))

		file_resurt.write("""
kt_boithuong = %0.5f
ds_boithuong = %0.5f
es_boithuong = %0.5f
ei_boithuong = %0.5f
k_boithuong = %0.5f
a_boithuong = %0.5f
Vitri_khauboithuong = %s\n
			""" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong, k_boithuong, alpha_boithuong,Khau_boi_thuong))
		file_resurt.close()

	if check_true == 1:
			Khau_boi_thuong = KhauBoiThuongGiam
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
				file_signal = open(path_config, mode='a')
				file_signal.write("""
T_am_signal = False
				""")
				file_signal.close()
				em_khau_boithuong = -Limit_mediumTotal + Tong_em_tang - Tong_em_giam - 0.5 * alpha_boithuong * DungSai_boithuong - 0.5 * alpha_tong * Dung_Sai_Total
				es_khau_boithuong = em_khau_boithuong + 0.5 * DungSai_boithuong
				ei_khau_boithuong = es_khau_boithuong - DungSai_boithuong
			else :
				file_signal = open(path_config, mode='a')
				file_signal.write("""
T_am_signal = True
				""")
				file_signal.close()

			file_resurt = open(path_config, mode='a')
			for  inra1 in range(input_args_SizeUp):
				file_resurt.write("""
ktt%s = %s
dst%s = %s
est%s = %s
eit%s = %s
kt%s = %s
at%s = %s\n
			""" %(inra1, list4[inra1][0], inra1, list4[inra1][1], inra1, list4[inra1][2], inra1, list4[inra1][3], inra1, list4[inra1][5], inra1, list4[inra1][6]))
			for inra2 in range(input_args_SizeDown -1):
				file_resurt.write("""
ktd%s = %s
dsd%s = %s
esd%s = %s
eid%s = %s
kd%s = %s
ad%s = %s\n
			""" %(inra2, list3[inra2][0], inra2, list3[inra2][1], inra2, list3[inra2][2], inra2, list3[inra2][3], inra2, list3[inra2][5], inra2, list3[inra2][6]))

			file_resurt.write("""
kt_boithuong = %0.5f
ds_boithuong = %0.5f
es_boithuong = %0.5f
ei_boithuong = %0.5f
k_boithuong = %0.5f
a_boithuong = %0.5f
Vitri_khauboithuong = %s\n
			""" %(Size_boithuong, DungSai_boithuong, es_khau_boithuong, ei_khau_boithuong, k_boithuong, alpha_boithuong,Khau_boi_thuong))
			file_resurt.close()

call(["python", path_intermediate])
