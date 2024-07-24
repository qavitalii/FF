import pytest

from src.emuns.error_masseges.base_error_messages import BaseErrorMessages
from src.emuns.error_masseges.car_service.action_add_errors import ActionAddErrorMessages
from src.response_helper.base_response import BaseResponseHelper


class CarResponseHelper(BaseResponseHelper):
	def validate_action_add_response(self, make, model):
		if not isinstance(self.response_json, dict):
			pytest.fail(f'{BaseErrorMessages.WRONG_STRUCTURE}\n'
			            f'Response body: {self.response_json}')
		sc = self.schema(**self.response_json)

		assert sc.car.make == make, (f'{ActionAddErrorMessages.WRONG_BRAND.value}\n'
		                             f'Brand: {sc.car.make}\n'
		                             f'Expected brand: {make}')

		assert sc.car.model == model, (f'{ActionAddErrorMessages.WRONG_MODEL.value}\n'
		                               f'Model: {sc.car.model}\n'
		                               f'Expected model: {model}')
