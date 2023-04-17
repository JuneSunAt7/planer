import os
import csv
from PyQt5 import QtWidgets  # for message about errors


def read_curr():

    with open('tasks.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['task'], row['deadline'], row['diff'], row['resources'])


def read_fired():
    pass


def rm_to_fired():
    pass


def rm_to_archive():
    pass


def delete():
    pass

def rm_all():
    pass



