class ActionAdd:
	INVALID_DATA = [
		{"action": "add", "car_service": {"make": "Volkswagen"}},
		{"action": "add", "car_service": {"make": 123, "model": "Jetta"}},
		{"action": "create", "car_service": {"make": "Volkswagen", "model": "Jetta"}},
		{"action": "add"},
		{"action": "add", "car_service": {"brand": "Volkswagen", "model": "Jetta"}},
		{"action": "add", "car_service": {"make": "", "model": "Jetta"}},
		{"action": "add", "car_service": {"make": "Volkswagen", "model": ""}},
		{"action": "add", "car_service": {"make": "Volkswagen", "model": 123}},
		{"action": "add", "car_service": {"make": "Volkswagen", "model": "Jetta", "year": 2024}},
		{"action": True, "car_service": {"make": "Volkswagen", "model": "Jetta"}},
		{"action": "add", "car_service": {"make": "Volkswagen", "model": "Jetta", "color": "blue"}},
		{"action": "add", "car_service": {"make": "Volkswagen123", "model": "Jetta"}}
	]
