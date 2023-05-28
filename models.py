import sys
from os.path import dirname, abspath

# Add the 'app' directory to the system path
app_path = dirname(dirname(abspath(__file__)))
sys.path.append(app_path)

from datetime import datetime
from config import db, ma

from datetime import datetime
from sqlalchemy import func, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.hybrid import hybrid_property

import app.globals.raw_content as rawData

class Content(db.Model):
    __tablename__ = "contents"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    url = db.Column(db.Text)
    thumbnail = db.Column(db.Text)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    @hybrid_property
    def total_engagement_time(self):
        return db.session.query(func.sum(ContentEngagement.engagement_time)).filter(ContentEngagement.content_id == self.id).scalar()

class ContentEngagement(db.Model):
    __tablename__ = "content_engagement"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content_id = Column(Integer, ForeignKey("contents.id"))
    engagement_time = Column(Integer)

    def __init__(self, content_id, engagement_time):
        self.content_id = content_id
        self.engagement_time = engagement_time

class ContentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Content
        load_instance = True
        sqla_session = db.session


class ContentEngagamentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContentEngagement
        load_instance = True
        sqla_session = db.session

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

content_engagement = ContentEngagamentSchema()
all_engagements = ContentEngagamentSchema(many=True)


# engine = create_engine('sqlite:///content_management.db')
# Base = declarative_base()
# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# ContentEngagement.__table__.create(bind=engine, checkfirst=True)

# for data in rawData.Engagement:
#     engagement = ContentEngagement(data["content_id"], data["engagement_time"])
#     session.add(engagement)

# session.commit()
