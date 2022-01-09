import time
import datetime
import jqdatasdk as jq
import numpy as np
#from datetime import datetime


localtime_structTime=time.localtime()
localtime_str=time.strftime("%Y-%m-%d",localtime_structTime)
localtime_DateTime=datetime.datetime.strptime(localtime_str,"%Y-%m-%d")

stock_pool=[
    '159915.XSHE', # 易方达创业板ETF
    '510300.XSHG', # 华泰柏瑞沪深300ETF
    '510500.XSHG', # 南方中证500ETF
]


def get_rank(stock_pool, day, time_DateTime):
    previous_date_DateTime=time_DateTime-datetime.timedelta(days=day)
    for stock in stock_pool:
        data = jq.get_price(stock, end_date = previous_date_DateTime, count = 1, frequency='daily', fields=['close'])
        print(data)
    return 0



#get_rank(stock_pool=stock_pool, day=4, time_DateTime=localtime_DateTime)

x=np.linspace(300,400,20)
y=x+np.random.randint(5,20,20)
data=np.polyfit(x,y,deg=1)
print(type(data))
print(data)
#print(intercept)