from src.emuns.car_service.actions import Action
from src.emuns.car_service.car_models import CarModel
from src.emuns.car_service.car_brands import CarBrand


class ActionAdd:
	VALID_DATA = {"action": Action.add.value,
	              "car_service":
		              {"make": CarBrand.volkswagen.value,
		               "model": CarModel.jetta.value
		               }
	              }
