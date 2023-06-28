import pandas
import datetime
import re

pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)

path_ = r"C:\Users\Administrator\Desktop\新建文件夹 (3)\通话记录.csv"
data = pandas.read_csv(path_, encoding="gbk", header=0, parse_dates=["时间"])
kb = data

k123 = data
k123 = k123.set_index("时间")
print(k123.to_period("M"))

# data = pandas.read_csv(path_, encoding="gbk", header=0)
# print(data.loc[:, "时间"])
# ff = pandas.to_datetime(data.loc[:, "时间"])
data.reset_index(drop=True, inplace=True)
# data.set_index("时间", inplace=True)
# print(data.loc[:, "时间"])
# freq = pandas.pdata.loc[:, "时间"]

data.loc[:, "week"] = data.loc[:, "时间"].apply(lambda x: x.weekday())

xx = data.loc[:, "week"] == 0
xx_ = data.loc[:, "week"].apply(lambda x: x in (0, 6, 2, 1))
# print(xx_)
xx = data[xx_]
print("ppppppppppppppppppppppppppp")
# print(xx)
# print(xx)
data_r = xx
dk = data_r.loc[:, "时间"].apply(lambda x: x.hour < 10)

# print(dk)
data_r2 = data_r[dk]

dk2 = data_r.loc[:, "时间"].apply(lambda x: x.hour >=21)
data_r22 = data_r[dk2]
data_r2 = pandas.concat([data_r2, data_r22])


print("fffffffffffffffffffffffffffffffffffffffffffff")
dp = data_r2.loc[:, "电话号码"].apply(lambda x: x not in (15882544589, 13350200796, 18398111207, 18982574589))
data_r3 = data_r2[dp]

# print(data_r3)
def apply_time_l(data):
    pattent = re.compile(r"[分秒]")
    result = re.split(pattent, data)
    result = int(result[0])*60 + int(result[1])
    return result

def hours_minit_add(data):
    hours_ = data.hour
    minut = data.minute
    totle = hours_*60 + minut
    return totle
kk = data_r3.loc[:, "通话时间"]
# print(kk)
# print(data_r3.loc[:, "通话时间"].transform(apply_time_l))
kf = data_r3.loc[:, "通话时间"].transform(apply_time_l)
data_r3 = data_r3.merge(kf, left_index=True, right_index=True)
data_r4 = data_r3.sort_values(by=["电话号码", "week"])
print(data_r4)
kf2 = data_r3.loc[:, "时间"].transform(hours_minit_add)
data_r3 = data_r3.merge(kf2, left_index=True, right_index=True)
data_r3 = data_r3.groupby(by=["电话号码"])
def app_group(data):
    print(data)
    return data.count()

print("****************************************")
count_ = data_r3.apply(app_group)
print(count_)
# print(data_r3_time_l)

data_back = kb
kkb = data_back[data_back.loc[:, "电话号码"] == 6253]
kkb = kkb.loc[:, "通话时间"].transform(apply_time_l)
# kkb = kkb.merge(kf, left_index=True, right_index=True)
print(kkb)
print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", len(kkb))

