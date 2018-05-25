# -*- encoding: utf-8 -*-
import socket
import threading
import datetime
from time import gmtime, strftime




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
                connection.send(b'welcome to chat room!\n')
                connection.send(b'Input your nickname: ')
                Username = connection.recv(1024).decode()
                lets = 'Now Lets Chat ' + Username
                connection.send(lets.encode())
                self.tellOthers(connection.fileno(), 'SYSTEM: ' + Username + ' in the chat room')
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, Username, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
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
                    self.tellOthers(connNumber, myname + ": " + recvedMsg + "\t" + "[" + str(x.hour).zfill(2) + ":" + str(x.minute).zfill(2) + ":" + str(x.second).zfill(2) + "]")
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

