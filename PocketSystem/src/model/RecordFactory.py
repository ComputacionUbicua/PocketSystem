# -*- coding: utf-8 -*-
import time
from Record import Record


class RecordFactory:
    def __init__(self):
        self.values = []
        self.recording = False
        self.portNumber = 1
        self.record = []
        self.showing = False

    def createRecord(self):
        self.record.append(Record())

    def getRecord(self, index):
        return self.record[index]

    def startStopRecord(self, start):
        print start
        self.recording = start

    def isRecording(self):
        return self.recording

    def isShowing(self):
        return self.showing

    def startShowRecord(self, start):
        self.showing = start