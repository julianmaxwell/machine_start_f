"""
nb  fdsafdasgdadhgadfhsad

"""

import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenu
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.Qt import Qt
import numpy

if __name__ == "__main__":
    import 通信查询 as txcx
    import find_086
    import find_
    import find_staff_zyy
else:
    print(os.getcwd())
    from . import 通信查询 as txcx
    from . import find_086
    from . import find_
    from . import find_staff_zyy

data_new_columns = ["时间", "地区", "类型", "电话号码", "通话时间", "主被叫", "套餐类型", "mask"]
class query_(txcx.Ui_Form):
    def __init__(self):
        super(query_, self).__init__()

    def setupUi(self, Form):
        super(query_, self).setupUi(Form)
        super(query_, self).retranslateUi(Form)
        self.pushButton_txcx.clicked.connect(self.read_086)
        self.pushButton_txcx_2.clicked.connect(self.read_phone)
        self.pushButton_txcx_9.clicked.connect(self.get_zyystaff)

        self.tableView_txcx_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_txcx_2.customContextMenuRequested.connect(self.contextMenuEvent1)

    def read_086(self):
        self.stackedWidget_txcx.setCurrentIndex(0)
        data = find_086.data_086
        data.columns = data_new_columns
        data_l = len(data.columns)
        data_n = len(data)
        self.model_txcx = QStandardItemModel(data_n, data_l)
        self.model_txcx.setHorizontalHeaderLabels(data.columns)
        self.tableView.setModel(self.model_txcx)
        for d in range(data_n):
            item_ii = []
            datae = data.loc[d, :]
            for ixx in data_new_columns:
                try:
                    if isinstance(datae.loc[ixx], numpy.int64):
                        data_str = str(datae.loc[ixx])
                        item_ii.append(QStandardItem(data_str))
                        print(ixx)
                    else:
                        item_ii.append(QStandardItem(datae.loc[ixx]))
                except Exception as e:
                    data_str = str(datae.loc[ixx])
                    item_ii.append(QStandardItem(data_str))
            for item in item_ii:
                try:
                    self.model_txcx.setItem(d, item_ii.index(item), item)
                except Exception as e:
                    print(f"ok2 {d}, {e}")

    def read_phone(self):
        self.stackedWidget_txcx.setCurrentIndex(1)
        self.data_phone = find_.data
        data = find_.data
        columns = data.columns
        data_n = len(data)
        data_c = len(columns)
        model_ = QStandardItemModel(data_n, data_c)
        model_.setHorizontalHeaderLabels(columns)
        self.tableView_txcx_2.setModel(model_)
        for da in range(data_n):
            data_da = data.loc[da, :]
            da_e = []
            for every_c in columns:
                if isinstance(data_da.loc[every_c], str):
                    data_str = data_da.loc[every_c]
                else:
                    data_str = str(data_da.loc[every_c])
                b = QStandardItem(data_str)
                b.checkState()
                b.column()
                b.index()
                da_e.append(QStandardItem(data_str))
            for dad in da_e:
                model_.setItem(da, da_e.index(dad), dad)


    def get_zyystaff(self):
        xx = self.stackedWidget_txcx.indexOf(self.page_txcx_3)
        print(xx, "point2")
        self.stackedWidget_txcx.setCurrentIndex(xx)
        data = find_staff_zyy.data_totle
        data = data.values
        print(f"totle_ data l is {len(data)}")
        data_c_l = 8
        data_in_l = len(data)//8
        print(data_in_l, data_c_l)
        self.namemodel = QStandardItemModel(data_in_l, data_c_l)

        # self.namemodel.setHorizontalHeaderLabels(["0", "1", "2", "3", "4", "5", "6", "7"])


        print("im in staff")
        self.tableView_txcx_3.setModel(self.namemodel)
        print("im in staff2")
        try:
            for n in range(len(data)):
                item_ = QStandardItem(data[n])
                print(data[n])
                index_, c_l = divmod(n, 8)
                print(f"data is ({index_}, {c_l}, n is {n})")
                self.namemodel.setItem(index_, c_l, item_)
                print(data[n], "is ok")
        except Exception as e:
            print(e)




    def contextMenuEvent1(self, e):
        print("nbbbbbb")
        cmenu = QMenu(self.tableView_txcx_2)
        act1 = cmenu.addAction("查询关联表当前时间数据")
        act2 = cmenu.addAction("大小号姓名互相查询")
        act3 = cmenu.addAction("查询关联表的数据")
        if hasattr(self, "data_phone"):
            data = self.data_phone

        action = cmenu.exec_(self.page_txcx_2.mapToGlobal(e))
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        row = self.tableView_txcx_2.selectionModel().selection().indexes()
        for x in row:
            x_pos = x.row()
            y_pos = x.column()
        if action == act1:
            print(x_pos)
            print(y_pos)
            print(data.iloc[x_pos, y_pos])
        elif action == act2:
            print(f"im the act2")
        elif action == act3:
            print(f"im the act3")
        else:
            print(f"something is wrong")

        # cmenu.exec_()

def run():
    xx = QWidget()
    menu_ = query_()
    menu_.setupUi(xx)
    return xx

def run3(QWidget_):
    menu_ = query_()
    menu_.setupUi(QWidget_)
    return menu_



def run2():
    app_ = QApplication(sys.argv)
    xx = QWidget()
    menu_ = query_()
    menu_.setupUi(xx)

    xx.show()

    sys.exit(app_.exec_())



if __name__ == "__main__":
    run2()