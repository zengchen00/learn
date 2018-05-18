# -*- coding:utf-8 -*-
'''
Created on 2018年5月18日

@author: zc
'''
import socket
import threading

def server():
  socketSever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  socketSever.bind(('127.0.0.1',9999))
  socketSever.listen(10)
  print('开始监听')
  while True :
    clientSocket,addr = socketSever.accept()
    print('监听到了 连接：%s,%s' % addr)
    #新启动一个线程处理这个socket
    t = threading.Thread(target=handleData,args=(clientSocket,))
    t.start()
    
def handleData(clientSocket):
  dataBuffer = b''
  while True:
    data = clientSocket.recv(1)
    if not data :
      print(dataBuffer.decode('utf-8'))
      break
    dataBuffer = dataBuffer + data
#   for i in range(10):
#     clientSocket.send(("我是话痨吗?" + str(i)).encode(encoding='utf_8', errors='strict'))
  clientSocket.close()
  
if __name__ == '__main__':
    server()
    
    
    