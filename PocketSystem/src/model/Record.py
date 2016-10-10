# -*- coding: utf-8 -*-
import time

class Record():

    def __init__(self):
        self.values = []
        self.recording = False
        self.portNumber = 1

    def addValue(self, value):
        self.values.append([time.time(), value])

    def getValues(self):
        return self.values

    def startStopRecord(self, start):
        self.recording = start

    def isRecording(self):
        return self.recording