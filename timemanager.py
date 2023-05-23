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


def readig_and_colour():
    s = ''
    with open('stat.pj', 'r', encoding='utf-8') as data:
        for line in data:
            columns = line.split(';')
            if columns == ['\r\n']:
                pass
            else:
                s += columns[0]
                print(s)

def statistics():
    pass


def computer_time():
    pass
