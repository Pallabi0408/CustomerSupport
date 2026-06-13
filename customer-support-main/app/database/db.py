import pymysql
from flask import g
from app.config.config import Config
import logging

def get_db():
    if 'db' not in g:
        try:
            g.db = pymysql.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.MySQLError as e:
            logging.error(f"Error connecting to MySQL: {e}")
            raise
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
