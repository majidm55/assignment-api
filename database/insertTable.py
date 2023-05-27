import sys
from os.path import dirname, abspath

# Add the 'app' directory to the system path
app_path = dirname(dirname(abspath(__file__)))
sys.path.append(app_path)

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, DateTime, Integer, String, Text
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to your database
engine = create_engine('sqlite:///content_management.db')

# Create a base class for declarative models
Base = declarative_base()

# Define your model class
class Content(Base):
    __tablename__ = 'contents'

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    url = Column(Text)
    thumbnail = Column(Text)
    timestamp = Column(DateTime)

# Create the table
Base.metadata.create_all(bind=engine)

# Get a session from the engine
Session = sessionmaker(bind=engine)
session = Session()

# Get all existing content objects
existing_content = session.query(Content).all()

# Update the timestamp for each content object
for content in existing_content:
    content.timestamp = datetime.now()

# Commit the session to persist the changes
session.commit()

# Close the session
session.close()
