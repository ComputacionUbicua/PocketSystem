# -*- coding: utf-8 -*-
import socket
import threading
from ShowRecordView import ShowRecordView
from StartRecordView import StartRecordView


class UdpView():

    def __init__(self):
        self.client = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)
        self.host = "192.168.1.40" #ip del external system
        self.port = 12345 #puerto del external system
        self.lost = False
        self.client.connect((self.host, self.port))
        self.s = socket.socket()         # Create a socket object
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(("192.168.1.41", 12346)) #nuestra ip y nuestro puerto
        self.thread = threading.Thread(target=self.listener)
        self.thread.start()

    def __del__(self):
        self.stop()

    def connect(self):
        try:
            self.client = socket.socket()
        except:
            print 'No connection'
            self.client.close()
            self.lost = True
        try:
            self.client.connect((self.host, self.port))
        except:
            print 'No connection2'
            self.client.close()
            self.lost = True

    def setCallBack(self, view):
        if view.__class__ == ShowRecordView:
            self.setShowing = view.startStop
        elif view.__class__ == StartRecordView:
            self.startStop = view.startRecord

    def send(self, message):
        try:
            self.client.send(str(message))
        except:
            # self.client.close()
            self.lost = True
            print 'Lost connection'

    def listener(self):
        self.work = True
        while self.work:
            data, addr = self.s.recvfrom(1024)
            if data.split(" ")[0] == "RecordView":
                self.setShowing(data.split(" ")[1] == "True")
            elif data.split(" ")[0] == "Record":
                self.startStop(data.split(" ")[1] == "True")
            elif data.split(" ")[0] == "Sensor":
                self.recordViewCallback(data.split(" ")[2], data.split(" ")[3], data.split(" ")[4])
        print "fin"

    def stop(self):
        self.work = False