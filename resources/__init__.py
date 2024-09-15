from flask_restx import Api
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:123456@localhost/nba_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控


api = Api(app, version='1.0', title='NBATeams API',
    description='This is a simple API for NBA teams',
)


db = SQLAlchemy(app)

from resources import NBAResources