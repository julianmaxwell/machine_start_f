# I:\20210826桌面\新建文件夹 (3)\网数据
import sys

# from ttest_packet import packet_test
pandas_path = 'D:\\Python39\\lib\\site-packages\\pandas'
sys.path.append(pandas_path)
import pandas

pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)
path_old = r"I:\20210826桌面\新建文件夹 (3)\网数据\通话2.csv"
data_086 = pandas.read_csv(path_old, encoding="gbk")
data_086.columns = ["时间", "地区", "类型", "电话号码", "通话时间", "主被叫", "套餐类型", "mask"]
data_086.loc[:, "时间"] = pandas.to_datetime(data_086.loc[:, "时间"])
