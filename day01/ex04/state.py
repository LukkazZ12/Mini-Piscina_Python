import sys

def get_state():
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
	given_capital = sys.argv[1]
	abbrev = ""
	for capital in capital_cities:
		if capital_cities[capital] == given_capital:
			abbrev = capital
	if not abbrev:
		print("Unknown capital city")
	for state in states:
		if states[state] == abbrev:
			print(f"{state}")

if __name__ == '__main__':
	get_state()