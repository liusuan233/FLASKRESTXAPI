from app import db
from models.NBAModels import NBATeams


class NBAServices:
    def get_teams_by_teamid(self, id):
        # 获取指定ID的球队信息
        return db.session.query(NBATeams).filter_by(id=id).first()

    def create_team(self, team_name, city, founded_year, championships_won):
        # 创建球队
        NBATeamsInfo = NBATeams(team_name=team_name,
                                city=city,
                                founded_year=founded_year,
                                championships_won=championships_won)
        db.session.add(NBATeamsInfo)
        db.session.commit()
        return  NBATeamsInfo

    def update_team(self, id, NBAteaminfo):
        # 更新球队信息
        NBATeamsInfo = NBATeams.query.filter(NBATeams.id == id).first()
        NBATeamsInfo.team_name = NBAteaminfo['team_name']
        NBATeamsInfo.city = NBAteaminfo['city']
        NBATeamsInfo.founded_year = NBAteaminfo['founded_year']
        NBATeamsInfo.championships_won = NBAteaminfo['championships_won']
        db.session.commit()
        return NBATeamsInfo

    def delete_team(self, id):
        # 删除球队
        NBATeamsInfo = NBATeams.query.filter(NBATeams.id == id).first()
        db.session.delete(NBATeamsInfo)  # 删除查询到的记录
        db.session.commit()  # 提交
        return NBATeamsInfo

    @classmethod
    def get_all_teams(cls):
        # 获取所有球队信息
        return db.session.query(NBATeams).all()

