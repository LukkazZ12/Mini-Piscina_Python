import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
	def __init__(self):
		self.drink_count = 0
		self.repaired = True

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.price = 0.90
			self.name = "empty cup"

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	
	def repair(self):
		self.repaired = True

	def serve(self, drink):
		if not self.repaired:
			raise CoffeeMachine.BrokenMachineException()

		self.drink_count += 1

		if self.drink_count >= 10:
			self.repaired = False
			self.drink_count = 0

		return random.choice([drink, CoffeeMachine.EmptyCup()])

if __name__ == "__main__":
	coffee_machine = CoffeeMachine()

	for _ in range(15):
		try:
			drink = coffee_machine.serve(random.choice([Coffee(), Tea(), Chocolate(), Cappuccino()]))
			print(drink)
		except CoffeeMachine.BrokenMachineException:
			print("Machine is broken! Time to repair.")
			coffee_machine.repair()