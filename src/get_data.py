import urllib2, os

url_template = '''http://real-chart.finance.yahoo.com/table.csv?g=d&ignore=.csv&\
s=%(ticker)s&\
a=%(start month - 1)s&\
b=%(start day)s&\
c=%(start year)s&\
d=%(end month - 1)s&\
e=%(end day)s&\
f=%(end year)s'''

url_param = {
    'ticker': '5PL.SI',
    'end month - 1': '03',
    'end day': '01',
    'end year': '2016',
    'start month - 1': '02',
    'start day': '01',
    'start year': '2010',
}


def get_url(**kwargs):
    global url_param
    url_param.update(**kwargs)
    url = url_template % url_param
    print 'get url:', url
    return url


def save_data(url=None, directory='data', filename=None, **kwargs):
    if url is None:
        url = get_url(**kwargs)
    if filename is None:
        filename = '''%(ticker)s-\
%(start year)s%(start month - 1)s%(start day)s-\
%(end year)s%(end month - 1)s%(end day)s.csv''' % url_param
    print 'url:', url
    print 'directory:', directory
    print 'filename:', filename
    with open(os.path.join(directory, filename), "wb") as f:
        u = urllib2.urlopen(url)
        f.write(u.read())
    print 'data saved'


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
    # get_url()
    save_data()
