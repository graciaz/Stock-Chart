import pylab
from yahoo_finance import Share
from datetime import date
import statistics
def get_database(stock):
    """Return stock database"""
    now = date.today()
    mystock = Share(stock)
    now_price = mystock.get_price() #ราคาปัจจุบัน
    import_time = mystock.get_trade_datetime() #เวลาที่ดึงฐานข้อมูล
    stock_db = mystock.get_historical("2015-01-01", now.isoformat()) #ฐานข้อมูลหุ้นตั้งแต่วันที่ 1 มกราคม 2558 ถึงปัจจุบัน
    return now, stock, now_price, import_time, stock_db

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

def futurerate(close_list):
    """Return predicted close rate."""
    latest_close = close_list[len(close_list)-1]
    higher = []
    lower = []
    for inte in range(len(close_list)-1, len(close_list)-14, -1):
        if close_list[inte] >= latest_close:
            higher.append(close_list[inte])
        else:
            lower.append(close_list[inte])
    if len(higher) > len(lower):
        future_close = "Will raise."
    elif len(higher) < len(lower):
        future_close = "Will fell."
    else:
        future_close = "Will balance."
    return future_close

def main(stock, inte=0):
    """Print Ploted graph and statistics"""
    now, stock, now_price, import_time, stock_db = get_database(stock)
    date_dic, close_dic  = {}, {}
    date_list, close_list = [], []
    for dict_count in stock_db:
        for keys_count in dict_count.keys():
            if keys_count.upper() == 'CLOSE':
                close_dic.setdefault(inte, dict_count[keys_count])
            elif keys_count.upper() == 'DATE':
                date_dic.setdefault(inte, dict_count[keys_count])
        inte += 1
    for i in range(inte-1, -1, -1):
        date_list.append(date_dic[i])
        close_list.append(close_dic[i])
    for inte in range(len(close_list)):
        close_list[inte] = float(close_list[inte])
    print("Mean :", mean(close_list))
    print("Median :", median(close_list))
    print("SD :", stand_div(close_list))
    print("Mode :", mode(close_list))
    print("Future Close Rate :", futurerate(close_list))
    pylab.figure(1)
    x = range(len(close_list))
    pylab.xticks(x, date_list)
    pylab.plot(x,close_list,"g")
    pylab.show()

main(input("Input Stock name : "))
