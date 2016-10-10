class ShowRecordController:
    def __init__(self, recordFactory, showRecordView):
        self.recordFactory = recordFactory
        self.showRecordView = showRecordView
        self.showRecordView.setController(self)

    def startShowRecord(self, start):
        self.recordFactory.startShowRecord(start)
