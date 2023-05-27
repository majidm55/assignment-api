from sqlalchemy import create_engine, Column, DateTime, ForeignKey, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///content_management.db')
# Base.
