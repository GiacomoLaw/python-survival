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

# fighting
attack = 1
defense = 1
health = 20

# farming
axe = 0
pickaxe = 0

# game stats
turn = 0
killed = 0

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

### boss monster ###
def boss():
        global health
	global food
	global turn
	global killed
        m_health = 100
        print('\nYou have been attacked by a huge monster!')
        sleep(1)
        print('Monster has', m_health, 'health.')
        sleep(1)
        while m_health != 0:
                health -= 12
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
                food += 6
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

### diamonds ###
def diamonds():
        global diamond
        chance = randint(1, 100)
        if chance == 50:
                print('You found a diamond!')
                diamond += 1
                print('You now have', diamond, 'diamonds.')
                

############ HEALTH ##############
### eating food ###
def eat_food():
	global food
	global health
	if food >= 1:
		food -= 1
		health = health + 2
		print('You have eaten food. You now have', food, 'food and your health is now', health,'.')
	elif food == 0:
		print('You have no food!')




############################################################
####################### MAIN PROGRAM #######################
############################################################
print("""Welcome! Try to survive as long as you can! First, you'll want to craft some weapons so that you can defend yourself from monsters.

Type 'craft' to get a list of things you can make, or 'help' to get a list of what you can do. Type in 'i' to view your inventory and see how many resources you have, and 'f' to see how much food and water you have.""")

while health > 0:
	health = int(round(defense * health))
	command = input('\n\nWhat do you want to do? ')
	turn += 1
	
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
		# print('Water -', water)
	
	##################### INVENTORY ITEMS #####################
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
		chance = randint(1, 20)
		if chance < 4:
			cow()
		elif chance > 12:
			battle()
		else:
			print('You found nothing!')

if health <= 0:
	print('You died! You survived', turn, 'turns, and killed', killed, "monsters. Thanks for playing, try again soon!")
