
import pylab

def stockgraph(stock):
    """"""
    now, stock, open_value, now_price, import_time, stock_db = get_database(stock)
    closdic = {}
    datdic = {}
    datlis = []
    closlis = []
    inte = 0
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

