# -*- coding:utf-8 -*-
'''
Created on 2018年5月17日

@author: zc
'''
import socket
import threading

serverIp = "127.0.0.1"
serverPort = 12345

class Server(object):
  
    def __init__(self):
      self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      address = (serverIp,serverPort)
      self.socket.bind(address)
      
    def start(self):
      self.socket.listen(10)
      print('Waiting for connection...')
      while True :
        connect,addr = self.socket.accept()
        t = threading.Thread(target=self.tcplink, args=(connect, addr))
        t.start()
        

    def tcplink(self,connect, addr):
      print('Accept new connection from %s:%s...' % addr)
      connect.send(b'welcome')
      while True:
        data = connect.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
          break
        print(data.decode('utf-8'))
        connect.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
      connect.close()
      print('Connection from %s:%s closed.' % addr)
      
      
if __name__ == '__main__':
    server1 = Server()
    server1.start()
    
    
    
    
    
    
    
    
    
    
    
      
      