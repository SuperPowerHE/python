import time
import datetime
#from datetime import datetime
print('现在时间')

localtime_structTime=time.localtime()
localtime_str=time.strftime("%Y-%m-%d",localtime_structTime)
localtime_dateTime=datetime.datetime.strptime(localtime_str,"%Y-%m-%d")

print(type(localtime_dateTime))
print(localtime_dateTime)
