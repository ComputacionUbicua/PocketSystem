# -*- coding: utf-8 -*-
import os
import commands


class SensorView():

    def __init__(self):
        # self.gpios = (11, 12, 15, 16, 19, 21, 22, 37, 38, 40)
        self.gpios = (0, 1, 2, 3, 4, 5, 23, 24, 25, 28)
        self.valueGpio = []

    def getValue(self):
        self.getGpio()
        value = 0
        for i in range(0, len(self.valueGpio)):
            value += int(self.valueGpio[i]) * (2 ** i)
        return value

    def getGpio(self):
        self.valueGpio = []
        for i in range(0, len(self.gpios)):
            self.valueGpio.append(commands.getoutput('gpio read ' + str(self.gpios[i])))