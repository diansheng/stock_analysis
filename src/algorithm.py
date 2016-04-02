from datetime import date
import numpy


class Account(object):
    # common variables
    stock_held = ()
    num_stock = len(stock_held)
    cash = 0
    current_date = date.today()
    trade_history = {}  # date:tuple(trade,price)
    monthly_invest_starting = 0
    monthly_invest_increment = 0.1

    # algorithm specific parameters
    long_term = 20
    short_term = 12
    long_term_average = numpy.array(long_term)
    short_term_average = numpy.array(short_term)
    diff_to_buy = 0.05
    diff_to_sell = 0.1
    trend_continue_days = 3
    
    def get_data(self, filename):
        return data
    
    last_30 = np.array()
    index_close = header.get_index('close')
    close_data = data[:,index_close]
    # init last 30
    last_30 = close_data[1:30,:]
    
    def calculate_term_average(self, term_length):
        sum_term = np.sum(close_data[1:term_length])
        term_average = np.array(long_term)
        for i in range(len(close_data)):
            if i < term_length -1:
                term_average[i]=0
            else:
                sum_term = sum_term - close_data[i-term_length] + close_data[i]
                term_average[i] = sum_term / term_length
        return term_average
    
    long_term_average = calculate_term_average(self.long_term)
    short_term_average = calculate_term_average(self.short_term)
    
    def day_decision(self, day):
        day_trade_arr = numpy.array(self.num_stock)
        day_price_arr = numpy.array(self.num_stock)
        # todo
        last_3_days = np.array(self.trend_continue_days)
        if self.long_term_average[day] > self.short_term_average[day] and
            
        return day_trade_arr, day_price_arr

    def monthly_deposit(self):
        # todo
        pass

    def run(self):
        # todo
        pass

