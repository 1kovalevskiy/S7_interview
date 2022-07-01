from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import Session, declared_attr, declarative_base


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Publ(Base):
    name = Column(String(200))
    quartile = Column(String(2))
    impact = Column(Integer)
    journal = Column(String(200))
    send = Column(Date)
    accept = Column(Date)
    pub_online = Column(Date)
    pub_offline = Column(Date)

    def __repr__(self):
        return f'get {self.send} {self.impact}'


def database_start():
    engine = create_engine('sqlite:///sqlite_old.db', echo=False)
    Base.metadata.create_all(engine)

    return Session(engine)

