def my_var():
	int42 = 42
	str42 = "42"
	str42name = "quarante-deux"
	float42 = 42.0
	bool42 = True
	list42 = [42]
	dict42 = {42: 42}
	tuple42 = (42,)
	set42 = set()
	print(f"{int42} has a type {type(int42)}")
	print(f"{str42} has a type {type(str42)}")
	print(f"{str42name} has a type {type(str42name)}")
	print(f"{float42} has a type {type(float42)}")
	print(f"{bool42} has a type {type(bool42)}")
	print(f"{list42} has a type {type(list42)}")
	print(f"{dict42} has a type {type(dict42)}")
	print(f"{tuple42} has a type {type(tuple42)}")
	print(f"{set42} has a type {type(set42)}")

if __name__ == '__main__':
	my_var()