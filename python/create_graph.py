import pygal
import csv

def read_csv(obj, ex_type):
    """ get data from csv"""
    reader = csv.DictReader(obj, delimiter=',')
    date = "Series Description"
    tmp = dict()
    for line in reader:
        tmp[line[date]] = line[ex_type]
    """ screen data """
    count = 0
    data = dict()
    for i in tmp:
        count += 1
        if count > 5 and 2017 >= int(i[:4]) >= 1981:
            if tmp[i] != '':
                if tmp[i][0] != 'N':
                    if i[:4] in data:
                        data[i[:4]][0] += float(tmp[i])
                        data[i[:4]][1] += 1
                    else:
                        data[i[:4]] = [float(tmp[i]), 1]
    temp = list()
    for i in sorted(data):
        temp.append(float("%.4f" % (data[i][0]/data[i][1])))

    return temp

def call_reader(ex_type):
    """ call file and function reader """
    with open("../src/exchange_rates.csv") as obj:
        return read_csv(obj, ex_type)

def main():
    """ Render graph """
    ex_baht = call_reader("THAILAND -- SPOT EXCHANGE RATE, BAHT/US$ ")
    
    line_chart = pygal.StackedLine(fill=True, x_label_rotation=30)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(1981, 2018))
    line_chart.add('BAHT(฿)/US($)', ex_baht)
    line_chart.render_to_file('../tmp/chart.svg') 
    #line_chart.render_in_browser()

main()
