import os
import csv
from PyQt5 import QtWidgets  # for message about errors


def read_curr():
    s = ''
    with open('file.csv', newline='') as csvfile:
        for line in csvfile:
            columns = line.split(',')
            s += str(columns[0]+' '+columns[1]+' '+columns[2]+' '+columns[3]).replace('"', '')
    s = s.replace("task deadline diff resources", '')
    parse = s.strip('[]').replace("\r\n", "").split(' ')
    print(parse)

    return parse


def read_fired():
    pass


def read_arc():
    pass


def m_to_fired():
    pass


def m_to_archive():
    pass


def wr_to_main_file():
    pass


def delete():
    pass


def rm_all():
    pass



