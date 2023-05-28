from flask import make_response, abort
from ujson import loads
from config import db
from models import Content, ContentEngagement, all_engagements, contents_schema

def getAllData():
    allContent = Content.query.all()
    allContent = contents_schema.dump(allContent)
    for content in allContent:
        content_obj = Content.query.get(content["id"])
        content["total_engagement_time"] = content_obj.total_engagement_time

    return allContent
