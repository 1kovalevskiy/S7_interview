import csv
import os
from datetime import datetime, date
from os.path import join
from typing import List

from service.const import IN_PATH, OUT_PATH
from service.logging import log
from service.schema import PersonScheme, FlightScheme, FileDataSceme


@log("Данные из названия файла получены")
def get_data_from_filename(
        csv_path: str
) -> (str, int, date):
    name_data = os.path.splitext(csv_path)[0].split('_')
    dep = name_data[2]
    flt = name_data[1]
    dt = datetime.strptime(name_data[0], '%Y%m%d').date()
    output = FileDataSceme(dep=dep, flt=flt, dt=dt)
    return output


@log("Информация из файла получена")
def get_persons_data_from_csv(
        csv_path: str
) -> List[PersonScheme]:
    persons = []
    with open(join(IN_PATH, csv_path), 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            persons.append(PersonScheme(**row))
    return persons


@log("Информация записана в json")
def write_output_data_to_json_file(
        csv_path: str,
        data: FlightScheme
) -> None:
    file_path = join(OUT_PATH, os.path.splitext(csv_path)[0] + '.json')
    with open(file_path, 'w') as j:
        j.write(data.json())
