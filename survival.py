# Survival game
# INCOMPLETE

from random import randint
from time import sleep

running = True

# resources
food = 0
wood = 0
stone = 0
diamond = 0
leather = 0
feathers = 0

# fighting
attack = 1
defense = 1
rawhealth = 20
health = 20

# farming
axe = 0
pickaxe = 0

# game stats
turn = 0
killed = 0
quests_completed = 0

quest = False

###############################################################
############################ QUESTS ###########################
###############################################################
def quest_starter():
	global quest
	quest = True
	if turn < 59:
		easy_quest()
	if turn < 119 and turn > 60:
		medium_quest()
	if turn < 240 and turn > 120:
		hard_quest()
	if turn > 241:
		extreme_quest()
		
def easy_quest():
	chance = randint(1, 4)
	global quest
	global feathers
	global quests_completed
	global stone
	if chance == 1:
		print("""A person asks you to bring them 3 feathers.""")
		if feathers >= 3:
			print('You already have 3 feathers. You gave them over. You now have', feathers, 'feathers.')
			feathers -= 3
			quests_completed += 1
			stone += 2
			print('\nThe person thanks you and hands over some stone. You now have', stone, 'stone.')
			quest = False
		else:
			print('\nGo find three feathers.')
			while quest is True:		
				print('\nYou go exploring to try and find some feathers.')
				sleep(1)
				explore()
				if feathers >= 3:
					print('You already have 3 feathers. You gave them over. You now have', feathers, 'feathers.')
					feathers -= 3
					quests_completed += 1
					stone += 2
					print('\nThe person thanks you and hands over some stone. You now have', stone, 'stone.')
					quest = False
					break
	if chance == 2:
		print("""You come across...""")
	if chance == 3:
		print("""You come across...""")

def explore():
	chance = randint(1, 20)
	if chance <= 12:
		chance = randint(1, 2)
		if chance == 1:
			cow()
		if chance == 2:
			chicken()
	elif chance >= 15:
		battle()
	else:
		print('You found nothing!')
###############################################################
############################ ANIMALS ##########################
###############################################################
### cow ###
def cow():
	global food
	global leather
	global turn
	print('You encounter and attack a cow.')
	turn += 1
	sleep(1)
	chance = randint(0, 4)
	if chance == 1:
		food += 1
		print('You got some food. You now have', food, 'food.')
	if chance == 2:
		leather += 2
		print('You found some leather. You now have', leather, 'leather.')
	else:
		print('You found nothing!')

### chicken ###
def chicken():
	global food
	global turn
	global feathers
	print('You encounter and attack a chicken.')
	turn += 1
	sleep(1)
	chance = randint(0, 1)
	if chance == 1:
		food += 1
		print('You got some food. You now have', food, 'food.')
	else:
		feathers += 1
		print('You found a feather! You now have', feathers, 'feathers.')

###############################################################
############################ MONSTERS #########################
###############################################################
def battle():
	if turn < 100:
		monster_easy()
	elif turn > 100 and turn < 200:
		monster_medium()
	elif turn > 300:
		monster_hard()

### easy monsters ###
def monster_easy():
	global health
	global food
	global turn
	global killed
	chance = randint(0, 2)
	if chance == 2:
		m_health = 4
		print('\nYou have been attacked!')
		sleep(1)
		print('Monster has', m_health, 'health.')
		sleep(1)
		while m_health != 0:
			health -= 1
			m_health = m_health - attack
			print("\nYou attacked!")
			sleep(0.5)
			print("Monster now has", m_health, "health left, and you have", health, "left.")
			sleep(0.5)
			if health == 0:
				print("You were killed! Try again.")
				break
		if m_health == 0:
			print('\nYou have defeated the monster!\n')
			food += 1
			turn += 1
			killed += 1
			print('You now have', food, "food, and", health, "health.")

### medium monsters ###
def monster_medium():
	global health
	global food
	global turn
	global killed
	chance = randint(0, 5)
	if chance == 2:
		m_health = 20
		print('\nYou have been attacked!')
		sleep(1)
		print('Monster has', m_health, 'health.')
		sleep(1)
		while m_health != 0:
			health -= 5
			m_health = m_health - attack
			print("\nYou attacked!")
			sleep(0.5)
			print("Monster now has", m_health, "health left, and you have", health, "left.")
			sleep(0.5)
			if health == 0:
				print("You were killed! Try again.")
				break
		if m_health == 0:
			print('\nYou have defeated the monster!\n')
			food += 2
			turn += 1
			killed += 1
			print('You now have', food, "food, and", health, "health.")
			
### hard monsters ###
def monster_hard():
	global health
	global food
	global turn
	global killed
	chance = randint(0, 9)
	if chance == 2:
		m_health = 45
		print('\nYou have been attacked!')
		sleep(1)
		print('Monster has', m_health, 'health.')
		sleep(1)
		while m_health != 0:
			health -= 8
			m_health = m_health - attack
			print("\nYou attacked!")
			sleep(0.5)
			print("Monster now has", m_health, "health left, and you have", health, "left.")
			sleep(0.5)
			if health == 0:
				print("You were killed! Try again.")
				break
		if m_health == 0:
			print('\nYou have defeated the monster!\n')
			food += 3
			turn += 1
			killed += 1
			print('You now have', food, "food, and", health, "health.")

###############################################################
######################### MATERIALS ###########################
###############################################################
### wood ###
def getting_wood():
	global wood
	global turn
	if axe == 0:
		wood += 1
		turn += 4
		if turn < 100:
			for _ in range(4):
				monster_easy()
		if turn < 200 and turn > 300:
			for _ in range(4):
				monster_medium()
		if turn > 300:
			for _ in range(4):
				monster_hard()
		print('You now have', wood, 'wood.')
	elif axe == 1:
		wood += 1
		turn += 3
		if turn < 100:
			for _ in range(3):
				monster_easy()
		if turn < 200 and turn > 300:
			for _ in range(3):
				monster_medium()
		if turn > 300:
			for _ in range(3):
				monster_hard()
		print('You now have', wood, 'wood.')
	elif axe == 2:
		wood += 1
		turn += 2
		if turn < 100:
			for _ in range(2):
				monster_easy()
		if turn < 200 and turn > 300:
			for _ in range(2):
				monster_medium()
		if turn > 300:
			for _ in range(2):
				monster_hard()
		print('You now have', wood, 'wood.')
	elif axe == 3:
		wood += 1
		turn += 1
		if turn < 100:
			monster_easy()
		if turn < 200 and turn > 300:
			monster_medium()
		if turn > 300:
			monster_hard()
		print('You now have', wood, 'wood.')

### stone ###
def getting_stone():
	global stone
	global turn
	if pickaxe == 0:
		stone += 1
		turn += 4
		if turn < 100:
			for _ in range(4):
				monster_easy()
		if turn < 200:
			for _ in range(4):
				monster_medium()
		if turn < 300:
			for _ in range(4):
				monster_hard()
		print('You now have', stone, 'stone.')
	elif pickaxe == 1:
		stone += 1
		turn += 3
		if turn < 100:
			for _ in range(3):
				monster_easy()
		if turn < 200 and turn > 300:
			for _ in range(3):
				monster_medium()
		if turn > 300:
			for _ in range(3):
				monster_hard()
		print('You now have', stone, 'stone.')
	elif pickaxe == 2:
		stone += 1
		turn += 2
		if turn < 100:
			for _ in range(2):
				monster_easy()
		if turn < 200 and turn > 300:
			for _ in range(2):
				monster_medium()
		if turn > 300:
			for _ in range(2):
				monster_hard()
		print('You now have', stone, 'stone.')
	elif pickaxe == 3:
		stone += 1
		turn += 1
		if turn < 100:
			monster_easy()
		if turn < 200 and turn > 300:
			monster_medium()
		if turn > 300:
			monster_hard()
		print('You now have', stone, 'stone.')

############ HEALTH ##############
### eating food ###
def eat_food():
	global food
	global health
	if food >= 1:
		food -= 1
		health += 2
		print('You have eaten food. You now have', food, 'food and your health is now', health, '.')
	else:
		print('You do not have enough food. You only have', food, 'food.')

############################################################
############################################################
############################################################
####################### MAIN PROGRAM #######################
############################################################
############################################################
############################################################

print("""Welcome! Try to survive as long as you can! First, you'll want to craft some weapons so that you can defend yourself from monsters.

Type 'craft' to get a list of things you can make, or 'help' to get a list of what you can do. Type in 'i' to view your inventory and see how many resources you have, and 'f' to see how much food and water you have. to see all commands, thpe 'commands'.""")

while health > 0:
	truehealth = defense * rawhealth
	health = int(round(truehealth))
	command = input('\n\nWhat do you want to do? ')
	turn += 1
	
	if command == 'commands':
		print("""
		Commands - Command lost
		Help - Get an idea of what to do
		Craft - Craft items
		i - Inventory items
		f - Food item stats
		h - Health stats
		wood - Get wood
		stone - Get stone
		craft axe - Craft an axe
		craft pickaxe - Craft a pickaxe
		craft sword - Craft a sword
		craft armour - Craft armour
		eat - Heal yourself
		explore - Go exploring, encounter monsters, animals etc
		quest - Get a quest and complete it
		""")
		
	##################### QUESTS #####################
	if command == 'quest':
		quest_starter()
	
	if command == 'c':
		chicken()
	##################### CRAFTING GUIDE #####################
	if command == 'craft':
		print("""
		* Wooden sword - 6 wood
		* Stone sword - 10 stone
		* Diamond sword - 4 diamonds
		* Wooden pickaxe - 4 wood
		* Stone pickaxe - 6 stone
		* Diamond pickaxe - 3 diamonds
		* Wooden axe - 4 wood
		* Stone axe - 4 stone
		* Diamond axe - 2 diamonds""")
		
	##################### INVENTORY ITEMS #####################
	elif command == 'i':
		print('Wood -', wood)
		print('Stone -', stone)
		print('Diamond -', diamond)
		print('Leather -', leather)
		
	##################### FOOD AND WATER LIST #####################
	elif command == 'f':
		print('Food -', food)
		print('Water -', water)
	
	##################### HEALTH STATS #####################
	elif command == 'h':
		print('Health -', health)
		print('Armour -', defense)
		
	##################### HELP GUIDE #####################
	elif command == 'help':
		print("""
		You want to make an axe so you can get wood. Type 'wood' in order to start getting wood. Without an axe, it will take more turns and you are more likely to get attacked. After this, try to make a pickaxe from wood to get stone. To make an axe, type 'craft axe'. Type in 'i' to view your inventory and see how many resources you have, and 'f' to see how much food and water you have.""")
		
	##################### GETTING WOOD #####################
	elif command == 'wood':
		getting_wood()
	
	##################### GETTING STONE #####################
	elif command == 'stone':
		getting_stone()
		
	##################### CRAFTING AXE #####################
	elif command == 'craft axe':
		material = input('Out of what? ')
		if material == 'wood':
			if wood > 3:
				axe = 1
				wood -= 4
				print('Wood axe crafted!')
			else:
				print('You don\'t have enough resources! You only have', wood, 'wood.')
		elif material == 'stone':
			if stone > 3:
				axe = 2
				stone -= 4
				print('Stone axe crafted!')
			else:
				print('You don\'t have enough resources! You only have', stone, 'stone.')
		elif material == 'diamond':
			if diamond > 1:
				axe = 3
				diamond -= 1
				print('Diamond axe crafted!')
			else:
				print('You don\'t have enough resources! You only have', diamond, 'diamond.')
				
	##################### CRAFTING PICKAXE #####################
	elif command == 'craft pickaxe':
		material = input('Out of what? ')
		if material == 'wood':
			if wood > 3:
				pickaxe = 1
				wood -= 4
				print('Wood pickaxe crafted!')
			else:
				print('You don\'t have enough resources! You only have', wood, 'wood.')
		elif material == 'stone':
			if stone > 5:
				pickaxr = 2
				stone -= 6
				print('Stone pickaxe crafted!')
			else:
				print('You don\'t have enough resources! You only have', stone, 'stone.')
		elif material == 'diamond':
			if diamond > 2:
				pickaxe = 3
				diamond -= 3
				print('Diamond pickaxe crafted!')
			else:
				print('You don\'t have enough resources! You only have', diamond, 'diamond.')
				
	##################### CRAFTING SWORD #####################
	elif command == 'craft sword':
		material = input('Out of what? ')
		if material == 'wood':
			if wood > 5:
				attack = 3
				wood -= 6
				print('Wood sword crafted!')
			else:
				print('You don\'t have enough resources! You only have', wood, 'wood.')
		elif material == 'stone':
			if stone > 9:
				attack = 5
				stone -= 10
				print('Stone sword crafted!')
			else:
				print('You don\'t have enough resources! You only have', stone, 'stone.')
		elif material == 'diamond':
			if diamond > 3:
				attack = 8
				diamond -= 4
				print('Diamond sword crafted!')
			else:
				print('You don\'t have enough resources! You only have', diamond, 'diamond.')
	
	##################### CRAFTING ARMOUR #####################
	elif command == 'craft armour':
		material = input('Out of what? ')
		if material == 'wood':
			if wood > 19:
				defense = 1.5
				wood -= 20
				print('Wooden armour crafted!')
			else:
				print('You don\'t have enough resources! You only have', wood, 'wood.')
		elif material == 'stone':
			if stone > 29:
				defense = 2
				stone -= 30
				print('Stone armour crafted!')
			else:
				print('You don\'t have enough resources! You only have', stone, 'stone.')
		elif material == 'diamond':
			if diamond > 29:
				defense = 3
				diamond -= 30
				print('Diamond armour crafted!')
			else:
				print('You don\'t have enough resources! You only have', diamond, 'diamond.')
		elif material == 'leather':
			if leather > 11:
				defense = 1.88
				leather -= 12
				print('Leather armour crafted!')
			else:
				print('You don\'t have enough resources! You only have', leather, 'leather.')

	##################### EATING #####################
	elif command == 'eat':
		eat_food()
		
	##################### EXPLORING #####################
	elif command == 'explore':
		explore()

if health <= 0:
	running = False
	print('You died! You survived', turn, 'turns, and killed', killed, "monsters. Thanks for playing, try again soon!")
