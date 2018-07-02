from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()

class CrawlerData(Base):
    __tablename__ = "crawler"
    id = Column(Integer, primary_key=True)
    site = Column(String)
    server = Column(String)

    def __str__(self):
        return "{} - {}".format(self.site, self.server)

    def __repr__(self):
        return self.__str__()
    

engine = create_engine("sqlite:///crawler_data.db")
Base.metadata.create_all(engine)