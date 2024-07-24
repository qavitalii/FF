from pydantic import BaseModel
from src.emuns.car_service.result_enums import Result


class Car(BaseModel):
	make: str
	model: str


class CarSchema(BaseModel):
	car: Car
	result: Result
