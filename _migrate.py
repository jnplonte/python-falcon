from app.migration.db_seeder import seed
from app import create_table

env = 'dev' # hardcoded to dev to prevent production migration

engine = create_table(env.upper(), log_level=None)

seed(engine)