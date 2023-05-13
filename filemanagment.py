import os
import csv
from PyQt5 import QtWidgets  # for message about errors
import datetime

def read_curr():
    s = ''
    with open('CURR.csv', newline='') as csvfile:
        for line in csvfile:
            columns = line.split(';')
            s += columns[0] + '.' +columns[1]+'.'+columns[2]+'.'+columns[3]
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse


def read_fired():
    s = ''
    with open('FIRE.csv', newline='') as csvfile:
        for line in csvfile:
            columns = line.split(';')
            s += columns[0] + '.' + columns[1] + '.' + columns[2] + '.' + columns[3]
            print(s)

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')
    print(parse)

    return parse


def read_arc():
    s = ''
    with open('ARC.csv', newline='') as csvfile:
        for line in csvfile:
            columns = line.split(',')
            s += str(columns[0] + ' ' + columns[1] + ' ' + columns[2] + ' ' + columns[3]).replace('"', '')
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')
    parse.pop(0)
    print(parse)

    return parse


def m_to_fired():
    with open('FIRE.csv', 'r') as fire:
        check_line = fire.read().replace("\n", '')

    with open('CURR.csv', 'r') as source, open('FIRE.csv', 'a') as destination:
        for line in source:
            columns = line.split(';')
            curr_date = datetime.date.today()
            date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
            if (date_object - curr_date).days <= 3:
                if (date_object - curr_date).days > 0:
                    if check_line != line.replace("\n", ''):
                        destination.write(line)

def m_to_archive():
    pass


def wr_to_main_file(taskname, deadline, diff, resources):
    data = taskname+';'+ deadline+';'+ diff+';'+ str(resources)

    with open('CURR.csv', 'a') as file:
        file.write('\n'+data)


def delete():
    pass


def rm_all():
    pass



