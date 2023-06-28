
"""
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

pip3 download torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

pip download torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

"""

# import subprocess
#
# xx = subprocess.Popen(r"\D:\machine\机器端\venv\Scripts\pip3.exe install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113", shell=True, stdout=subprocess.PIPE)
# single = xx.stdout.readlines()
#
# print(single)
import pickle
import pandas
from functools import reduce
xx = ["aa", 22, 33, "bb"]
xxx = pickle.dumps(xx)
xd = {"aa":xxx[:10], "bb":xxx[10:20], "cc":xxx[20:]}
print(xd)
xs = pandas.Series(data=xd)
print(xs)
bb = reduce(lambda x,y: x+y, xs)
print(bb)

