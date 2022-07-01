import csv
from os import listdir
from os.path import isfile, join
from time import sleep

from const import IN_PATH


def handler(csv_path):

    with open(join(IN_PATH, csv_path), 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            print(row)
    sleep(2)



def main():
    while True:
        csv_files = [f for f in listdir(IN_PATH) if isfile(join(IN_PATH, f)) and f.endswith('.csv')]
        if len(csv_files) == 0:
            continue
        handler(csv_files[0])



    pass


if __name__ == '__main__':
    main()
