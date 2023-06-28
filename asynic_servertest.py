import asyncio
import sys
import subprocess

print(sys.path)


from ws4py.server.tulipserver import *
from ws4py.async_websocket import WebSocket

loop = asyncio.get_event_loop()

class WsServer(WebSocket):
    clients = set()

    def opened(self):
        print("new connection...")
        self.clients.add(self)

    def received_message(self, m):
        print("send msg...")
        for client in self.clients:
            client.send(m)

    def closed(self, code, reason="Error"):
        print("connect close...")


def init_server(host, port):
    factory = lambda: WebSocketProtocol(WsServer)
    return loop.create_server(factory, host, port)


def main():
    ws_server = loop.run_until_complete(init_server('localhost', 9007))
    print('serving on', ws_server.sockets[0].getsockname())
    loop.run_forever()

if __name__ == '__main__':
    main()