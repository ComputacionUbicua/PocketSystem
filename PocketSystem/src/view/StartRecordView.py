import os


class StartRecordView:

    def __init__(self, controller):
        self.controller = controller
        os.system("echo 16 > /sys/class/gpio/export") #este gpio activa el envio de datos en el arduino

    def startRecord(self, start):
        os.system("echo out > /sys/class/gpio/gpio16/direction")
        if start:
            os.system("echo 1 > /sys/class/gpio/gpio16/value")
        else:
            os.system("echo 0 > /sys/class/gpio/gpio16/value")
        self.controller.startRecord(start)