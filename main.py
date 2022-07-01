from pydantic import ValidationError
from sqlalchemy.orm import Session

from service.db import database_start, write_to_db
from service.file import (
    move_file_to_ok_folder, move_file_to_err_folder,
    get_csv_filenames_in_in_folder
)
from service.handler import (
    get_data_from_filename, get_persons_data_from_csv,
    write_output_data_to_json_file
)
from service.schema import FlightScheme, FlightDBScheme


def process_the_file(
        csv_path: str,
        session: Session
):
    try:
        flight_data = get_data_from_filename(csv_path)
        persons = get_persons_data_from_csv(csv_path)
        response = FlightScheme(
            flt=flight_data.flt, dep=flight_data.dep,
            date=flight_data.dt.isoformat(), prl=persons
        )
        write_output_data_to_json_file(data=response, csv_path=csv_path)
        data_for_db = FlightDBScheme(
            file_name=csv_path, flt=flight_data.flt, depdate=flight_data.dt,
            dep=flight_data.dep
        )
        write_to_db(session=session, data=data_for_db)
        move_file_to_ok_folder(csv_path)
    except ValidationError:
        move_file_to_err_folder(csv_path)


def main():
    session = database_start()
    while True:
        csv_files = get_csv_filenames_in_in_folder()
        if len(csv_files) == 0:
            continue
        process_the_file(csv_files[0], session)


if __name__ == '__main__':
    main()
