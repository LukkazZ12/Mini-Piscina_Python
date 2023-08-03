class Coffee:
	def __str__(self):
		return "This is the worst coffee you ever tasted."


class Intern:
	def __init__(self, name = "My name? I'm nobody, an intern, I have no name."):
		self.Name = name

	def __str__(self):
		return self.Name

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return Coffee()

if __name__ == "__main__":
	intern_without_name = Intern()
	intern_with_name = Intern("Mark")

	print("First intern's name:", intern_without_name)
	print("Second intern's name:", intern_with_name)

	try:
		intern_with_name.work()
	except Exception as e:
		print("Exception:", e)

	coffee = intern_with_name.make_coffee()
	print("Mark made a coffee:", coffee)

	try:
		intern_without_name.work()
	except Exception as e:
		print("Exception:", e)