import sys

def get_capital_city(parameter, states, capital_cities):
	abbrev = ""
	for state in states:
		if state == parameter:
			abbrev = states[state]
	for capital in capital_cities:
		if capital == abbrev:
			return capital_cities[capital]
	else:
		return abbrev

def get_state(parameter, states, capital_cities):
	abbrev = ""
	for capital in capital_cities:
		if capital_cities[capital] == parameter:
			abbrev = capital
	for state in states:
		if states[state] == abbrev:
			return state
	else:
		return abbrev

def get_parameters():
	parameters = sys.argv[1].split(", ")
	i = 0
	while i < len(parameters):
		parameters[i] = parameters[i].strip()
		i += 1
	return parameters

def get_capital_city_or_state():
	if len(sys.argv) != 2:
		sys.exit(1)
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	parameters = get_parameters()
	for parameter in parameters:
		if parameter:
			parameter_aux = parameter.title()
			result = ""
			result = get_state(parameter_aux, states, capital_cities)
			if result:
				print(f"{parameter_aux} is the capital of {result}")
			else:
				result = get_capital_city(parameter_aux, states, capital_cities)
				if result:
					print(f"{result} is the capital of {parameter_aux}")
				else:
					print(f"{parameter} is neither a capital city nor a state")

if __name__ == '__main__':
	get_capital_city_or_state()