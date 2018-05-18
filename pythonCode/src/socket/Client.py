# -*- coding:utf-8 -*-
'''
Created on 2018年5月17日

@author: zc
'''
import socket

class Client(object):
  
    def __init__(self):
      self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      self.socket.connect(("127.0.0.1",12345))
      print(self.socket.recv(1024).decode('utf-8'))
      
    def send(self,message):
      self.socket.send(message)
      print(self.socket.recv(1024).decode('utf-8'))
      
    
    def close(self):
      self.socket.close()
      
if __name__ == '__main__':
  for i in range(10):
    client1 = Client()
    client1.send(('你好-'+ str(i)).encode(encoding='utf_8', errors='strict'))