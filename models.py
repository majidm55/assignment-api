from datetime import datetime
from config import db, ma

from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Content(db.Model):
    __tablename__ = "contents"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    url = db.Column(db.Text)
    thumbnail = db.Column(db.Text)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    engagment_time = relationship("ContentEngagement", back_populates="contents")

class ContentEngagement(db.Model):
    __tablename__ = "content_engagement"
    id = Column(Integer, primary_key=True)
    content_id = Column(Integer, ForeignKey("contents.id"))
    engagement_time = Column(Integer)

class ContentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Content
        load_instance = True
        sqla_session = db.session

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)
