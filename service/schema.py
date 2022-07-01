import re
from datetime import date
from typing import List

from pydantic import BaseModel, root_validator, validator


class PersonScheme(BaseModel):
    num: str
    surname: str
    firstname: str
    bdate: str

    @root_validator
    def check_non_nullable_fields(cls, values):
        for value in values:
            if len(values.get(value)) == 0:
                raise ValueError("Поля не могут быть пустыми")
        return values


class FlightBase(BaseModel):
    flt: int
    dep: str


class FileDataSceme(FlightBase):
    dt: date

    @validator('dt')
    def check_date_isnt_future(cls, value):
        if date.today() < value:
            raise ValueError('Проверьте дату')
        return value

    # закомментил, чтобы отслеживать другие файлы
    # В них вместо dep написана проблема
    # @validator('dep')
    # def check_dep_is_iata(cls, value):
    #     if not re.match(r'\w{3}', value):
    #         raise ValueError('Проверьте код аэропорта')
    #     return value


class FlightScheme(FlightBase):
    date: str
    prl: List[PersonScheme]


class FlightDBScheme(FlightBase):
    depdate: date
    file_name: str

    class Config:
        orm_mode = True
