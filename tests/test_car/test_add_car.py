import pytest

from configuration import ENDPOINT
from src.api_methods.car_service.car import CarApiMethods
from src.emuns.car_service.car_brands import CarBrand
from src.emuns.car_service.car_models import CarModel
from src.pydentic_schemas.response.add_car import CarSchema
from src.response_helper.car_response import CarResponseHelper
from tests.test_car.data.valid_data import ActionAdd
from utils.request_use_method_ import request_use_method_


@pytest.mark.prod
@pytest.mark.dev
def test_action_add():
	"""
	This is case will be added car_service in car_service.
	Use http method: POST.

	Check:
	 1. Status code
	 2. Structure data (used CarSchema)
	 3. Brand and model in response
	:return:
	"""
	res = request_use_method_(method='POST',
	                          url=f'{ENDPOINT}{CarApiMethods.jetta_receiver.value}',
	                          data=ActionAdd.VALID_DATA)

	response = CarResponseHelper(response=res, schema=CarSchema)
	response.assert_status_code(expected_status_code=200)
	response.validate_action_add_response(make=CarBrand.volkswagen.value,
	                                      model=CarModel.jetta.value)
