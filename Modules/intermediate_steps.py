import math
import os
import sys
from pathlib import Path
from subprocess import call

mypath = Path().absolute()
join_path = os.path.join(mypath, "..\\Temp")
path_config = os.path.join(mypath, "..\\Temp\\config.py")
path_creResultScript2 = os.path.join(mypath, "..\\Lib\\creResultScript2.py")
path_Warning = os.path.join(mypath, "..\\Modules\\Warning_Resend.py")
sys.path.append(join_path)  
from config import *

if T_am_signal == True :
	call(["python", path_Warning])
elif T_am_signal == False :
	call(["python", path_creResultScript2])
