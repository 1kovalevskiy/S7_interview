import csv
import json
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
    """Вытаскивает информацию из названия файла, валидирует и упаковывает"""
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
    """Вытаскивает информацию из тела файла, валидирует и упаковывает"""
    persons = []
    with open(join(IN_PATH, csv_path), 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            try:
                bdate = datetime.strptime(row.get('bdate'), '%d%b%y').date()
            except TypeError:
                raise ValueError("не указан день рождения пассажира")
            persons.append(
                PersonScheme(
                    bdate=bdate.isoformat(), num=row.get('num'),
                    surname=row.get('surname'), firstname=row.get('firstname')
                )
            )
    return persons


@log("Информация записана в json")
def write_output_data_to_json_file(
        csv_path: str,
        data: FlightScheme
) -> None:
    """Записывает json в одну строку"""
    file_path = join(OUT_PATH, os.path.splitext(csv_path)[0] + '.json')
    is_exist = os.path.exists(OUT_PATH)
    if not is_exist:
        os.makedirs(OUT_PATH)
    with open(file_path, 'w') as j:
        j.write(data.json())


@log("Информация записана в json")
def write_pretty_output_data_to_json_file(
        csv_path: str,
        data: FlightScheme
) -> None:
    """Записывает json красиво и удобно для прочтения людьми"""
    file_path = join(OUT_PATH, os.path.splitext(csv_path)[0] + '.json')
    is_exist = os.path.exists(OUT_PATH)
    if not is_exist:
        os.makedirs(OUT_PATH)
    with open(file_path, 'w') as j:
        json_data = data.dict()
        json.dump(json_data, j, indent=4)
