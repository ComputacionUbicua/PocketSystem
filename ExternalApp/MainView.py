from encodings.punycode import selective_find

from builtins import print

from dialog1 import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import (QAreaSeries, QBarSet, QChart, QChartView,
        QLineSeries, QPieSeries, QScatterSeries, QSplineSeries,
        QStackedBarSeries)
import configureView
import socket               # Import socket module



class MainView(QWidget, Ui_Dialog):
	
    def __init__(self):
        super().__init__()
        Ui_Dialog.setupUi(self,self)
        self.pushButton_3.clicked.connect(self.showRecords)
        self.pushButton.clicked.connect(self.start)
        self.recive = False
        self.s = socket.socket()         # Create a socket object
        self.c = socket.socket()         # Create a socket object
        host = "192.168.1.40"       # Get local machine name
        port = 12345                # Reserve a port for your serv
        host = ""       # Get local machine nameice.
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.pushButton_3.setDisabled(True)
        self.pushButton.setText("Stop")
        try:
            self.s.bind(("", port))        # Bind to the port
        except:
            print("error")

        # self.s.listen(5)                 # Now wait for client connection.

    def __del__(self):
        self.s.close()

    def showConfiguration(self):
        self.hide()
        self.conf = configureView.configureView(self)
        self.conf.setMain(self)
        self.conf.show()

    def showRecords(self):
        self.w = QWidget()
        self.w.show()
        self.hide()
        self.gridLayout = QtWidgets.QVBoxLayout(self.w)
        self.text = QtWidgets.QLabel(self.w)
        self.chart = QChart()
        self.chart2 = QChart()
        self.chart3 = QChart()
        self.text.setText("none")
        self.backButton = QtWidgets.QPushButton(self.w)
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        # self.chartView2.setRenderHint(QtGui.QPainter.Antialiasing)
        # self.chartView3.setRenderHint(QtGui.QPainter.Antialiasing)
        self.gridLayout.addWidget(self.chartView)
        # self.gridLayout.addWidget(self.chartView3)
        self.backButton.setText("Back")
        self.gridLayout.addWidget(self.backButton)
        self.backButton.clicked.connect(self.back)
        self.recive = True
        # self.series2 = QLineSeries(self.chart2)
        # self.series3 = QLineSeries(self.chart3)
        self.series = QLineSeries(self.chart)
        self.series2 = QLineSeries(self.chart)
        self.series3 = QLineSeries(self.chart)
        # self.series2.setUseOpenGL(True)
        # self.series3.setUseOpenGL(True)
        self.series.setUseOpenGL(True)
        self.series2.setUseOpenGL(True)
        self.series3.setUseOpenGL(True)
        # self.chart.addSeries(self.series)
        self.startServer()

    def createLineChart(self, dataTable):
        self.chart.setTitle("Sensor1")
        series = QLineSeries(self.chart)
        series2 = QLineSeries(self.chart)
        series3 = QLineSeries(self.chart)
        # series2 = QLineSeries(self.chart)
        # series3 = QLineSeries(self.chart)
        series.setUseOpenGL(True)
        series2.setUseOpenGL(True)
        series3.setUseOpenGL(True)
        # series2.setUseOpenGL(True)
        # series3.setUseOpenGL(True)

        series.replace(self.series.pointsVector())
        series2.replace(self.series2.pointsVector())
        series3.replace(self.series3.pointsVector())
        # series2.replace(self.series2.pointsVector())
        # series3.replace(self.series2.pointsVector())
        self.chart.removeAllSeries()
        self.chart.addSeries(series2)
        self.chart.addSeries(series)
        self.chart.addSeries(series3)
        # self.chart2.removeAllSeries()
        # self.chart2.addSeries(series2)
        # self.chart3.removeAllSeries()
        # self.chart3.addSeries(series3)
        # self.chart.scroll(1,2)

    def startServer(self):
        # Establish connection with client.
        a = []
        QApplication.processEvents()
        self.c.connect(("192.168.1.41", 12346))
        self.c.send(b'RecordView True')
        print("connected")
        index = 0
        while self.recive:

            QApplication.processEvents()         # c, addr = self.s.accept()
            message, adre = self.s.recvfrom(1024)
            # print(message)
            values = message.decode("utf-8").split("-")
            value1 = int(values[0])
            value2 = int(values[1])
            value3 = int(values[2])
            self.series.append(index, value1)
            self.series2.append(index, value2)
            self.series3.append(index, value3)
            # self.series2.append(index, int(message.decode("utf-8")))
            # self.series3.append(index, int(message.decode("utf-8")))
            if self.series.count() > 100:
                self.series.removePoints(0,1)
                self.series2.removePoints(0,1)
                self.series3.removePoints(0,1)
                # self.series2.removePoints(0,1)
                # self.series3.removePoints(0,1)
            index += 1
            a.append(message.decode("utf-8"))
            self.createLineChart(a)
        self.c.connect(("192.168.1.41", 12346))
        self.c.send(b'RecordView False')

    def back(self):
        self.w.hide()
        self.show()
        self.recive = False

    def configure(self, arguments):
        print(arguments)
        self.c.connect(("192.168.1.41", 12346))
        self.c.send(b'Sensor ' + arguments)


    def start(self):
        self.c.connect(("192.168.1.41", 12346))
        if self.pushButton.text() == "Start" :
            text = "Stop"
            self.pushButton_3.setEnabled(False)
            self.c.send(b'Record False')
        else:
            text = "Start"
            self.pushButton_3.setEnabled(True)
            self.c.send(b'Record True')

        self.recive = self.pushButton.text() == "Start"
        self.pushButton.setText(text)

a = QApplication([])
m = MainView()
m.show()
sys.exit(a.exec_())
