from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class NBATeams(db.Model):
    # 设置 __tablename__ 表名 为 nba_teams
    __tablename__ = 'nba_teams'
    # 设置映射关系
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    team_name:Mapped[str] = mapped_column(String, nullable=False, unique=True)
    city:Mapped[str] = mapped_column(String, nullable=False)
    founded_year:Mapped[str] = mapped_column(String, nullable=False)
    championships_won:Mapped[int] = mapped_column(Integer, nullable=False, default=0)

