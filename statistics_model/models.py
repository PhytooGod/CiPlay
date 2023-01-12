from core.db import Base
from sqlalchemy import Column, Integer, DateTime, Float


class Statistics(Base):
    __tablename__ = "statistics"
    date = Column(DateTime, primary_key=True, index=True, unique=True)
    views = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    cost = Column(Float, default=0.0)

    def to_dict(self) -> dict:
        return {
            'date': self.date.strftime("%Y-%m-%d"),
            'views': self.views,
            'clicks': self.clicks,
            'cost': self.cost
        }

