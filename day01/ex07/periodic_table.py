import sys

def read_file():
	with open(sys.argv[1], "r") as file:
		content = file.read()
	file.close()
	return content

def matrix_periodic_table(content):
	elements_lines = content.split("\n")
	elements = [[0 for _ in range(18)] for _ in range(7)]
	i = 0
	for line in elements_lines:
		if line:
			elem_split = line.split(",")
			j = int(elem_split[0].split(":")[1])
			elements[i][j] = elem_split
			if j == 17:
				i += 1
	return elements

def table_to_str(table):
	table_str = ""
	for line in table:
		for column in line:
			if column == line[0]:
				table_str += "			<tr>\n" + column
			elif column == line[-1]:
				table_str += column + "			</tr>\n" 
			else:
				table_str += column
	return table_str

def replace_on_html(table):
	html = '<!DOCTYPE html>\n<html lang="en">\n\n<head>\n	<meta charset="UTF-8">\n'\
			+ '	<title>Periodic table</title>\n	<style>\n		h1 {\n'\
			+ '			text-align: center;\n		}\n'\
			+ '		h4 {\n			text-align: center;\n		}\n'\
			+ '	</style>\n</head>\n\n'\
			+ '<body>\n	<h1>Periodic table</h1>'\
			+ '	<table>\n		<tbody>\n'\
			+ '			[...]\n		</tbody>\n'\
			+ '	</table>\n</body>\n\n'\
			+ '</html>'
	
	html = html.replace("[...]", table)
	return html

def build_table(elements):
	table = [[0 for _ in range(18)] for _ in range(7)]
	i = 0
	while i < len(elements):
		j = 0
		while j < len(elements[i]):
			if elements[i][j]:
				table[i][j] = '				<td style="border: 1px solid black; padding:10px">\n'\
					+ '					<h4>' + elements[i][j][0].split(" ")[0] + '</h4>\n'\
					+ '						<ul>\n							<li>No '\
					+ elements[i][j][1].split(":")[1] + '</li>\n'\
					+ '							<li>' + elements[i][j][2].split(" ")[2] + '</li>\n'\
					+ '							<li>' + elements[i][j][3].split(":")[1] + '</li>\n'\
					+ '							<li>eletrons:<br>'\
					+ elements[i][j][4].split(":")[1] + '</li>\n'\
					+ '						</ul>\n				</td>\n'
			else:
				table[i][j] = '				<td>\n				</td>\n'
			j += 1
		i += 1
	return table

def periodic_table():
	content = read_file()
	elements = matrix_periodic_table(content)
	table = build_table(elements)
	table_str = table_to_str(table)
	html = replace_on_html(table_str)
	with open("periodic_table.html", "w") as file:
		file.write(html)

if __name__ == "__main__":
	periodic_table()