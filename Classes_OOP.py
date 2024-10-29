from datetime import date
from datetime import datetime
import calendar


class Publication:
    def __init__(self, name):
        self.name = name

    def write_into_file(self, record):
        with open("news.txt", "a") as f:
            f.write(f"{self.record}\n")


class News(Publication):
    def __init__(self, name):
        Publication.__init__(self, name=name)
        self.record = None

    def __populate_news(self):
        self.text = input("Write a news text: ")
        self.city = input("Write a city name: ")
        self.populate_day = date.today()

    def create_news(self):
        self.__populate_news()
        self.record = f'''{self.name}----------\n{self.text}\n{self.city}, {self.populate_day}\n'''
        return self.record


class PrivateAd(Publication):
    def __init__(self, name):
        Publication.__init__(self, name=name)
        self.record = None
        self.expiration_date = None

    def __input_text(self):
        self.text = input("Write a Privat Ad text: ")
        return self.text

    @property
    def __input_date(self):
        while self.expiration_date is None:
            try:
                exp_year = input("Write a expiration year: ")
                self.exp_year = int(exp_year)
                if datetime.now().year <= self.exp_year <= 3000:
                    while self.expiration_date is None:
                        try:
                            exp_month = input("Write a expiration month: ")
                            self.exp_month = int(exp_month)
                            if (self.exp_month in range(1, 13) and self.exp_year != datetime.now().year) or (self.exp_year == datetime.now().year and self.exp_month in range(datetime.now().month, 13)):
                                while self.expiration_date is None:
                                    try:
                                        exp_day = input("Write a expiration day: ")
                                        self.exp_day = int(exp_day)
                                        if datetime.now().year == self.exp_year and self.exp_month == datetime.now().month and self.exp_day in range(datetime.now().day, calendar.monthrange(self.exp_year, self.exp_month)[1] + 1):
                                            self.expiration_date = date(self.exp_year, self.exp_month, self.exp_day)
                                        elif self.exp_year == datetime.now().year and self.exp_month != 2 and self.exp_month in range(datetime.now().month + 1, 13) and self.exp_day in range(1, calendar.monthrange(self.exp_year, self.exp_month)[1] + 1):
                                            self.expiration_date = date(self.exp_year, self.exp_month, self.exp_day)
                                        elif datetime.now().year != self.exp_year and 2 != self.exp_month and self.exp_month in range(1, 13) and self.exp_day in range(1, calendar.monthrange(self.exp_year, self.exp_month)[1] + 1):
                                            self.expiration_date = date(self.exp_year, self.exp_month, self.exp_day)
                                        elif datetime.now().year != self.exp_year and self.exp_month == 2 and self.exp_day in range(1, 30) and calendar.isleap(self.exp_year):
                                            self.expiration_date = date(self.exp_year, self.exp_month, self.exp_day)
                                        elif datetime.now().year != self.exp_year and self.exp_month == 2 and self.exp_day in range(1, 29) and not calendar.isleap(self.exp_year):
                                            self.expiration_date = date(self.exp_year, self.exp_month, self.exp_day)
                                        else:
                                            print('You write a wrong day')
                                            self.expiration_date = None
                                    except:
                                        print('You write something wrong. Try one more time! Please check the date '
                                              'today.')
                                        self.expiration_date = None
                            else:
                                print('You write a wrong month')
                                self.expiration_date = None
                        except:
                            print('You should write a number. Try one more time!')
                            self.expiration_date = None
                else:
                    print('You write a wrong year. Year should be more or equal to current and not more then 3000')
                    self.expiration_date = None
            except:
                print('You should write a number. Try one more time!')
                self.expiration_date = None

        return self.expiration_date

    def __calculate_day_left(self):
        self.day_left = self.expiration_date - date.today()
        return self.day_left

    def create_privat_ad(self):
        self.record = f'''{self.name}----------\n{self.__input_text()}\nExpiration date: {self.__input_date}, Days left: {self.__calculate_day_left()}\n'''
        return self.record


class Report(Publication):
    def __init__(self, name):
        Publication.__init__(self, name=name)
        self.record = None
        self.text = None
        self.reporter = None
        self.rating = None

    def __populate_report(self):
        self.text = input("Write a report text: ")
        self.reporter = input("Write a reporter name: ")

    def __enter_rating(self):
        while self.rating is None:
            self.rating = input("Enter the importance rating of the report, where 1 is not important, 10 is the highest importance rating: ")
            try:
                self.rating = int(self.rating)
            except:
                print('Rating should be a number')
                self.rating == None
            if self.rating in range(1, 11):
                self.rating = str(self.rating) + '/10'
            else:
                self.rating = None
                print('You write a wrong rating. Please try one more time!')
        return self.rating

    def create_report(self):
        self.__populate_report()
        self.record = f'''{self.name}----------\n{self.text}\nReporter: {self.reporter}, Rating: {self.__enter_rating()}\n'''
        return self.record


def create_new_record():
    record_type = None
    while record_type is None:
        record_type = input('Write what you want to add:\n1 - News\n2 - Privat Ad\n3 - Report\n')
        if record_type == '1':
            print('You select to create a News.')
            news = News('News')
            record = news.create_news()
            news.write_into_file(record)
            one_more = input('Do you add something else Y/N: ')
            if one_more == 'Y' or one_more == 'y':
                record_type = None
            else:
                print('Program is finished')
        elif record_type == '2':
            print('You select to create a Privat Ad')
            privat_ad = PrivateAd('Privat Ad')
            record = privat_ad.create_privat_ad()
            privat_ad.write_into_file(record)
            one_more = input('Do you add something else Y/N: ')
            if one_more == 'Y' or one_more == 'y':
                record_type = None
        elif record_type == '3':
            print('You select to create a Report')
            report = Report('Report')
            record = report.create_report()
            report.write_into_file(record)
            one_more = input('Do you add something else Y/N: ')
            if one_more == 'Y' or one_more == 'y':
                record_type = None
            else:
                print('Program is finished')
        else:
            print('You select something wrong. Please, try one more time!')
            record_type = None


create_new_record()