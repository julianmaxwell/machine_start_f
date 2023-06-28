import pandas
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)
path_old = r"C:\Users\Administrator\Desktop\recorder.txt"
data = pandas.read_table(path_old, header=None)
ff = data.loc[:, 0]
def split_new(data):
    xx = data.split()
    if len(xx) > 1:
        name = xx[0]
    else:
        name = ""
    return name

def split_new_phone(data):
    xx = data.split()
    if len(xx) > 1:
        phone = xx[1]
    else:
        phone = xx[0]
    return phone

fk = ff.apply(split_new)
fp = ff.apply(split_new_phone)
data = pandas.concat([data, fk], axis=1)
data = pandas.concat([data, fp], axis=1)
data.columns = ["nouse", "时间", "时长", "通话类型", "姓名", "电话", ]
data = data.loc[:, ["姓名", "电话", "时间", "时长", "通话类型"]]

import datetime
xx = datetime.datetime.now()
str_time = xx.strftime("%Y_%m_%d_%H_%M_%S")
path_ = r"I:\luo\\"
file_name = path_ + "luo_phone_may_later__" + str_time + ".csv"
data2 = data.groupby(["姓名", "通话类型"])
data.loc[:, "时间"] = pandas.to_datetime(data.loc[:, "时间"].str.strip(), format="%y-%m-%d %H:%M")

def app_data(data):
    data_ = int(data.replace("秒", ""))
    return data_

data_t = data.loc[:, "时长"].apply(app_data)
data.loc[:, "时长"] = data_t

def app_time(data):
    return data.dayofweek

data.loc[:, "星期"] = data.loc[:, "时间"].apply(app_time)

def app_moth(data):
    return data.month

data.loc[:, "月份"] = data.loc[:, "时间"].apply(app_moth)

def app_day(data):
    return data.day

data.loc[:, "日"] = data.loc[:, "时间"].apply(app_day)
datap = pandas.pivot_table(data, index=["姓名", "通话类型", "月份", "星期"], values=["电话"], aggfunc=["count"])
# datap = pandas.pivot_table(data, index=["姓名", "通话类型", "月份", "星期"], values=["电话", "时长"],
#                            aggfunc={"姓名": "count", "时长": "mean"})

datap = pandas.pivot_table(data, index=["姓名", "通话类型", "月份", "星期", "日"], values=["电话", "时长"],
                           aggfunc={"电话": "count", "时长": "sum"})
# data_g = data.groupby(by=["姓名", "通话类型", "月份", "星期", "日"])


