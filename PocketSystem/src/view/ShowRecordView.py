import os


class ShowRecordView():

    def __init__(self, udp, recordFactory):
        self.udp = udp
        self.recordFactory = recordFactory
        self.udp.setCallBack(self)
        self.i = 0

    def show(self, x):
        try:
            self.udp.send(str(x[0]+"-"+x[1]+"-"+x[2]))
        except:
            pass

    def setController(self, controller):
        self.controller = controller

    def startStop(self, startStop):
        self.controller.startShowRecord(startStop)
