from threading import Thread
import filemanagment
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import datestr2num, DateFormatter, DayLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.patches import Patch

def time_count(task):
    timer_start = datetime.datetime.now()
    with open('stat.pj', 'a+', encoding='utf-8') as timer:
        timer.write('\n'+str(task) + ';' + timer_start.strftime('%Y-%m-%d %H-%M')+';')


def timer_end(task):
    timer_start = datetime.datetime.now()
    with open("stat.pj", "r", encoding='utf-8') as f:
        data = f.readlines()

    def transformation(line):
        if task in line:
            line = line.replace('\n','') + timer_start.strftime('%Y-%m-%d %H-%M')+'\n'

        return line
    data = map(transformation, data)
    data = set(data)
    with open("stat.pj", "w", encoding='utf-8') as f:

        f.write(''.join(data))


def statistics():
    data = ''
    memory = []
    names = []
    with open('stat.pj', 'r', encoding='utf-8') as timer:
        for line in timer:
            columns = line.split(';')
            if columns == ['\n']:
                pass
            else:
                if len(columns) < 3:
                    pass
                else:
                    data += columns[0] + '.' + columns[1] + '.' +columns[2]

    data = data.replace("\n", ',')
    parse = data.strip('[]').replace("\r", "").split(',')


    for i in range(len(parse)):
        stat = parse[i].strip('[]').split('.')
        if stat == ['']:
            pass
        else:
            if stat[2] == '':
                pass
            else:
                tdelta = (datetime.datetime.strptime(stat[2], '%Y-%m-%d %H-%M') - datetime.datetime.strptime(stat[1], '%Y-%m-%d %H-%M')).seconds / 3600
                memory.append(tdelta)
                names.append(stat[0])

    plt.xlabel('Tasks')
    plt.ylabel('Hours')
    plt.bar(x=names, height=memory, color=['green'])
    plt.title('Statistics')
    plt.show()
def get_task():
    s = []
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            if columns == ['\n']:
                pass

            else:
                s.append(columns[0])

    return s


def get_time():
    s = []
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            if columns == ['\n']:
                pass
            else:
                s.append(columns[1])

    return s
def get_count_curr_time():
    s = []
    for i in range(len(get_time())):
        s.append(str(datetime.date.today()))
    return s
def gant_stat():
    tasks = get_task()
    start_dates = get_count_curr_time()
    end_dates = get_time()

    start_dates = [datestr2num(d) for d in start_dates]
    end_dates = [datestr2num(d) for d in end_dates]

    durations = [(end - start) for start, end in zip(start_dates, end_dates)]

    fig, ax = plt.subplots(figsize=(15, 8), facecolor='#4653b0')

    ax.set_facecolor('#4653b0')

    # Create colours for each task based on categories
    colors = ['#8adec0', '#ef5675', '#ffa600']
    task_colors = [colors[0]] * 3 + [colors[1]] * 4 + [colors[2]] * 3

    # Display the bars
    ax.barh(y=tasks, width=durations, left=start_dates,
            height=0.8, color=task_colors)

    ax.invert_yaxis()

    # Setup the x axis labels
    ax.set_xlim(start_dates[0], end_dates[-1])

    date_form = DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(date_form)

    ax.xaxis.set_major_locator(DayLocator(interval=10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.tick_params(axis='x', which='minor', length=2, color='white', labelsize=6)

    ax.get_yaxis().set_visible(False)

    # Control the colour of the grid for major and minor lines
    ax.grid(True, axis='x', linestyle='-', color='#FFFFFF', alpha=0.2, which='major')
    ax.grid(True, axis='x', linestyle='-', color='#FFFFFF', alpha=0.05, which='minor')
    ax.set_axisbelow(True)

    # Add labels for each task. For padding, we can use an f-string and add some extra space
    for i, task in enumerate(tasks):
        ax.text(start_dates[i], i, f'  {task}', ha='left', va='center', color='white', fontsize=12, fontweight='bold')

    # Add the current date line
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today_num = datestr2num(today)
    ax.axvline(today_num, color='red', alpha=0.8)

    # Style ticks, labels and colours
    ax.tick_params(axis='both', colors='white')

    ax.set_xlabel('Date', color='white', fontsize=12)
    ax.set_title('Gant diagram(today - deadline)', color='white', fontsize=14)

    # Hide spines so only bottom is visible
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


    plt.savefig('tg.png')


def computer_time():

    pass
