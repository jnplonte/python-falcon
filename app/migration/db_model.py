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

    def __init__(self, image, first_name, last_name, username, password, email, active, update_time):
        self.image = image
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.active = active
        self.update_time = update_time

    def __repr__(self):
        return "<user(%s, %s, %s, %s, %s, %s, %i, %s)>" % (self.image, self.first_name, self.last_name, self.username, self.password, self.email, self.active, self.update_time)


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
    likes_count = Column(INTEGER(11), nullable=False, server_default="0")
    shares_count = Column(INTEGER(11), nullable=False, server_default="0")
    update_time = Column(TIMESTAMP, server_default=func.now())
    create_time = Column(TIMESTAMP, server_default=func.now())

    def __init__(self, user_id, views_count, likes_count, shares_count, update_time):
        self.user_id = user_id
        self.views_count = views_count
        self.likes_count = likes_count
        self.shares_count = shares_count
        self.update_time = update_time

    def __repr__(self):
        return "<user_activity(%i, %i, %i, %i, %s)>" % (self.user_id, self.views_count, self.likes_count, self.shares_count, self.update_time)
