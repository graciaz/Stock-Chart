import pylab
from yahoo_finance import Share
from datetime import date
import statistics
def get_database(stock):
	"""Return stock database"""
	now = date.today()
	mystock = Share(stock)
	open_value = mystock.get_open() #ราคาเปิดตัวหุ้น ณ วันนั้นๆ
	now_price = mystock.get_price() #ราคาปัจจุบัน
	import_time = mystock.get_trade_datetime() #เวลาที่ดึงฐานข้อมูล
	stock_db = mystock.get_historical("2015-01-01", now.isoformat()) #ฐานข้อมูลหุ้นตั้งแต่วันที่ 1 มกราคม 2558 ถึงปัจจุบัน
	return now, stock, open_value, now_price, import_time, stock_db

def mean(data):
    """find and return mean from data"""
    return statistics.mean(data)

def median(data):
    """find and return median from data"""
    return statistics.median(data)

def stand_div(data):
    """find and return standard deviation from data"""
    return statistics.stdev(data)

def mode(data):
    """find and return mode from data"""
    return max(set(data), key=data.count)

def stockgraph(stock, inte=0):
    """Print Ploted graph"""
    now, stock, open_value, now_price, import_time, stock_db = get_database(stock)
    closdic, datdic = {}, {}
    datlis, closlis = [], []
    for dic in stock_db:
        for kii in dic.keys():
            if kii.upper() == 'CLOSE':
                closdic.setdefault(inte, dic[kii])
            elif kii.upper() == 'DATE':
                datdic.setdefault(inte, dic[kii])
        inte += 1
    count = 0
    for i in range(inte-1, -1, -1):
        datlis.append(datdic[i])
        closlis.append(closdic[i])
        count += 1
    #
    pylab.figure(1)
    x = range(len(closlis))
    pylab.xticks(x, datlis)
    pylab.plot(x,closlis,"g")
    pylab.show()
