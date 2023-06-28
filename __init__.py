
import os
import sys

print(os.getcwd())
xx = os.getcwd()
path_ = r"d:\machine\机器端"
sys.path.append(path_)
path__ = r"d:\machine"
sys.path.append(path__)
from 机器端 import find_086

import pandas
print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
print(pandas.__path__)

# import find_086
# import find_
# import find_staff_zyy
# # os.chdir(path_)
# # import find_086
# # os.chdir(xx)
# print(find_086.data_086)