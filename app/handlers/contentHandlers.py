from flask import make_response, abort
from config import db
from models.contentModels import Content, contents_schema

def getAllData():
    allContent = Content.query.all()
    allContent = contents_schema.dump(allContent)
    for content in allContent:
        content_obj = Content.query.get(content["id"])
        content["totalEngagementTime"] = content_obj.total_engagement_time

    return allContent
