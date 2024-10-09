from flask import Flask
from flask_restx import Api
from models.NBAModels import db
from resources.NBAResources import ns as ns_nba

def create_app():
    # 初始化Flask应用
    app = Flask(__name__)# __main__
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba_db.db'
    # 关闭对模型修改的监控
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 初始化数据库
    db.init_app(app)
    # 初始化API
    api = Api(app, version='1.0', title='NBA API', description='This is a NBA API')
    # 注册路由
    api.add_namespace(ns_nba)
    return app


