from datetime import date
import numpy as np
import csv
import math


class Account(object):
    # common variables independent from algorithms
    tickers = ['ACW.SI', ]
    stock_held = {}  # a dict of ticker and number of shares
    num_stock = len(stock_held)
    cash = 0
    current_date = date.today()
    trade_history = {}  # date:tuple(trade,price)
    monthly_invest_starting = 1000
    monthly_invest_increment = 0.05

    # algorithm specific parameters
    long_term = 20
    short_term = 12
    long_term_average = np.array(long_term)
    short_term_average = np.array(short_term)
    diff_to_buy = 0.05
    diff_to_sell = 0.1
    trend_continue_days = 3
    num_share_base = 100

    def __init__(self):
        """
        initialize variables
        :return:
        """
        pass

    def _validate(self):
        """
        make sure the parameters are valid and reasonable
        :return:
        """
        assert self.trend_continue_days <= self.long_term

    def get_data_from_file(self, filename):
        with open(filename) as f:
            r = csv.reader(f)
            header = r[0]
            data = [d for d in r]
        return header, data

    def prepare(self):
        self.last_30 = np.array()
        index_close = header.get_index('close')
        self.data_close = data[:, index_close]
        # init last 30
        self.last_30 = self.data_close[1:30, :]

    def calculate_term_average(self, term_length):
        sum_term = np.sum(self.data_close[1:term_length])
        term_average = np.array(term_length)
        for i in range(len(self.data_close)):
            if i < term_length - 1:
                term_average[i] = 0
            else:
                sum_term = sum_term - self.data_close[i - term_length] + self.data_close[i]
                term_average[i] = sum_term / term_length
        return term_average

    long_term_average = calculate_term_average(long_term)
    short_term_average = calculate_term_average(short_term)

    def day_decision(self, day):
        day_trade_arr = []
        day_price_arr = np.array(self.num_stock)

        short_ave = self.short_term_average[day - self.trend_continue_days, day]
        long_ave = self.long_term_average[day - self.trend_continue_days, day]
        # todo
        for t in self.tickers:
            # buy in criteria
            match = True
            for i in range(self.trend_continue_days):
                if short_ave[i] / long_ave[i] > self.diff_to_buy + 1:
                    continue
                else:
                    match = False
                    break
            if match:
                num_share = self.adjust_num_share_to_buy(short_ave, long_ave)
                self.buy_or_sell(t, num_share, self.data_close[day])
            else:
                num_share = 0
            # sell criteria    todo

            day_trade_arr.append(num_share)

        return np.asarray(day_trade_arr), day_price_arr

    def adjust_num_share_to_buy(self, short_ave, long_ave):
        """
        adjust the amount to buy based on recent average price.
        basic idea: if the gap between short average and long average is increasing, buy more
        :param short_ave:
        :param long_ave:
        :return:
        """
        gap = short_ave/long_ave
        ratio = (gap[2]+gap[0])/2
        return self.num_share_base*ratio

    def adjust_num_share_to_sell(self, short_ave, long_ave):
        """
        adjust the amount to buy based on recent average price.
        basic idea: if the gap between short average and long average is increasing, sell more
        :param short_ave:
        :param long_ave:
        :return:
        """
        gap = short_ave/long_ave
        ratio = (gap[2]+gap[0])/2
        return self.num_share_base*ratio*ratio

    def buy_or_sell(self, ticker, num_share, price):
        """
        the process of buy or sell shares of a stock
        :param ticker: the ticker of the stock
        :param num_share: the number of shares to buy or sell. positive for buy in and negative for sell
        :param price: price of the day
        :return:
        """
        amount = num_share * price
        # buying but not enough cash
        if amount > 0 and self.cash < amount:
            amount = self.cash
            num_share = price
        # sell more than you have
        if self.stock_held[ticker] + num_share < 0:
            num_share = 0 - self.stock_held
            amount = num_share * price
        self.cash -= amount
        self.stock_held[ticker] += num_share

    def monthly_deposit(self, num_month):
        """
        regularly add money to cash account
        :param num_month:
        :return:
        """
        self.cash += self.monthly_invest_starting * math.pow((1 + self.monthly_invest_increment), num_month)

    def run(self):
        self.prepare()
        i = self.long_term + 1
        current_month = self.data[i, 1].get_month()
        num_month = 1
        # loop over every open day
        while i < len(self.data_close):
            # add cash every month
            if self.data_close[i, 1] is not current_month:
                num_month += 1
                self.monthly_deposit(num_month)
                current_month = self.data_close[i, 1]

            # make decision on the day
            self.day_decision(i)
            i += 1
