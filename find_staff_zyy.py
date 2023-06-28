import pandas
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)
path_old = r"I:\20210826桌面\新建文件夹 (3)\网数据\人员表.txt"
data = pandas.read_table(path_old, header=None, sep="\d+元")

# print(data)

data = data.drop([4], axis=1)
# print(data)
data.to_csv(r"I:\20210826桌面\新建文件夹 (3)\网数据\zyy人员表.txt", index=False)

data_totle= pandas.concat([data.loc[:, 0], data.loc[:, 1], data.loc[:, 2], data.loc[:, 3], ], ignore_index=True)
# print(data_totle)
data_totle.to_csv(r"I:\20210826桌面\新建文件夹 (3)\网数据\zyy人员表.csv", index=False, encoding="gbk")