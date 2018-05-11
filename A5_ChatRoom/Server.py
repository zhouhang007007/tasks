# -*- encoding: utf-8 -*-
import socket
import threading
import datetime
from time import gmtime, strftime


x=datetime.datetime.now()

class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.namelist = list()

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
                connection.send(b'welcome to chat room!')
                connection.send(b'Input your nickname: ')
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

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        i = 1
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if i:
                    self.namelist.append(recvedMsg)
                    lets = 'Now Lets Chat ' + recvedMsg
                    myconnection.send(lets.encode())
                    self.tellOthers(connNumber, 'SYSTEM: ' + recvedMsg + ' in the chat room')
                    i = 0
                else:
                    if recvedMsg:
                        self.tellOthers(connNumber, recvedMsg + "\t" + "[" + str(x.day) + ":" + str(x.hour) + ":" + str(x.minute) + "]")
                    else:
                        pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                except:
                    pass

                myconnection.close()
                return


def main():
    s = Server('localhost', 5550)
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

