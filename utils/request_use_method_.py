import requests


def request_use_method_(method: str, url: str, data: dict) -> requests.Response:
	"""
	This method can perform the following queries:
	GET, POST, PUT, DELETE, PATCH
	:param data:
	:param url:
	:param method:
	:return:
	"""
	match method:
		case 'GET':
			r = requests.get(url=url)
		case 'POST':
			r = requests.post(url=url, json=data)
		case 'PUT':
			r = requests.put(url=url, json=data)
		case "DELETE":
			r = requests.delete(url=url)
		case 'PATCH':
			r = requests.patch(url=url, json=data)
		case _:
			raise ValueError('This method use only the following requests: GET, POST, PUT, DELETE, PATCH')
	return r
