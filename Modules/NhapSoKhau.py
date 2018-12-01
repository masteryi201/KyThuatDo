import os
import sys
from pathlib import Path
mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
sys.path.append(join_path)  
from config import *

	# Nhập số khâu tăng và giảm
input_value_SizeUp = SoKhauTang
input_value_SizeDown = SoKhauGiam

