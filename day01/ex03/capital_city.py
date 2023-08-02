import sys

def get_capital_city():
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
	given_state = sys.argv[1]
	abbrev = ""
	for state in states:
		if state == given_state:
			abbrev = states[state]
	if not abbrev:
		print("Unknown state")
	for capital in capital_cities:
		if capital == abbrev:
			print(f"{capital_cities[capital]}")

if __name__ == '__main__':
	get_capital_city()