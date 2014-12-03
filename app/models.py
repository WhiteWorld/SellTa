from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    uuid = db.Column(db.String(32), unique = True, index = True)
    sex = db.Column(db.Boolean)
    character = db.Column(db.Integer)
    nickname = db.Column(db.String(32))
    words = db.Column(db.String(150))
    wechat = db.Column(db.String(32))
    created_at = db.Column(db.DateTime(), default = db.func.now())
    updated_at = db.Column(db.DateTime(), default = db.func.now(), onupdate = db.func.now())
    completed = db.Column(db.Boolean, default = False)
    remark = db.Column(db.String(64))
        
    def __init__(self, uuid):
        self.uuid = uuid
