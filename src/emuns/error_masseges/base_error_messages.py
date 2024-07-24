from enum import StrEnum


class BaseErrorMessages(StrEnum):
	WRONG_STATUS_CODE = 'Receive status code is not equal to expected'
	WRONG_RESPONSE_EMPTY = 'Response empty'
	WRONG_STRUCTURE = 'The structure is not as expected'
