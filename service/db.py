from sqlalchemy import create_engine, Column, Integer, Date, Text
from sqlalchemy.orm import Session, declared_attr, declarative_base

from service.schema import FlightDBScheme


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Flight(Base):
    file_name = Column(Text)
    flt = Column(Integer)
    depdate = Column(Date)
    dep = Column(Text)

    def __repr__(self):
        return f'{self.flt} {self.dep} {self.depdate}'


def database_start():
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    Base.metadata.create_all(engine)
    return Session(engine)


def write_to_db(
        session: Session,
        data: FlightDBScheme
):
    flight = Flight(**data.dict())
    session.add(flight)
    session.commit()
