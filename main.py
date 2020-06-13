from classes.game import Person, bcolors
from classes.magic import magic
from classes.inventory import item
import random

# region defining magics
fire = magic("Fire", 10, 100, "Black")
thunder = magic("Thunder", 12, 120, "Black")
blizzard = magic("Blizzard", 14, 140, "Black")
darin = magic("Drain", 16, 160, "Black")
osmose = magic("Osmose", 18, 180, "Black")
fira = magic("Fira", 20, 200, "Black")
alvin = magic("Alvin", 10, 100, "White")
arion = magic("Arion", 12, 120, "White")
argus = magic("Argus", 14, 140, "White")
ambrose = magic("Ambrose", 16, 160, "White")
aelfdene = magic("Aelfdene", 18, 180, "White")
aeamus = magic("Aeamus", 20, 200, "White")
player_magics = [fire, blizzard, osmose, alvin, argus, aeamus]
#endregion

# region defining items
potion = item("Potion", "potion", "It heals for 50 HP", 200)
super_potion = item("Super Potion", "potion", "It heals for 500 HP", 500)
elixir = item("Elixir", "elixir", "It fully restores HP/MP of a player", 0)
super_elixir = item("Super Elixir", "elixir", "It fully restores HP/MP of all team members", 0)
grenade = item("Grenade", "attack", "Makes 50 damages", 200)
bomb = item("Bomb", "attack", "Makes 500 damages", 500)
player_items = [{"name": potion, "quant": 1}, {"name": super_potion, "quant": 1},
				{"name": elixir, "quant": 1}, {"name": super_elixir, "quant": 1},
				{"name": grenade, "quant": 1}, {"name": bomb, "quant": 1}]
#endregion

# region defining people
p1 = Person("Velo", 1000, 99, 200, player_magics, player_items)
p2 = Person("Nick", 3000, 25, 50, player_magics, player_items)
p3 = Person("Hohn", 2000, 50, 100, player_magics, player_items)
players = [p1, p2, p3]
# endregion

# region defining enemies
e1 = Person("Gian", 3000, 0, 300, [], [])
e2 = Person("Sion", 1000, 0, 50, [], [])
e3 = Person("Sito", 1000, 0, 50, [], [])
enemies = [e1, e2, e3]
#endregion

# main game procedure
running = True
while running:

	# priniting people and enemies status
	print("\n" + "Name              HP                                         MP")
	for player in players:
		player.get_player_status()
	for enemy in enemies:
		enemy.get_enemy_status()

	# players phase
	for player in players:

		# is player alive?
		if player.get_hp() > 0:

			# showing who is playing
			print("\n" + player.name + " is playing!")

			# choosing action by who is now playing
			selected_action = player.choose_action()

			# if player chooses to attack
			if selected_action == 0:

				# choosing target enemy by who is now playing
				selected_enemy = player.choose_enemy(enemies)

				# applying damage
				enemies[selected_enemy].take_damage(player.generate_damage())
				print(bcolors.OKGREEN + "You attacked " + enemies[selected_enemy].name + " for " +
					  str(player.generate_damage()) + " points of damage." + bcolors.ENDC)

			# if player chooses to use magic
			elif selected_action == 1:

				# choosing magic by who is now playing
				selected_magic_index = player.choose_magic()
				selected_magic = player.magic_array[selected_magic_index]

				# returning to main menu
				if selected_magic_index == -1:
					continue

				# going on
				else:

					# if player dont have enough mp to use magic
					if player.get_mp() < selected_magic.cost:
						print(bcolors.FAIL + "You dont have enough magic points!" + bcolors.ENDC)

					# if player has enough mp to use magic
					else:

						# reducing mp
						player.reduce_mp(selected_magic.cost)

						# using white magic to heal player/players
						if selected_magic.type == "White":
							player.take_heal(selected_magic.damage)
							print(bcolors.OKBLUE + "You used your magic power to heal yourself for " + str(
								selected_magic.damage) + " points of HP." + bcolors.ENDC)

						# using black magic to make some damage! YAH!
						elif selected_magic.type == "Black":
							# choosing target enemy by who is now playing
							selected_enemy = player.choose_enemy(enemies)
							# applying damage
							enemies[selected_enemy].take_damage(selected_magic.damage)
							print(bcolors.OKBLUE + "You used your magic power to attack " + enemies[selected_enemy].name +
								" for " + str(selected_magic.damage) + " points of damage." + bcolors.ENDC)

			# if player chooses to use item
			elif selected_action == 2:

				# choosing magic by who is now playing
				selected_item_index = player.choose_item()
				# returning to main menu

				if selected_item_index == -1:
					continue

				# going on
				else:

					# if there is not enough quantity of that item
					if player.item_array[selected_item_index]["quant"] == 0:
						print(bcolors.FAIL + "No item of this type is remained." + bcolors.ENDC)
						continue

					# updating number of items available
					player.item_array[selected_item_index]["quant"] -= 1

					# intriducing selected item by its name
					selected_item = player.item_array[selected_item_index]["name"]

					# if player wants to use potion
					if selected_item.type == "potion":
						player.take_heal(selected_item.amount)
						print(bcolors.OKBLUE + "You used your " + selected_item.name + " to heal yourself for " + str(
							selected_item.amount) + " points of HP." + bcolors.ENDC)

					# if player wants to use elixir
					elif selected_item.type == "elixir":

						# if player wants to heal team
						if selected_item.name == "Super Elixir":
							for player in players:
								player.hp = player.maxhp
								player.mp = player.maxmp
								print(bcolors.OKBLUE + "You used your " + selected_item.name +
									  " to fully recover your team." + bcolors.ENDC)

						# if player wants to heal himself
						player.hp = player.maxhp
						player.mp = player.maxmp
						print(bcolors.OKBLUE + "You used your " + selected_item.name + " to fully recover your HP and MP."
							  + bcolors.ENDC)

					# if player wants to make big damage on enemies
					elif selected_item.type == "attack":

						# choosing target enemy by who is now playing
						selected_enemy = player.choose_enemy(enemies)

						# applying damage
						enemies[selected_enemy].take_damage(selected_item.amount)
						print(bcolors.OKBLUE + "You used your " + selected_item.name + " to attack "
							  + enemies[selected_enemy].name + " for " + str(selected_item.amount) + " points of damage."
							  + bcolors.ENDC)

	# setting up a flag which shows you have been defeated
	lose_flag = 0
	for player in players:
		if player.get_hp() == 0:
			lose_flag += 1

	# setting up a flag which shows you win
	win_flag = 0
	for enemy in enemies:
		if enemy.get_hp() == 0:
			win_flag += 1

	# do you win?
	if win_flag == len(enemies):
		print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
		running = False
		continue

	# have you been defeated?
	elif lose_flag == len(players):
		print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
		running = False
		continue

	#enemies phase
	for enemy in enemies:

		# is player alive?
		if enemy.get_hp() > 0:

			# showing who is playing
			print("\n" + enemy.name + " is playing!")

			# applying damage
			enemy_damage = enemy.generate_damage()
			enemy_choice = random.randrange(0, len(players))
			players[enemy_choice].take_damage(enemy_damage)
			print(bcolors.FAIL + "Enemy attacked " + players[enemy_choice].name + " for " + str(enemy_damage) +
				  " damages" + bcolors.ENDC)

			#it is done.