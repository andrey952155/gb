class Date:

    def __init__(self, input_date):
        input_date = Date.transform_date(input_date)
        self.date = Date.check_date(input_date)

    def __str__(self):
        return f'Дата: {self.date}'

    @classmethod
    def transform_date(cls, input_date):
        return [int(i) for i in input_date.split('-')]

    @staticmethod
    def check_date(input_date):
        try:
            if not 0 < input_date[0] < 32 or not 0 < input_date[1] < 13 or input_date[2] // 10000 != 0:
                raise ValueError
        except ValueError:
            print('Неправильно ввели дату!')
        else:
            return f'{input_date[0]}-{input_date[1]}-{input_date[2]}'


dt = Date('1-10-2022')
print(dt)
error_day = Date('50-10-2022')
error_month = Date('1-50-2022')
error_year = Date('1-10-20223000')
