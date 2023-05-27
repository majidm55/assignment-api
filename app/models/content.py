from datetime import datetime
from config import db, ma

class Content(db.Model):
    __tablename__ = "contents"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    url = db.Column(db.Text)
    thumbnail = db.Column(db.Text)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class ContentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Content
        load_instance = True
        sqla_session = db.session

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)
