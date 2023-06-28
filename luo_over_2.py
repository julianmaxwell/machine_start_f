import pandas
import re
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)


data = r"I:\tallken\吕.csv"

data = pandas.read_csv(data, encoding="gbk")

data.columns = ["姓名电话", "时间", "时长", "类别"]

data.loc[:, ["姓名", "电话"]] = data.loc[:, "姓名电话"].str.extract("(\D*)\s*(\d*)")
# data_ = data.loc[:, "姓名电话"].str.contains("\W")
# print(data)

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
data_old = data

data = data.loc[:, "姓名电话"]
data = pandas.DataFrame(data)

data_neww = data.apply(app_new, axis=1, result_type="expand")
# print(data_neww)
data_old.loc[:, "姓名"] = data_neww.iloc[:, 0]
data_old.loc[:, "电话"] = data_neww.iloc[:, 1]
data_old.drop("姓名电话", inplace=True, axis=1)


def del_ques(data):
    ff = data.str.replace("\?", "")
    return ff



data_old = data_old.apply(del_ques)
print(data_old)

data_old_g = data_old.groupby("电话")
dd = data_old_g.count()
# print(dd.sort_values("时间"))
print("fffffffffffffffffffffffffffffffffffffdddddddddddddddddd")
kk = data_old.loc[:, "电话"] == "62715"

print(data_old[kk])
# print(kk)
# print(data_old[data_old.loc[:, "电话"] == 62715])