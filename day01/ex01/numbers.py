def print_numbers(content):
	i = 0

	while i < len(content):
		if content[i] == ',':
			print("")
		else:
			print(content[i], end="")
		i += 1

def read_file():
	file_name = "numbers.txt"
	with open(file_name, "r") as file:
		content = file.read()
	file.close()
	return content

def numbers():
	print_numbers(read_file())

if __name__ == '__main__':
	numbers()