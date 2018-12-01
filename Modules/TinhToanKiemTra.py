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
path_ThongSoKhauTang = os.path.join(mypath, "..\\Temp\\ThongSoKhauTang.py")
path_ThongSoKhauGiam = os.path.join(mypath, "..\\Temp\\ThongSoKhauGiam.py")
sys.path.append(join_path)  
from config import *
from ThongSoKhauTang import *
from ThongSoKhauGiam import *

input_value_SizeUp = SoKhauTang
input_value_SizeDown = SoKhauGiam
if tup_in_creScript1 == ([], [0, 0, 0]) :
	list_SizeUp = ([[0, 0, 0, 0, 0, 1, 0]], [0, 0, 0])
else :
	list_SizeUp = tup_in_creScript1
if tup_in_creScript2== ([], [0, 0, 0]) :
	list_SizeDown = ([[0, 0, 0, 0, 0, 1, 0]], [0, 0, 0])
else :
	list_SizeDown = tup_in_creScript2
if value == 1:
	alpha_tong = float(atong)
	ktong = float(ktong)
elif value == 0:
	alpha_tong = 0
	ktong = 1
A_tong = list_SizeUp[-1][0] - list_SizeDown[-1][0]
i = 1
j = 1
T_SizeUp = 0
T_SizeDown = 0
kT_SizeUp = 0
kT_SizeDown = 0
Em_SizeUp = 0
Em_SizeDown = 0
while i <= input_value_SizeUp:
	T_SizeUp += list_SizeUp[0][i-1][1]
	kT_SizeUp += math.pow(list_SizeUp[0][i-1][1]*list_SizeUp[0][i-1][5],2)
	Em_SizeUp += list_SizeUp[0][i-1][4] + 0.5*list_SizeUp[0][i-1][6]*list_SizeUp[0][i-1][1]
	i += 1
while j <= input_value_SizeDown:
	T_SizeDown += list_SizeDown[0][j-1][1]
	kT_SizeDown += math.pow(list_SizeDown[0][j-1][1]*list_SizeDown[0][j-1][5],2)
	Em_SizeDown += list_SizeDown[0][j-1][4] + 0.5*list_SizeDown[0][j-1][6]*list_SizeDown[0][j-1][1]
	j += 1
if value == 1 :
	T_tong = ( 1 / ktong )*(math.sqrt(kT_SizeUp + kT_SizeDown))
elif value == 0 :
	T_tong = T_SizeUp + T_SizeDown
Em_tong = Em_SizeUp - Em_SizeDown - 0.5*alpha_tong*T_tong
ES_tong = Em_tong + 0.5*T_tong
EI_tong = ES_tong - T_tong

if value == 1:
	file_object =  open(path_config, mode='a')
	file_object.write("""
A_tong = %0.5f
T_tong = %0.5f
ES_tong = %0.5f
EI_tong = %0.5f
		""" %(A_tong, T_tong, ES_tong, EI_tong))
elif value == 0:
	file_object =  open(path_config, mode='a')
	file_object.write("""
A_tong = %0.5f
T_tong = %0.5f
ES_tong = %0.5f
EI_tong = %0.5f
		""" %(A_tong, T_tong, ES_tong, EI_tong))	