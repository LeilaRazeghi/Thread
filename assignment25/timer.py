import time
from PySide6.QtCore import *
from mytime import MyTime

class TimerThread(QThread):
    signal_show = Signal(MyTime)
    signal_time_finished =Signal()

    def __init__(self):
        super().__init__()
        self.time = MyTime(0,15,30)

    def run(self):
        while True:
            self.time.sub_second()
            time.sleep(1)
            self.signal_show.emit(self.time)

            #self.signal_time_finished.emit()
            if self.time.hour == 0 and self.time.min == 0 and self.time.sec == 0:
                self.signal_timer_finished.emit()
                break 

    def set_time(self,hour,min,sec):
        self.time.hour = hour
        self.time.min = min
        self.time.sec = sec
