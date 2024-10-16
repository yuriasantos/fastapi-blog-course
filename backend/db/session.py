from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print('Database URL is ', SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(autoflush=False, autocomit = False, bind=engine)
