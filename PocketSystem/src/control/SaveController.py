import xlwt


class SaveController:

    def __init__(self, recordFactory,):
        self.recordFactory = recordFactory

    def save(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')
        records = self.recordFactory.getAllRecords()
        for record in records:
            values = record.getValues()
            for value in values:
                ws.write(value[0], value[1])

        wb.save('example.xls')
