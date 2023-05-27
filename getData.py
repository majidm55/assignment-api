from flask import make_response, abort

from config import db
from content import Content, content_schema, contents_schema

def getAllData():
    allContent = Content.query.all()
    return contents_schema.dump(allContent)
