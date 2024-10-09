from flask import request
from flask_restx import Resource,Namespace,fields
from models.NBAModels import NBATeams
from app import db

# 创建命名空间ns
ns = Namespace('nba', description='NBA related operations')

# 创建模型
player_model = ns.model("NBATeams", {
    'team_name': fields.String(required=True, description='Team name'),
    'founded_year': fields.Integer(required=True, description='Player founded year'),
    'city': fields.String(required=True, description='Player city'),
    'championships_won': fields.Integer(required=True, description='Player championships won')
})

@ns.route('/<int:id>')
class NBAResourcesDetail(Resource):
    @ns.doc(params={"id": "球队ID"})
    def get(self,id):
        """
        get方法用于获取球队详情
        This method returns the details of a team by its name.
        """
        try:
            # 查询数据库
            NBAModels = db.session.query(NBATeams).filter_by(id=id).first()
            # 返回查询到的球队信息
            return {"id": f"{NBAModels.id}",
                    "team_name": f"{NBAModels.team_name}",
                    "founded_year": f"{NBAModels.founded_year}",
                    "city": f"{NBAModels.city}",
                    "championships_won": f"{NBAModels.championships_won}",},200

        except Exception as e:
            # 数据库查询失败
            return {"message": f"输入的球队名称有误，请检查后重试。{e}"}, 404
    @ns.doc(params={"id": "球队ID"})
    def delete(self,id):
        """
        delete方法用于删除球队
        This method deletes a team by its name.
        """
        try:
            # 查询数据库
            NBATeamsInfo = NBATeams.query.filter(NBATeams.id == id).first()
            # 删除球队信息
            db.session.delete(NBATeamsInfo)  # 删除查询到的记录
            db.session.commit()
            # 返回删除成功信息
            return {"message": "球队删除成功！","球队ID":f"{id}"}, 200
        except Exception as e:
            return {"message": f"球队删除失败！{e}"}, 500

    @ns.doc(params={"id": "球队ID"})
    @ns.expect(player_model)
    def put(self,id):
        """
        put方法用于更新球队详情
        This method updates the details of a team by its name.
        """
        try:
            NBAteaminfo = request.json
            if NBAteaminfo:
                # 查询数据库
                NBATeamsInfo = NBATeams.query.filter(NBATeams.id == id).first()
                # 更新球队信息
                NBATeamsInfo.team_name = NBAteaminfo['team_name']
                NBATeamsInfo.city = NBAteaminfo['city']
                NBATeamsInfo.founded_year = NBAteaminfo['founded_year']
                NBATeamsInfo.championships_won = NBAteaminfo['championships_won']
                # 更新数据库
                db.session.commit()
                # 返回更新后的球队信息
                NBAModels = NBATeamsInfo
                return {"message": "球队更新成功！",
                        "id": f"{NBAModels.id}",
                        "team_name": f"{NBAModels.team_name}",
                        "founded_year": f"{NBAModels.founded_year}",
                        "city": f"{NBAModels.city}",
                        "championships_won": f"{NBAModels.championships_won}"
                        }, 200
            else:
                return {"message": "输入的JSON数据为空！"}, 400
        except Exception as e:
            return {"message": f"球队更新失败！{e}"}, 500
@ns.route('/')
class NBAResourcesList(Resource):
    @ns.doc()
    def get(self):
        """
        get方法用于获取所有球队列表
        This method returns a list of all teams.
        """
        try:
            # 查询数据库
            NBAModels = db.session.query(NBATeams).all()
            # 返回查询到的所有球队信息
            teams_list = []
            for team in NBAModels:
                teams_list.append({"id": f"{team.id}",
                                   "team_name": f"{team.team_name}",
                                   "founded_year": f"{team.founded_year}",
                                   "city": f"{team.city}",
                                   "championships_won": f"{team.championships_won}"})
            return {"teams": teams_list}, 200
        except Exception as e:
            return {"message": f"获取球队列表失败！{e}"}, 500


    @ns.doc()
    @ns.expect(player_model)
    def post(self):
        """
        post方法用于创建球队
        This method creates a new team.
        """
        try:
            if db.session.query(NBATeams).filter_by(team_name=request.json["team_name"]).first():
                return {"message": "该球队已存在！"}, 400
            # 接收请求数据
            request_json = request.json
            if request_json:
                NBATeamsInfo = NBATeams(team_name=request_json["team_name"],
                                        city=request_json["founded_year"],
                                        founded_year=request_json["city"],
                                        championships_won=request_json["championships_won"])
                db.session.add(NBATeamsInfo)
                db.session.commit()
            return {"message": "球队创建成功！",
                    "id": f"{NBATeamsInfo.id}",
                    "team_name": f"{NBATeamsInfo.team_name}",
                    "founded_year": f"{NBATeamsInfo.founded_year}",
                    "city": f"{NBATeamsInfo.city}",
                    "championships_won": f"{NBATeamsInfo.championships_won}"}, 201
        except Exception as e:
            return {"message": f"球队创建失败！{e}"}, 500


