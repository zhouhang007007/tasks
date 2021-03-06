# -*- encoding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import mainwindow_server
import sys
import json

import urllib
from urllib.request import urlopen

import xlsxwriter as xlsxwriter
from bs4 import BeautifulSoup
import socket
import threading
import datetime

class Server(QMainWindow, mainwindow_server.Ui_MainWindow):
    def crawler(self, b):
        mainurl = 'https://www.fatsecret.cn/%E7%83%AD%E9%87%8F%E8%90%A5%E5%85%BB/search?q=%E7%89%9B%E8%82%89'
        mainurl = mainurl+b
        html_page = urlopen(mainurl)
        soup = BeautifulSoup(html_page,'html.parser')
        table = soup.find('table',attrs = {'class':'generic searchResult'})
        location = table.find_all('tr')
        loc = location[0].find('div',attrs = {'class':'smallText greyText greyLink'})
        act_date = loc.text.replace("\r\n",' ').replace("\t",'').replace('\u3000','').replace("     ",'')
        return act_date

    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.num_of_client = 0
        th2 = threading.Thread(target=self.checkConnection)
        th2.setDaemon(True)
        th2.start()

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                Username = connection.recv(1024).decode()
                welcome = 'welcome to chat room, ' + Username + '!\n'
                connection.send(welcome.encode())
                lets = 'Now Lets Chat ' + Username
                connection.send(lets.encode())
                self.tellOthers(connection.fileno(), 'SYSTEM: ' + Username + ' in the chat room')
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, Username, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
                self.num_of_client += 1
                print(self.num_of_client)
            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

    def subThreadIn(self, myconnection, myname, connNumber):
        self.mylist.append(myconnection)
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    x=datetime.datetime.now()
                    asn = urllib.parse.quote(recvedMsg)
                    asn =self.crawler(asn)
                    print(asn)
                    self.tellOthers(connNumber, myname + ": " + recvedMsg + "\t" + "[" + str(x.hour).zfill(2) + ":" + str(x.minute).zfill(2) + ":" + str(x.second).zfill(2) + "]")
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                    self.num_of_client -= 1
                    print(self.num_of_client)
                    self.tellOthers(connNumber, "[SYSTEM: "+myname+" leave the chat room]")
                except:
                    pass

                myconnection.close()
                return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Server('localhost', 5550)
    MainWindow.show()
    sys.exit(app.exec_())
