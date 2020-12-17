from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData

meta = MetaData()

HeadHunterTable = Table(
    'skill', meta,
    Column('id', Integer, primary_key=True),
    Column('word', String(80), nullable=False),
    Column('skill', String(80), nullable=False),
    Column('count', Integer, nullable=False),
    Column('created_date', DateTime, default=datetime.utcnow),
)
