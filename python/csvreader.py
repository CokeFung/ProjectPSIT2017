""" CSV reader """
import csv
def csv_dict_reader(obj):
    reader = csv.DictReader(obj, delimiter=',')
    date = "Series Description"
    ex_type = "CHINA -- SPOT EXCHANGE RATE, YUAN/US$ P.R. "
    for line in reader:
        print(line[date], line[ex_type])

def main():
    with open("../src/exchange_rates.csv") as obj:
        csv_dict_reader(obj)
main()
