from PyQt5.QtWidgets import QMainWindow, QApplication
import mainwindow_clinet
import sys
import socket
import threading

class Client(QMainWindow, mainwindow_clinet.Ui_MainWindow):
    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.PushButton_Send.clicked.connect(self.sendThreadFunc)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.PushButton_Login.clicked.connect(self.send)#22

    def sendThreadFunc(self):
        try:
            myword = self.lineEdit.text()
            if myword != "":
                self.sock.send(myword.encode())
                myword = myword.rjust(40)+" :You"
                self.textBrowser.append(myword)
                self.textBrowser.update()
                self.lineEdit.setText("")
        except ConnectionAbortedError:
            self.textBrowser.append('Server closed this connection!')
            self.textBrowser.update()
        except ConnectionResetError:
            self.textBrowser.append('Server is closed!')
            self.textBrowser.update()

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                self.textBrowser.append(otherword.decode())
                self.textBrowser.update()
            except ConnectionAbortedError:
                self.textBrowser.append('Server closed this connection!')
            except ConnectionResetError:
                self.textBrowser.append('Server is closed!')


    def send(self):#11
        name = self.lineEdit_Name.text()#222
        self.sock.send(name.encode())
        self.textBrowser.update()#222
        self.lineEdit_Name.setText("")#222
        th2 = threading.Thread(target=self.recvThreadFunc)
        th2.setDaemon(True)
        th2.start()

def main():
    c = Client('localhost', 5550)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Client('localhost', 5550)
    MainWindow.show()
    sys.exit(app.exec_())
    main()
