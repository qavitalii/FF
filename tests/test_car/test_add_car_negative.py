import pytest
import requests
from configuration import ENDPOINT
from src.api_methods.car_service.car import CarApiMethods
from src.pydentic_schemas.response.add_car import CarSchema
from src.response_helper.base_response import BaseResponseHelper
from tests.test_car.data import valid_data
from tests.test_car.data import invalid_data
from utils.request_use_method_ import request_use_method_
from src.emuns.error_masseges.base_error_messages import BaseErrorMessages


@pytest.mark.prod
@pytest.mark.dev
@pytest.mark.parametrize('data', invalid_data.ActionAdd.INVALID_DATA)
def test_add_car_with_incorrect_data(data: dict):
	"""
	A testcase with incorrect data.

	Check:
		1. Status code == 204
	:return:
	"""
	r = requests.post(url=f'{ENDPOINT}{CarApiMethods.jetta_receiver.value}',
	                  json=data)
	BaseResponseHelper(r).assert_status_code(204)


@pytest.mark.prod
@pytest.mark.dev
@pytest.mark.parametrize('method', ['GET', 'PUT', 'DELETE', 'PATCH'])
def test_add_car_with_incorrect_http_method(method: str):
	"""
	A testcase with incorrect http method.

	Check:
		1. Status code == 405
	:return:
	"""

	res = request_use_method_(method=method,
	                          url=f'{ENDPOINT}{CarApiMethods.jetta_receiver.value}',
	                          data=valid_data.ActionAdd.VALID_DATA)

	BaseResponseHelper(res).assert_status_code(405)
