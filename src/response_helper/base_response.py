from json import JSONDecodeError

import pytest

from src.emuns.error_masseges.base_error_messages import BaseErrorMessages


class BaseResponseHelper:
	def __init__(self, response, schema=None):
		self.response = response
		self.response_status = response.status_code
		try:
			self.response_json = response.json()
		except JSONDecodeError:
			self.response_json = None
		if schema:
			self.schema = schema

	def assert_status_code(self, expected_status_code):
		assert self.response_status == expected_status_code, \
			f'{BaseErrorMessages.WRONG_STATUS_CODE.value}\n' \
			f'Status code: {self.response_status}\n' \
			f'Expected status code: {expected_status_code}\n' \
			f'Requested url: {self.response.url}\n' \
			f'Request method: {self.response.request.method}\n' \
			f'Request headers: {self.response.request.headers}\n' \
			f'Request body: {self.response.request.body}'
		return self

	def base_validate_response(self):
		if not self.response_json:
			pytest.fail(f'{BaseErrorMessages.WRONG_RESPONSE_EMPTY}\n'
			            f'Response body: {self.response_json}')

		if self.response_status:
			if isinstance(self.response_json, dict):
				self.schema(**self.response_json)

			elif isinstance(self.response_json, list):
				for item in self.response_json:
					self.schema(**item)
			else:
				pytest.fail(f'{BaseErrorMessages.WRONG_STRUCTURE}\n'
				            f'Response body: {self.response_json}')

			return self
		return self
