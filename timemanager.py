from threading import Thread
import main
import design
import filemanagment
import datetime
from datetime import timedelta


def time_count(task):
    timer_start = datetime.datetime.now()
    with open('stat.pj', 'a+', encoding='utf-8') as timer:
        timer.write('\n'+str(task) + ';' + timer_start.strftime('%Y-%m-%d %H-%M'))


def timer_end(task):
    pass


def statistics():
    pass


def computer_time():
    pass
