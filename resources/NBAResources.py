from flask import request
from flask_restx import Resource
from resources import api
from services.NBAServices import NBAServices
from models.NBAModels import NBATeams

class NBAResourcesDetail(Resource):
    @api.doc(params={"id": "球队ID"})
    def get(self,id):
        """
        get方法用于获取球队详情
        This method returns the details of a team by its name.
        """
        try:
            NBAModels = NBAServices.get_teams_by_teamname(NBATeams,id)
            return {"id": f"{NBAModels.id}",
                    "team_name": f"{NBAModels.team_name}",
                    "founded_year": f"{NBAModels.founded_year}",
                    "city": f"{NBAModels.city}",
                    "championships_won": f"{NBAModels.championships_won}",},200
        except Exception as e:
            return {"message": f"输入的球队名称有误，请检查后重试。{e}"}, 404
    @api.doc(params={"id": "球队ID"})
    def delete(self,id):
        """
        delete方法用于删除球队
        This method deletes a team by its name.
        """
        try:
            NBAServices.delete_team(NBATeams,id)
            return {"message": "球队删除成功！","球队ID":f"{id}"}, 200
        except Exception as e:
            return {"message": f"球队删除失败！{e}"}, 500

    @api.doc(params={"team_name": "球队名称", "founded_year": "创立年份", "city": "所在城市",
                     "championships_won": "冠军赛赢得次数"})
    def put(self,id):
        """
        put方法用于更新球队详情
        This method updates the details of a team by its name.
        """
        try:
            request_json = request.json
            if request_json:
                NBAModels = NBAServices.update_team(NBATeams,id,request_json)
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

class NBAResourcesList(Resource):
    def get(self):
        """
        get方法用于获取所有球队列表
        This method returns a list of all teams.
        """
        try:
            NBAModels = NBAServices.get_all_teams()
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


    @api.doc(params={"team_name": "球队名称", "founded_year": "创立年份", "city": "所在城市",
                     "championships_won": "冠军赛赢得次数"})
    def post(self):
        """
        post方法用于创建球队
        This method creates a new team.
        """
        try:
            if NBAServices.get_teams_by_teamname(NBATeams,request.json["team_name"]):
                return {"message": "该球队已存在！"}, 400
            request_json = request.json
            if request_json:
                NBAModels = NBAServices.create_team(NBATeams,team_name=request_json["team_name"],
                                        founded_year=request_json["founded_year"],
                                        city=request_json["city"],
                                        championships_won=request_json["championships_won"])
            return {"message": "球队创建成功！",
                    "id": f"{NBAModels.id}",
                    "team_name": f"{NBAModels.team_name}",
                    "founded_year": f"{NBAModels.founded_year}",
                    "city": f"{NBAModels.city}",
                    "championships_won": f"{NBAModels.championships_won}"}, 201
        except Exception as e:
            return {"message": f"球队创建失败！{e}"}, 500


api.add_resource(NBAResourcesDetail, "/NBA/<int:id>")
api.add_resource(NBAResourcesList, "/NBA")