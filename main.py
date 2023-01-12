import json

import uvicorn
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from core.db import SessionLocal
from statistics_model.models import Statistics as StatisticsModel
from schemas import Statistics, GetStatistics

app = FastAPI()
db = SessionLocal()


@app.post("/statistics/create")
def create_statistics(statistics: Statistics) -> dict:
    new_statistics = db.query(StatisticsModel).filter(StatisticsModel.date == statistics.date).first()
    if new_statistics is None:
        new_statistics = StatisticsModel(
            date=statistics.date,
            views=statistics.views,
            clicks=statistics.clicks,
            cost=statistics.cost
        )
    else:
        new_statistics.views += statistics.views
        new_statistics.clicks += statistics.clicks
        new_statistics.cost += statistics.cost

    db.add(new_statistics)
    db.commit()
    return {"message": "success"}


@app.post("/statistics/get")
def get_statistics(statistics_get: GetStatistics,
                   order_by: str = Query("date", enum=["date", "views", "clicks", "cost", "cpc", "cpm"]),
) -> dict:
    statistics = db.query(StatisticsModel).filter(
        (StatisticsModel.date >= statistics_get.date_from) & (StatisticsModel.date <= statistics_get.date_to)
    ).order_by(StatisticsModel.date).all()
    response = []
    for i in statistics:
        resp = i.to_dict()
        resp['cpc'] = resp['cost']/resp['clicks']
        resp['cpm'] = (resp['cost']/resp['views']) * 1000
        response.append(resp)
    response = response if order_by == 'date' else sorted(response, key=lambda d: d[order_by], reverse=True)
    return JSONResponse(content=response)


@app.delete("/statistics/delete")
def delete_statistics():
    db.query(StatisticsModel).delete()
    return {"message": "Deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
