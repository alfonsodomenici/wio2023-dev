from datetime import datetime
from src.app import db

class Wio(db.Model):
    __tablename__ = 'wio'
    id = db.Column(db.Integer, primary_key=True)
    wio = db.Column(db.String(45), nullable=False, default='wio terminal')
    macaddress = db.Column(db.String(45), unique=True)
    code = db.Column(db.String(45), nullable=False)
