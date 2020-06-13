import random
from .magic import magic
from .bar import bar

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '033[4m'

class Person:
	def __init__(self, name, hp, mp, atk, magic_array, item_array):
		self.maxhp = hp
		self.hp = hp
		self.maxmp = mp
		self.mp = mp
		self.atkl = atk-10
		self.atkh = atk+10
		self.magic_array = magic_array
		self.actions = ["Attack", "Magic", "Items"]
		self.item_array = item_array
		self.name = name

	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)

	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def take_heal(self, dmg):
		self.hp = min(self.maxhp, self.hp + dmg)
		return self.hp

	def get_hp(self):
		return self.hp

	def get_maxhp(self):
		return self.maxhp

	def get_mp(self):
		return self.mp

	def get_maxmp(self):
		return self.maxmp

	def reduce_mp(self, cost):
		self.mp -= cost

	def choose_enemy(self, enemies):
		print(bcolors.FAIL + bcolors.BOLD + "Enemies:" + bcolors.ENDC)
		i = 1
		for enemy in enemies:
			if enemy.get_hp() > 0:
				print(str(i) + ":" + enemy.name)
			i += 1
		return (int(input("Choose enemy: ")) - 1)

	def choose_action(self):
		print(bcolors.OKBLUE + bcolors.BOLD + "Actions:" + bcolors.ENDC)
		i = 1
		for item in self.actions:
			print(str(i) + ":" + item)
			i += 1
		return (int(input("Choose action: ")) - 1)

	def choose_magic(self):
		print(bcolors.OKBLUE + bcolors.BOLD + "Magics:" + bcolors.ENDC)
		i = 1
		for spell in self.magic_array:
			print(str(i) + ":" + spell.name + "(cost:" + str(spell.cost) + ")")
			i += 1
		return (int(input("Choose magic: ")) - 1)

	def choose_item(self):
		print(bcolors.OKBLUE + bcolors.BOLD + "Items:" + bcolors.ENDC)
		i = 1
		for item in self.item_array:
			if item["quant"] > 0:
				print(str(i) + ":" + item["name"].name + "(Property:" + str(item["name"].amount) + ", Quantity:" + str(item["quant"]) + ")")
			i += 1
		return (int(input("Choose item: ")) - 1)


	def get_enemy_status(self):

		HP_bar = bar(self.hp, self.maxhp, 52)
		MP_bar = bar(self.mp, self.maxmp, 10)

		str_hp = str(self.hp)
		while (len(str_hp)) < 4:
			str_hp = " " + str_hp

		str_mp = str(self.mp)
		while (len(str_mp)) < 2:
			str_mp = " " + str_mp

		print("                    ____________________________________________________ ")
		print(
			bcolors.BOLD + self.name + ":    " + str_hp + "/" + str(
				self.maxhp) + " |" + bcolors.ENDC + bcolors.FAIL + HP_bar.get_bar() + bcolors.ENDC +
			bcolors.BOLD + "|" + bcolors.ENDC)


	def get_player_status(self):

		HP_bar = bar(self.hp, self.maxhp, 25)
		MP_bar = bar(self.mp, self.maxmp, 10)

		str_hp = str(self.hp)
		while (len(str_hp)) < 4:
			str_hp = " " + str_hp

		str_mp = str(self.mp)
		while (len(str_mp)) < 2:
			str_mp = " " + str_mp

		print("                    _________________________                 __________")
		print(
			bcolors.BOLD + self.name + ":    " + str_hp + "/" + str(self.maxhp) + " |" + bcolors.ENDC + bcolors.OKGREEN + HP_bar.get_bar() + bcolors.ENDC +
			bcolors.BOLD + "|          " + str_mp + "/" + str(self.maxmp) + "|" + bcolors.ENDC + bcolors.OKGREEN + MP_bar.get_bar() + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)
