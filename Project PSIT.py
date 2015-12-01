from yahoo_finance import Share
from datetime import date
def get_database(stock):
	"""Return stock database"""
	now = date.today()
	mystock = Share(stock)
	open_value = mystock.get_open() #ราคาเปิดตัวหุ้น ณ วันนั้นๆ
	now_price = mystock.get_price() #ราคาปัจจุบัน
	import_time = mystock.get_trade_datetime() #เวลาที่ดึงฐานข้อมูล
	stock_db = mystock.get_historical("2015-01-01", now.isoformat()) #ฐานข้อมูลหุ้นตั้งแต่วันที่ 1 มกราคม 2558 ถึงปัจจุบัน
	return now, stock, open_value, now_price, import_time, stock_db

