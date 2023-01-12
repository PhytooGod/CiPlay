from pydantic import BaseModel, validator
from datetime import date, datetime


class Statistics(BaseModel):
    date: date
    views: int = 0
    clicks: int = 0
    cost: float = 0.0

    @validator('date')
    def date_validation(cls, v):
        if isinstance(v, str):
            return datetime.strptime(
                v, "%Y-%m-%d"
            )
        return v

    @validator('views')
    def validate_views(cls, v):
        assert isinstance(v, int)
        return v

    @validator('clicks')
    def validate_clicks(cls, v):
        assert isinstance(v, int)
        return v

    @validator('cost')
    def validate_cost(cls, v):
        assert isinstance(v, float)
        return v


class GetStatistics(BaseModel):
    date_from: date
    date_to: date

    @validator('date_from')
    def date_from_validation(cls, v):
        if isinstance(v, str):
            return datetime.strptime(
                v, "%Y-%m-%d"
            )
        return v

    @validator('date_to')
    def date_to_validation(cls, v):
        if isinstance(v, str):
            return datetime.strptime(
                v, "%Y-%m-%d"
            )
        return v
