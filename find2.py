import numpy
import pandas
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 1500)
data = pandas.read_csv(r"D:\av_file_work\avmoves_table.csv", header=0, encoding="gbk")
# data.to_csv(r"D:\av_file_work\avmoves_table.csv", mode="w", index=None, encoding="gbk")
aa = pandas.read_csv(r"D:\av_file_work\temporary_data.csv", header=None, encoding="gbk", names=["moves_id", "moves_title", "distribute_time"])

aa.loc[:, "actor_name"] = "大沢美加".strip()
aa.loc[:, "moves_path"] = None
print("***************************************")
print(aa)

# print(len(kuisi))
# n_l = len(kuisi)
# data_new_actor_name = [None for n in range(n_l)]
# print(data.columns)
# print(data_new_actor_name)
# datan = zip(data_new_actor_name, kuisi, data_new_actor_name, data_new_actor_name, data_new_actor_name, data_new_actor_name)
#
# data_new = pandas.DataFrame(list(datan), columns=data.columns)
# data_new.loc[:, "actor_name"] = "あやみ旬果"
# print(data_new)
old_data_len = len(data)
data = pandas.concat([data, aa], ignore_index=True)

data.drop_duplicates(subset=["moves_id"], inplace=True, keep="first")
print(len(data), old_data_len)
# print(data)
data_w = data.iloc[old_data_len:, ]
print("*****************************")
print(data_w)

if len(data_w) != 0:
    pass
    data_w.to_csv(r"D:\av_file_work\avmoves_table.csv", mode="a", index=False, encoding="gbk", header=False)