import os
from os.path import join, isfile
from typing import List, Union

from service.const import IN_PATH, OK_PATH, ERR_PATH


def move_file_to_ok_folder(csv_path: str):
    os.replace(join(IN_PATH, csv_path), join(OK_PATH, csv_path))


def move_file_to_err_folder(csv_path: str):
    os.replace(join(IN_PATH, csv_path), join(ERR_PATH, csv_path))


def get_csv_filenames_in_in_folder() -> List[Union[str, None]]:
    csv_files = [f for f in os.listdir(IN_PATH) if isfile(join(IN_PATH, f))
                 and f.endswith('.csv')]
    return csv_files
