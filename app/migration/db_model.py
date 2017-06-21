from sqlalchemy import Column, ForeignKey, create_engine
from sqlalchemy.dialects.mysql import INTEGER, TIMESTAMP, VARCHAR, TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

BaseSqlOrm = declarative_base()

class User(BaseSqlOrm):
    """ user entity class """
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_engine': 'MyISAM',
        'mysql_charset': 'utf8'
    }

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    image = Column(VARCHAR(250), nullable=True)
    first_name = Column(VARCHAR(250), nullable=True)
    last_name = Column(VARCHAR(250), nullable=True)
    username = Column(VARCHAR(250), nullable=True)
    password = Column(VARCHAR(250), nullable=True)
    email = Column(VARCHAR(250), nullable=False, unique=True)
    active = Column(TINYINT(1), nullable=False, server_default="0")
    update_time = Column(TIMESTAMP, server_default=func.now())
    create_time = Column(TIMESTAMP, server_default=func.now())

    def __init__(self, image, first_name, last_name, username, password, email):
        self.image = image
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<user(%s, %s, %s, %s, %s, %s)>" % (self.image, self.first_name, self.last_name, self.username, self.password, self.email)


class UserActivity(BaseSqlOrm):
    """ user entity class """
    __tablename__ = 'user_activity'
    __table_args__ = {
        'mysql_engine': 'MyISAM',
        'mysql_charset': 'utf8'
    }

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(11), nullable=False)
    views_count = Column(INTEGER(11), nullable=False, server_default="0")
    views_last = Column(VARCHAR(500), nullable=True)
    likes_count = Column(INTEGER(11), nullable=False, server_default="0")
    likes_last = Column(VARCHAR(500), nullable=True)
    shares_count = Column(INTEGER(11), nullable=False, server_default="0")
    shares_last = Column(VARCHAR(500), nullable=True)
    update_time = Column(TIMESTAMP, server_default=func.now())
    create_time = Column(TIMESTAMP, server_default=func.now())

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<user_activity(%s)>" % (self.user_id)
