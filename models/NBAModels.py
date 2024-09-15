from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from resources import db



class NBATeams(db.Model):
    __tablename__ = 'nba_teams'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    team_name:Mapped[str] = mapped_column(String, nullable=False, unique=True)
    city:Mapped[str] = mapped_column(String, nullable=False)
    founded_year:Mapped[str] = mapped_column(String, nullable=False)
    championships_won:Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    def to_dict(self):
        return {
            'id': self.id,
            'team_name': self.team_name,
            'city': self.city,
            'found_year': self.found_year,
            'championships': self.championships
        }
