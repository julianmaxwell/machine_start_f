import os
import re
import numpy as np
import pandas as pd
import shutil
from bs4 import BeautifulSoup
import requests

import subprocess

pip_addr = [
    "https://pypi.python.org/simple",
    "https://pypi.douban.com/simple/",
    "https://mirrors.aliyun.com/pypi/simple",
    "https://pypi.tuna.tsinghua.edu.cn/simple",
    "https://pypi.mirrors.ustc.edu.cn/simple",
    "http://pypi.sdutlinux.org/",
    "http://pypi.hustunique.com/",

]
packe_name = "beautifulsoup4"

order_ = "pip install -i " + pip_addr[1] + " " + packe_name
print(order_)

def install_packet(self, order):
    install_r = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    out, _inn = install_r.communicate()
    print(out.decode("gbk"))

install_packet(5, order_)

bb = requests.get("https://www.javlands.net/tw/star/y72lzx.html")
print(bb.text)
bt = BeautifulSoup(bb.text)
xx = bt.find_all("span", {"class": "bsid"})

name_dic = {}

print(bt.title.string)
all_ = bt.title.string
name = all_.split()[0]
for x in xx:
    print(x)
    print(type(x))
    if x.string:
        print(x.string)
        try:
            name_dic[name].add(x.string)
        except:
            name_dic[name] = set()
            name_dic[name].add(x.string)
print(name_dic)
print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")




zzr=bt.find_all("a", href=True)
a = set()
for zr in zzr:
    text = zr.get("href")
    pp = re.search("(.*)\?page=(.+)", text)
    try:
        if len(a) == 0:
            addr = pp.groups()[0]
        else:
            addr = pp.groups()[0] + "?page=" + str(pp.groups()[1])
        a.add(addr)

    except:
        pass

print(a)
        # ff = uu.get_tgext(strip=True)
        # print(ff["href"])



    # d = next_u.findall("li>a")
    # print(d)

# print(bt.head)
# print(bt.body.children , "ffffffffffffffffffff")