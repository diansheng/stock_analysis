import urllib2, os, datetime
from dateutil.relativedelta import relativedelta
import traceback

url_template = '''http://real-chart.finance.yahoo.com/table.csv?\
s=%(ticker)s&\
d=%(d)s&\
e=%(e)s&\
f=%(f)s&\
g=d&\
a=%(a)s&\
b=%(b)s&\
c=%(c)s&\
ignore=.csv'''

filename_template = '%(ticker)s-%(start)s-%(end)s.csv'

url_param = {
    'ticker': '5PL.SI',
    'a': '03',
    'b': '01',
    'c': '2010',
    'd': '02',
    'e': '01',
    'f': '2016',
}

tickers = [
    '%5ESTI', '5PL.SI', '5TS.SI', 'T19.SI', 'B2F.SI',
    'D05.SI', 'O39.SI', 'E5H.SI', '5CP.SI', 'ACW.SI',
    'F03.SI', '5HJ.SI', 'O05.SI', 'Z74.SI', 'N21.SI',
    '5GB.SI', '5WA.SI', 'BN4.SI', '5OU.SI', 'NR7.SI',
    'B0Z.SI', 'H78.SI', 'OV8.SI',
]

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2015, 12, 31)


class Data(object):
    def __init__(self):
        self.url_param = url_param
        self.start = datetime.date(2010, 1, 1)
        self.end = datetime.date(2015, 12, 31)
        self.ticker = '%5ESIT'
        self.url=''

    def get_url_param(self):
        one_month = relativedelta(months=1)
        new_start = self.start - one_month
        new_end = self.end - one_month
        param = {
            'ticker': self.ticker,
            'a': new_start.month,
            'b': new_start.day,
            'c': new_start.year,
            'd': new_end.month,
            'e': new_end.day,
            'f': new_end.year,
        }
        return param

    def get_url(self, param=None):
        if param is None:
            param = self.get_url_param()
        url = url_template % param
        return url

    def get_data(self, url=None, directory='data', filename=None, ):
        if url is None:
            url = self.get_url()
        if filename is None:
            filename = filename_template % {'ticker': self.ticker, 'start': self.start.strftime('%Y%m%d'),
                                            'end': self.end.strftime('%Y%m%d')}
        print 'url:', url
        print 'directory:', directory
        print 'filename:', filename
        with open(os.path.join(directory, filename), "wb") as f:
            u = urllib2.urlopen(url)
            f.write(u.read())
        print 'data saved'

    # don't use it, because the data is not huge
    def download(url, filename=None):
        if filename is None:
            file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8) * (len(status) + 1)
            print status,

        f.close()


if __name__ == '__main__':
    d = Data()
    for t in tickers:
        d.ticker = t
        try:
            d.get_data()
        except Exception, e:
            print e
            traceback.print_exc()
