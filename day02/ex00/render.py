import sys, os, re
from settings import name, surname, age, profession

def error():
	if len(sys.argv) != 2:
		print("Invalid number of parameters. Try: python3 render.py myCV.template.")
		sys.exit(1)
	if os.path.splitext(sys.argv[1])[1] != ".template":
		print("Wrong extension. Try a '.template' extension file.")
		sys.exit(1)
	if not os.path.exists(sys.argv[1]):
		print("The file does not exist.")
		sys.exit(1)

def read_file():
	error()
	with open(sys.argv[1], "r") as file:
		content = file.read()
	file.close()
	return content

def replace():
	content = read_file()
	content = content.replace("{name}", str(name)).replace("{surname}", str(surname)) \
		.replace("{age}", str(age)).replace("{profession}", str(profession))
	file_name = "myCV.html"
	with open(file_name, "w") as file:
		file.write(content)

if __name__ == '__main__':
	replace()