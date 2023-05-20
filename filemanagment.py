import os
import csv
from PyQt5 import QtWidgets  # for message about errors
import datetime
import re
import pandas as pd


def read_curr():
    s = ''
    if int(os.stat('CURR.csv').st_size) == 0:
        return 'data.2023-01-01.not.found('
    with open('CURR.csv', newline='', encoding='utf-8') as csvfile:
        for line in csvfile:
            columns = line.split(';')
            s += columns[0] + '.' +columns[1]+'.'+columns[2]+'.'+columns[3]
            print(s)
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse


def read_fired():
    s = ''
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            curr_date = datetime.date.today()
            date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
            if (date_object - curr_date).days <= 4:
                if (date_object - curr_date).days > 0:
                    s += columns[0] + '.' + columns[1] + '.' + columns[2] + '.' + columns[3]
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse


def read_arc():
    s = ''
    with open('ARC.csv', newline='', encoding='utf-8') as csvfile:
        for line in csvfile:
            columns = line.split(';')
            s += str('Task: '+columns[0] + ' ' + columns[1] + ' ' + columns[2] + ' ' + columns[3]+ ' archived: ' + columns[4] + '\n').replace('"', '')
    print(s)

    return s

def m_to_archive():
    with open('CURR.csv', 'r', encoding='utf-8') as f:
        lines = f.read().split()
        print('lines')
        print(lines)
    s = ''
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            curr_date = datetime.date.today()
            date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
            if (date_object - curr_date).days < 0:
                s += columns[0] + '.' + columns[1] + '.' + columns[2] + '.' + columns[3]

                with open('ARC.csv', 'a+', encoding='utf-8') as arc:
                    arc.write(line + ';' + str(curr_date) + '\n')
                lines.remove(line.replace('\n', ''))

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')
    with open('CURR.csv', 'w', encoding='utf-8') as rewrite:
        for elem in lines:
            rewrite.write(elem)






def wr_to_main_file(taskname, deadline, diff, resources):
    data = taskname+';'+ deadline+';'+ diff+';'+ str(resources)

    with open('CURR.csv', 'a', encoding='utf-8') as file:
        file.write('\n'+data)

def week_tasks():
    s = ''
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            curr_date = datetime.date.today()
            date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
            if (date_object - curr_date).days <= 7:
                if (date_object - curr_date).days > 0:
                    s += columns[0] + '.' +columns[1]+'.'+columns[2]+'.'+columns[3]
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse

def delete():
    with open('ARC.csv', 'w', encoding='utf-8') as delMe:
        delMe.write('')


def rm_all():
    pass



