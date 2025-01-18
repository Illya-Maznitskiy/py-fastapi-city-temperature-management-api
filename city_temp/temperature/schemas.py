from pydantic import BaseModel
import datetime


class TemperatureBase(BaseModel):
    city_id: int
    datetime: datetime.datetime
    temperature: float

    class Config:
        orm_mode = True


class TemperatureCreate(BaseModel):
    pass


class Temperature(BaseModel):
    id: int
