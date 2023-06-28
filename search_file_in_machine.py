import asyncio
import aiohttp
asyncio.start_server()

import re
from bs4 import BeautifulSoup

url_g = ["https://www.0mag.net/!f3Er", "https://www.javlands.net/tw/label/9dey9x.html", "https://www.javlands.net/tw/star/rpj2er.html", "https://www.javlands.net/tw/v_newrelease.php"]
url = "https://www.0mag.net/!f3Er"
async def read_respond(url):
    print("im {}".format(url))
    async with aiohttp.ClientSession() as session:
       async with session.get(url) as r_respond:
            back_data = await r_respond.read()
            print(url)
            print(back_data)


target = []
def m_ain():
    for url__ in url_g:
        ex = asyncio.ensure_future(read_respond(url__))
        target.append(ex)


if __name__ == "__main__":

    m_ain()
    ww = asyncio.wait(target)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(ww)

# import asyncio
# from aiohttp import ClientSession
#
# tasks = []
# url = "https://www.baidu.com/{}"
#
#
# async def hello(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#             print(response)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(hello(url))

# import time
# import asyncio
# from aiohttp import ClientSession
#
# tasks = []
# url = "https://www.baidu.com/{}"
#
#
# async def hello(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#             print(response)
#             print('Hello World:%s' % time.time())
#
#
# def run():
#     for i in range(5):
#         task = asyncio.ensure_future(hello(url.format(i)))
#         tasks.append(task)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     run()
#     loop.run_until_complete(asyncio.wait(tasks))