from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Conectar ao banco
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)