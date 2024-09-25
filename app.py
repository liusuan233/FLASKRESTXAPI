from flask import Flask
from flask_restx import Api
from models.NBAModels import db
from resources.NBAResources import NBAResourcesDetail,NBAResourcesList

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/nba_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

    db.init_app(app)

    api = Api(app, version='1.0', title='NBA API', description='This is a NBA API')

    api.add_resource(NBAResourcesDetail, "/NBA/<int:id>")
    api.add_resource(NBAResourcesList, "/NBA")


    return app


