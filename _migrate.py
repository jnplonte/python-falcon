from app.migration.db_model import *

from app import create_table

env = 'dev' # hardcoded to dev to prevent production migration

engine = create_table(env.upper())

# BaseSqlOrm.metadata.drop_all(bind=engine)
# BaseSqlOrm.metadata.create_all(bind=engine)
