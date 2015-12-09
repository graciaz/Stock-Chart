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

def mean(close_list):
    """find and return mean from data"""
    return statistics.mean(close_list)

def median(close_list):
    """find and return median from data"""
    return statistics.median(close_list)

def stand_div(close_list):
    """find and return standard deviation from data"""
    return statistics.stdev(close_list)

def mode(close_list):
    """find and return mode from data"""
    return max(set(close_list), key=close_list.count)

def main(stock, inte=0):
    """Print Ploted graph and statistics"""
    now, stock, open_value, now_price, import_time, stock_db = get_database(stock)
    date_dic, close_dic  = {}, {}
    date_list, close_list = [], []
    for dict_count in stock_db:
        for keys_count in dict_count.keys():
            if keys_count.upper() == 'CLOSE':
                close_dic.setdefault(inte, dict_count[keys_count])
            elif keys_count.upper() == 'DATE':
                date_dic.setdefault(inte, dict_count[keys_count])
        inte += 1
    count = 0
    for i in range(inte-1, -1, -1):
        date_list.append(date_dic[i])
        close_list.append(close_dic[i])
        count += 1
    pylab.figure(1)
    x = range(len(close_list))
    pylab.xticks(x, date_list)
    pylab.plot(x,close_list,"g")
    pylab.show()
    for inte in range(len(close_list)):
        close_list[inte] = float(close_list[inte])
    print("Mean :", mean(close_list))
    print("Median :", median(close_list))
    print("SD :", stand_div(close_list))
    print("Mode :", mode(close_list))

main(input("Input Stock name : "))
