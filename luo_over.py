import pandas
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)
import re

path_old = r"C:\Users\Administrator\Desktop\新建文件夹 (3)\通话记录.csv"
data = pandas.read_csv(path_old, encoding="gbk", header=0, parse_dates=["时间"])

print(data)
print(data[data.loc[:, "电话号码"] == 61082])
print("cccccccccccccccccccccccccccccccccccccc")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

search_month = [2, 3, 4]
data.loc[:, "month"] = data.loc[:, "时间"].apply(lambda x: x.month)
data_old_ = data.loc[:, "month"].apply(lambda x: x in search_month)
data_old = data[data_old_]
data_new_columns = ["时间", "地区", "类型", "电话号码", "通话时间", "主被叫", "套餐类型", "mask"]
path_new =r"I:\tallken\通话2.csv"
data_new = pandas.read_csv(path_new, encoding="gbk")
data_new.columns = data_new_columns
print("ffffkkkkkkkkkkkkkkkkkkkkkk")
print(data_new)
data_5_m = data_new.loc[pandas.to_datetime(data_new.loc[:, "时间"]) > pandas.to_datetime("21-05-21 10:40")]
# print("wwwwwwwwwwwwwwwwwwwwwwwwwwwww2")
# print(data_5_m)
# print(len(data_5_m), "*****************2")




#
# print(data_new[data_new.loc[:, "电话号码"] == 13778748551])
# xx = data_new[data_new.loc[:, "电话号码"] == 13778748551]
# xx.to_csv(r"I:\tallken\结果.csv")

data_new.loc[:, "时间"] =pandas.to_datetime(data_new.loc[:, "时间"])
print(data_new.loc[:, "时间"] )
data_new.loc[:, "month"] = data_new.loc[:, "时间"].apply(lambda x: x.month)
data_old_ = data_new.loc[:, "month"].apply(lambda x: x in search_month)
data_new = data_new[data_old_]


"""
data_new

data_old
"""
print(len(data_new), len(data_old), "kkkkkkkkkkkkkkkkkkkkkkkkkk")
print(data_new)
print("kffffffffffffkkkkkkkkkkkkkkkkkkkffffffffffff")
data_new = data_new.set_index("时间", drop=False)
data_new.index.name = "ff"
data_old = data_old.set_index("时间", drop=False)
data_old.index.name = "ff"
data_new_set = data_new.index
data_new_set_ = []
for da_ in data_new_set:
    # print(da_.strftime("%Y-%m-%d %H:%M:%S"))
    data_new_set_.append(da_.strftime("%Y-%m-%d %H:%M:%S"))
data_new_set = set(data_new_set_)


data_old_set = data_old.index
data_old_set_ = []
for dad_ in data_old_set:
    # print(dad_.strftime("%Y-%m-%d %H:%M:%S"))
    data_old_set_.append(dad_.strftime("%Y-%m-%d %H:%M:00"))

data_old_set = set(data_old_set_)

"""
data_new_set

data_old_set
"""


subb = data_new_set - data_old_set
# for dd in data_old_set:
#     print(type(dd))
# for d in data_new_set:
#     print(d)
# for d_ in data_old_set:
#     print(d_)
print(len(data_new_set), len(data_old_set), len(subb))
# print(data_old)

subb_l = list(subb)
for l in subb_l:
    print(l)
data_new__ = data_new.loc[subb_l, :]
data_new__.loc[:, "week"] = data_new__.loc[:, "时间"].apply(lambda x: x.weekday())
data_new__ = data_new__.drop("时间", axis=1)
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 15108114574]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 18982574589]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 15982527807]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 13882554488]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 15882544589]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 15881903797]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 18728552335]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 13882589376]
data_new__ = data_new__[data_new__.loc[:, "电话号码"] != 13684434738]
print(data_new__)
print("ppppppppppppppppppppppppppppppppppppppp")
data_new__g = data_new__.groupby(by=["电话号码"])
print(data_new__g.count())

# data_new__.to_csv(r"C:\Users\Administrator\Desktop\新建文件夹 (3)\筛选结果.csv", encoding="gbk")
path_1 = r"I:\tallken\吕.csv"

def app_new(data):
    # print(data, type(data), "fffffffffffffffffffffffffffffffffff")
    datan = data.values[0]
    if re.match("\d", datan):
        # data.loc["电话"] = datan
        # data.loc["姓名"] = None
        return None, datan
    else:
        data_re = datan.split()
        # data.loc["电话"] = data_re[1]
        # data.loc["姓名"] = data_re[0]
        return data_re[0], data_re[1]

def get_monitor_data(path):
    data = pandas.read_csv(path, encoding="gbk")
    data.columns = ["姓名电话", "时间", "时长", "类别"]
    data.loc[:, "姓名电话"] = data.loc[:, "姓名电话"].str.strip("?")
    data.loc[:, "时间"] = data.loc[:, "时间"].str.strip("?")
    data.loc[:, "时长"] = data.loc[:, "时长"].str.strip("?")
    data.loc[:, "时长"] = data.loc[:, "时长"].str.strip("秒")
    data.loc[:, "类别"] = data.loc[:, "类别"].str.strip("?")
    print("pppppppppppppppppppppppppppppppppppppppfffffffffffffffffffffff")
    data2 = data.apply(app_new, axis=1, result_type="expand")
    data = pandas.concat([data, data2], axis=1)
    data = data.loc[:, [0, 1,  "时间", "时长", "类别"]]
    data.rename(columns={0:"姓名", 1:"号码"}, inplace=True)
    # print(data)
    return data
import re
def parse_search_data_time(data):
    datan = data.loc["通话时间"]
    datan = re.split("[分秒]", datan)
    datan.remove("")
    # print(datan)
    if len(datan) > 1:
        times = int(datan[-1]) + int(datan[0])*60
    else:
        times = int(datan[0])
    return times

machine_data = get_monitor_data(path_1)

machine_data = machine_data[pandas.to_datetime(machine_data.loc[:, "时间"]) > pandas.to_datetime("21-05-21 10:40")]
# print("m,mmmmmmmmm", len(machine_data))
# print((machine_data[machine_data.loc[:, "时长"] == "0"]))
machine_data = machine_data[machine_data.loc[:, "时长"] != "0"]
# machine_data = machine_data[pandas.to_datetime(machine_data.loc[:, "时间"]) <= pandas.to_datetime("2021/8/9 18:47")]
machine_data_hkh = machine_data[machine_data.loc[:, "号码" ] == "61082"]
print("PPPPKKKKKKLLLLLLLL")
print(machine_data_hkh)
print(len(machine_data_hkh))
print("PPPPKKKKKKLLLLLLLL")
print(machine_data.tail(10))
data_5_m = data_5_m[data_5_m.loc[:, "通话时间"] != 0]
print(data_5_m.head(10))
print(data_5_m.tail(10))
print("machine_data len is {}  search data len is {}".format(len(machine_data), len(data_5_m)) )

data_5_m_ = data_5_m.apply(parse_search_data_time, axis=1,  result_type="expand")
data_5_m = pandas.concat([data_5_m, data_5_m_], axis=1)
data_5_m = data_5_m.sort_values(0)

print(data_5_m)
data_5_m_g = data_5_m.groupby(["电话号码"])
# print(data_5_m.apply({"count": "count“,}))
print("pppppppppppppppkkkkkkkkkkkkkkkkkkkkk")

# print(data_5_m.count(axis=1))