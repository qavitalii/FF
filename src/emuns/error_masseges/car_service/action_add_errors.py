from enum import StrEnum


class ActionAddErrorMessages(StrEnum):
	WRONG_BRAND = 'Receive BRAND is not equal to expected'
	WRONG_MODEL = 'Receive MODEL is not equal to expected'
	WRONG_RESULT = 'Receive RESULT is not equal to expected'
