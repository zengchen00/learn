# -*- coding:utf-8 -*-
'''
Created on 2018年5月18日

@author: zc
'''
import socket

def cc():
  clientServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  clientServer.connect(('127.0.0.1',9999))
  clientServer.send("你好啊兄弟1你好啊兄弟二你好啊兄弟3你好啊兄弟4".encode(encoding='utf_8', errors='strict'))
#   clientServer.send("你好啊兄弟2".encode(encoding='utf_8', errors='strict'))
#   clientServer.send("你好啊兄弟3".encode(encoding='utf_8', errors='strict'))
#   clientServer.send("你好啊兄弟4".encode(encoding='utf_8', errors='strict'))
#   while True:
#     data = clientServer.recv(1024)
#     if not data:
#       break
#     print(data.decode('utf_8'))
  clientServer.close()

if __name__ == '__main__':
    cc()