#import python modules 
#time
#psutil
#plyer 

from email import message
from socket import timeout
import time
from numpy import percentile
import psutil
from plyer import notification

battery = psutil.sensors_battery()
percent = battery.percent

notification.notify(
    title = "battey percentage", message = str(percent)+" % battery remaining ", timeout = 20
)

