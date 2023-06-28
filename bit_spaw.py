import asyncio
from functools import partial
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import by
import pandas
from time import time
get_url_time = 10
scan_time_delta = 5
task_que = asyncio.LifoQueue()
asyncio_pool_number = 5
webdriver_que_product = asyncio.queues.Queue(asyncio_pool_number)

async def parse(browser, name):
    old_cny = 0
    old_dola = 0
    basic_data = pandas.DataFrame([], index=["name", "trade_count", "price_dollar", "price_cny", "time_"])
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
            new_data = {"name": name, "trade_count": count_data, "price_dollar": data2, "price_cny": data, "time_": time()}
            # print("process _data", new_data)
            basic_data = basic_data.append(new_data, ignore_index=True)
            print("data number is ", len(basic_data))
        except Exception as e:
            print(e)
        basic_data.drop_duplicates(inplace=True)
        basic_data.drop_duplicates(inplace=True)
        basic_data.dropna(inplace=True, how="all")
        if len(basic_data) > 100:
            print("writting data begin1")
            try:
                with open(r"D:\machine\机器端\base_data.csv", "a") as add_da:
                    print("writting data begin2")
                    (basic_data.iloc[0:100]).to_csv(add_da, index=False, columns=None, header=False)
                    print("writting data begin3")
                basic_data.drop(index=range(100), inplace=True)
            except Exception as ef:
                print("writting data is failed ", ef)

            return True



def open_url():
    webdriver_list = []
    for datan in range(asyncio_pool_number):
        print(datan)
        browser = webdriver.Firefox()
        webdriver_list.append(browser)
    return webdriver_list

async def parse_url(webdriver_que_product, name, url):
    browser = None
    while True:
        if browser is None:
            browser = await webdriver_que_product.get()
            print("im in parse {}".format(browser), name)
            parse_owner = parse(browser, name)
        try:
            browser.get(url=url)
            print(url)
            wwait = WebDriverWait(browser, 15)
            wwait.until(ec.presence_of_element_located((by.By.XPATH, "//div[@class='ticker']/dl[4]/dd")))
            print("i have geted url ")
            # browser.wait
        except Exception as e:
            print("im get url , im wrong ", e)

        print("im in parse2, ")
        try:
            parse_result = await parse_owner
            print("parse url is ok back data is ", parse_result)
        except Exception as ee:
            parse_result = False
            print("parse data is wrong, ", ee)
            print("parse data is wrong, ", ee)
        if parse_result:
            print("parse {}  ok".format(name))
        await webdriver_que_product.put(browser)
        await asyncio.sleep(0.5)
        browser = None


url_table = pandas.read_csv(r"D:\machine\机器端\bit_name_href_.csv", header=0, index_col="name")

def call_back_task(webdriver_list, future):
    for web_driver in webdriver_list:
        pass
        # web_driver.close()

async def main_(webdriver_list):
    open_list = []
    open_list_que = asyncio.Queue()
    for webdriver_ in webdriver_list:
        await open_list_que.put(webdriver_)
    task_index = 0
    for name in url_table.index.values:
        print("task index is {}".format(task_index))
        url = url_table.loc[name].values[0]
        task = asyncio.ensure_future(parse_url(open_list_que, name, url))
        open_list.append(task)
        task_index = task_index + 1
    # tasks_result = await asyncio.gather(*open_list, return_exceptions=False)
    done, pendding = await asyncio.wait(open_list)
    print(done)
    print(pendding)
    # tasks_result.add_done_callback(partial(call_back_task, webdriver_list))
    return done
    # loop_.run_until_complete(tasks)


def run_loop():
    webdriver_list = open_url()
    loop_ = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main_(webdriver_list))
    main_task.add_done_callback(partial(call_back_task, webdriver_list))
    tasks_result = loop_.run_until_complete(main_task)
    print(tasks_result)

def run_loop2():
    webdriver_list = open_url()
    loop_ = asyncio.get_event_loop()
    loop_.create_task(main_(webdriver_list))
    loop_.run_forever()






if __name__ == "__main__":

    # run_loop()
    run_loop2()