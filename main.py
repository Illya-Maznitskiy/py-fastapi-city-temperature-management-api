from fastapi import FastAPI

from city_temp.city.router import router as city_router
from city_temp.temperature.router import router as temperature_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(city_router)
app.include_router(temperature_router)
