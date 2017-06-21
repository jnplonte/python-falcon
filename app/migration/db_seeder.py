from app.migration.db_model import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


def seed(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    BaseSqlOrm.metadata.drop_all(bind=engine)
    BaseSqlOrm.metadata.create_all(bind=engine)

    new_record = [
        User(None, 'john paul', 'onte', 'jnplonte', 'password', 'jnpl.onte@gmail.com', None, func.now()), 
        User(None, 'first name', 'last name', 'username', 'password', 'email@gmail.com', None, func.now()), 
        UserActivity('1', '0', '0', '0', func.now()), 
        UserActivity('2', '0', '0', '0', func.now())
    ]
    
    session.add_all(new_record)
    session.commit()