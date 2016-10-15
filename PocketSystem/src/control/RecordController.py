# -*- coding: utf-8 -*-
import time
import Filter

class RecordController():

    def __init__(self, recordFactory, sensorView):
        self.recordFactory = recordFactory
        self.records = []
        self.frecuency = 30.0
        self.a = 0
        self.sensorView = sensorView
        print 1.0 / self.frecuency

    def stopRecord(self):
        print self.records

    def setFrecuency(self, frecuency):
        self.frecuency = frecuency


    def setView(self, view):
        self.showRecordView = view
        # self.showRecordView.setStarStopSignal(self.startStop)

    def startStop(self, isStart):
        self.recordFactory.startStopRecord(isStart)

    def record(self):
        if self.recordFactory.isRecording():
            self.b = time.time()
            if ((self.b - self.a) > 1.0 / self.frecuency):
                values = self.sensorView.getValues()
                self.recordFactory.getRecord(0).addValue(values)
                if self.recordFactory.isShowing():
                    self.showRecordView.show(values)
                self.a = time.time()
