from datetime import date
import numpy


class Account(object):
    stock_held = ()
    num_stock = len(stock_held)
    cash = 0
    current_date = date.today()
    trade_history = {}  # date:tuple(trade,price)
    monthly_invest_starting = 0
    monthly_invest_increment = 0.1

    long_term_average = numpy.array()
    short_term_average = numpy.array()
    diff_to_buy = 0.05
    diff_to_sell = 0.1

    def operate_day(self):
        day_trade_arr = numpy.array(self.num_stock)
        day_price_arr = numpy.array(self.num_stock)
        # todo
        return day_trade_arr, day_price_arr

    def monthly_deposit(self):
        # todo
        pass

    def run(self):
        # todo
        pass

