import os
import sys
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
path_creScript1 = os.path.join(mypath, "..\\Lib\\creScript1.py")
join_path = os.path.join(mypath, "..\\Temp")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join_path)  
from config import *

	# Nhập số khâu tăng và giảm
input_value_SizeUp = SoKhauTang
input_value_SizeDown = SoKhauGiam
call(["python", path_creScript1])

