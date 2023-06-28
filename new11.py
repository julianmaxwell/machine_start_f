import asyncio
from selenium import webdriver
import pandas
from time import time as time_c
import signal
basic_data_columns = ["name", "trade_count", "price_dollar", "price_cny", "time_"]
basic_data = pandas.DataFrame([], columns=basic_data_columns)
url_table = pandas.read_csv("")
def open_browser(url, name):
    browser = webdriver.Firefox()
    try:
        browser.get(url=url)
        browser.rname = name
        return browser
    except:
        print("something wrong")
        return "something wrong"

url = "https://www.huobi.pe/zh-cn/cross-margin/btc_usdt"
etc_url = "https://www.huobi.pe/zh-cn/cross-margin/eth_usdt"
browser = open_browser(url, "btc")
browser_etc = open_browser(etc_url, "eth")
task_lst = ["btc", "eth", "ht", "dot", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", "btc", ]
print("***********************************")

async def read_data(browser, basic_data):
    old_cny = 0
    old_dola = 0

    while True:
        tt = browser.find_element_by_xpath("//span[@class='estimate']")
        tt2 = browser.find_element_by_xpath("//div[@class='price-container']")
        if tt.text != "---":
            if tt.text != "":
                data = float(tt.text.split()[1])
                if old_cny != data:
                    # print(data, type(data), "人民币价格 ", browser.rname)
                    old_cny = data
                else:
                    data = None
            else:
                data = None
        else:
            data = None
        tt3 = tt2.find_element_by_xpath("./span")
        if tt3.text != "---":
            if tt3.text != "":
                data2 = float(tt3.text)
                if data2 != old_dola:
                    # print(data2, type(data2), "美元价格 ",  browser.rname)
                    old_dola = data2
                else:
                    data2 = None
            else:
                data2 = None
        else:
            data2 = None
        try:
            current24_count = browser.find_element_by_xpath("//div[@class='ticker']/dl[4]/dd")
            count, type_ = current24_count.text.split()
            count_new = count.split(",")
            count_data = float("".join(count_new))
            # print("当前交易数量{}, 类型{}".format(count_data, type_))
        except:
            print("当前交易数量 未查询到")
            count_data = None
        try:

            new_data = {"name": browser.rname, "trade_count": count_data, "price_dollar": data2, "price_cny": data, "time_": time_c()}
            # print("process _data", new_data)
            basic_data = basic_data.append(new_data, ignore_index=True)
            print("data number is ", len(basic_data))
        except Exception as e:
            print(e)
        if len(basic_data) > 100:
            with open(r"E:\machine\机器端\base_data.csv", "a") as add_da:
                (basic_data.iloc[0:100]).to_csv(add_da, index=False, columns=None, header=False)
            basic_data.drop_duplicates(inplace=True)
            basic_data.drop(index=range(100), inplace=True)
        await asyncio.sleep(0)

import time
async def save_data(basic_data):
    while True:
        print("im in save", len(basic_data))
        if len(basic_data) > 100:
            (basic_data.iloc[0:100]).to_csv(r"E:\machine\机器端\base_data.csv", index=False, columns=None, header=False)
            print("write ok")
            time.sleep(5)
            basic_data.drop(index=range(100), inplace=True)
        await asyncio.sleep(0)

def loop_():
    loop_ = asyncio.get_event_loop()
    tt = asyncio.gather(read_data(browser, basic_data), read_data(browser_etc, basic_data))
    loop_.run_until_complete(tt)

if __name__ == "__main__":
    try:
        loop_()
    except Exception as e:
        print("e")
        browser.quit()
        browser_etc.quit()
        if len(basic_data) > 0 :
            basic_data.to_csv(index=False, columns=None, header=False)
