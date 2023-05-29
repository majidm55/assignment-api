import sys
from os.path import dirname, abspath

# Add the 'app' directory to the system path
app_path = dirname(dirname(abspath(__file__)))
sys.path.append(app_path)

from sqlalchemy import create_engine, Table, Column, DateTime, Integer, String, Text, text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create an engine to connect to your database

engine = create_engine('sqlite:///content_management.db')

# Create a metadata object

Base = declarative_base()
Base.metadata.create_all(bind=engine)
# Define your table

class Contents(Base):
  __tablename__ = 'contents'
  id = Column(Integer, primary_key=True)
  title = Column(String(250))
  url = Column(Text)
  thumbnail = Column(Text)
  timestamp = Column(DateTime)

alter_stmt = text("ALTER TABLE contents ADD COLUMN timestamp DATETIME")
# Create the database session
Session = sessionmaker(bind=engine)
session = Session()

# Execute the ALTER statement
session.execute(alter_stmt)

# Commit the changes
session.commit()

# Close the session
session.close()
