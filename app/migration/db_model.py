from sqlalchemy import Column, ForeignKey, create_engine
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
import uuid

BaseSqlOrm = declarative_base()

def generate_uuid():
   return str(uuid.uuid4())

class User(BaseSqlOrm):
    """ user entity class """
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    # first_name = Column(VARCHAR(250), nullable=True)
    # last_name = Column(VARCHAR(250), nullable=True)
    # email = Column(VARCHAR(250), nullable=False, unique=True)
    # username = Column(VARCHAR(250), nullable=True)
    # password = Column(VARCHAR(250), nullable=False)
    # active = Column(TINYINT(1), nullable=False, default=0)
    # create_time = Column(DATETIME)
    # update_time = Column(DATETIME)

    # def __init__(self, email):
    #     self.email = email
