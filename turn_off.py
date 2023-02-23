import os
import signal
import time
from library.log import logger

# Import only the modules for LCD communication
from library.lcd.lcd_comm import Orientation
from library.lcd.lcd_comm_rev_a import LcdCommRevA


def killProcess():
    f=open("main.pid","r")
    pid=f.readlines()
    f.close()
    pid=int(pid[0])
    logger.info("Killing stat monitor process " + str(pid))
    os.kill(pid, signal.SIGINT)

def killDisplay():
    lcd_comm = LcdCommRevA(com_port="AUTO",
                           display_width=480,
                           display_height=800)
    #lcd_comm.SetOrientation(orientation=Orientation.LANDSCAPE)
    #lcd_comm.Clear()
    lcd_comm.ScreenOff()


killProcess()
time.sleep(1)
killDisplay()