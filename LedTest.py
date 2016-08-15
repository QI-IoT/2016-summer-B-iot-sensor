from neo import Gpio
import time
import datetime
#neo as  GPIO CLASS 
gpio = Gpio()


pin = 0

print "Time : time.ctime() result -"
print time.ctime()

print "datetime : datetime.datetime.now() -"
print datetime.datetime.now().strftime('%Y.%m.%d. %H.%M.%S')


