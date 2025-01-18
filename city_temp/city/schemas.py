from pydantic import BaseModel


class CityBase(BaseModel):
    name: str
    additional_info: str

    class Config:
        orm_mode = True


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int
