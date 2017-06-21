from app.migration.db_model import *
from sqlalchemy.orm import sessionmaker


def seed(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    BaseSqlOrm.metadata.drop_all(bind=engine)
    BaseSqlOrm.metadata.create_all(bind=engine)

    new_record = [
        User('', 'john paul', 'onte', 'jnplonte', 'password', 'jnpl.onte@gmail.com'), 
        User('', 'first name', 'last name', 'username', 'password', 'email@gmail.com'), 
        UserActivity('1'), 
        UserActivity('2')
    ]
    
    session.add_all(new_record)
    session.commit()