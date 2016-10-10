# -*- coding: utf-8 -*-
from control.RecordController import RecordController
from model.RecordFactory import RecordFactory
from view.ConfigureSensorView import ConfigureSensorView
from view.SensorView import SensorView
from view.ShowRecordView import ShowRecordView
from control.Umbral import Umbral
from view.UdpServerView import UdpView
from view.SensorSerialView import SensorSerialView
from view.StartRecordView import StartRecordView
from control.StartRecordController import StartRecordController
from control.ShowRecordController import ShowRecordController

class main():

    def callback(self, data):
        print data
        if data == "stop":
            self.cont = False

    def __init__(self):

        udpView = UdpView()
        recordFactory = RecordFactory()
        showRecordView = ShowRecordView(udpView, recordFactory)
        startRecordController = StartRecordController(recordFactory)
        startRecordView = StartRecordView(startRecordController)
        udpView.setCallBack(startRecordView)
        # sensorView = SensorView()
        sensorView = SensorSerialView()
        recordFactory.createRecord()
        record = recordFactory.getRecord(0)

        recordController = RecordController(recordFactory, sensorView)
        recordController.setFilter(Umbral(100))
        recordController.setView(showRecordView)
        showRecordController = ShowRecordController(recordFactory, showRecordView)
        configureSensorView = ConfigureSensorView(recordController)
        udpView.setCallBack(configureSensorView)

        # server.start()
        self.cont = True
        while self.cont:
            recordController.record()
        recordController.stopRecord()

main()
