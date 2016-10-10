import Filter


class Umbral(Filter.filter):
    def __init__(self, umbral):
        self.umbral = umbral
        self.minimo = 0

    def setMinimo(self, minimo):
        self.minimo = minimo

    def filterSignal(self,x):
        if x > self.umbral:
            return x
        else:
            return self.minimo