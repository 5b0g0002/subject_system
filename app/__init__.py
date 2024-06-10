from flask import Flask
from .db import mysql
from config import Config
import time

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)

    # 測試資料庫連接，添加重試邏輯
    for _ in range(5):
        try:
            with app.app_context():
                conn = mysql.connection
                cursor = conn.cursor()
                cursor.execute('SELECT 1')
                cursor.close()
                print('success')
                break
        except Exception as e:
            print(f'Failed to connect to the database: {e}')
            time.sleep(5)  # 等待 5 秒後重試

    with app.app_context():
        from . import routes

    return app
