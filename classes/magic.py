# this is magic class

import random

class magic:
	def __init__(self, name, cost, damage, type):
		self.name = name
		self.cost = cost
		self.damage = damage
		self.type = type

		def magic_damage(self):
			low = self.damage - 5
			high = self.damage + 5
			return random.randrange(low, high)