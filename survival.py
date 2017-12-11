# Survival game
# INCOMPLETE

from random import randint

# resources
food = 0
water = 0
wood = 0
stone = 0
diamond = 0

# fighting
attack = 1
defense = 1
health = 10

# farming
axe = 0
pickaxe = 0

# game stats
turn = 0
killed = 0

########### MONSTERS #############
### easy monsters ###
def monster_easy(health, food, turn, killed):
	chance = randint(0, 2)
	if chance == 2:
		m_health = 2
		print('You have been attacked!')
		print('Monster has', m_health, 'health.')
		while m_health != 0:
			health -= 1
			m_health = m_health - attack
			print("You attacked!")
			print("Monster now has", m_health, "health left, and you have", health, "left.")
			if health == 0:
				print("You were killed! Try again.")
				break
		if m_health == 0:
			print('You have defeated the monster!')
			food += 1
			turn += 1
			killed += 1
			print('You now have', food, "food, and", health, "health.")

########### MATERIALS #############
### wood ###
def getting_wood():
	if axe == 0:
		wood += 1
		turn += 4
		monster_easy(health, food, turn, killed)
		monster_easy(health, food, turn, killed)
	elif axe == 1:

##################
## MAIN PROGRAM ##
##################
print("""Welcome! Try to survive as long as you can! First, you'll want to craft some weapons so that oyu can defend yourself from monsters.\n Type 'craft' to get a list of things you can make, or 'help' to get a list of what you can do.""")

while health > 0:
	command = input('\nWhat do you want to do? ')
	turn += 1
	if command == 'craft':
		print("""		* Wooden sword - 6 wood
		* Stone sword - 10 stone
		* Diamond sword - 4 diamonds
		* Wooden pickaxe - 4 wood
		* Stone pickaxe - 6 stone
		* Diamond pickaxe - 3 diamonds""")
	elif command == 'help':
		print("""You want to make an axe so you can get wood. Type 'wood' in order to start getting wood. Without an axe, it will take more turns and you are more likely to get attacked. After this, try to make a pickaxe from wood to get stone. To make an axe, type 'craft axe'.""")
	elif command == 'wood':
		
	elif command == 'craft axe':
		material = input('Out of what? ')
		if material == 'wood':
			axe = 1
			print('Wood axe crafted!')
		elif material == 'stone':
			axe = 2
			print('Stone axe crafted!')
		elif material == 'diamond':
			axe = 3
			print('Diamond axe crafted!')
	
if health == 0:
	print('You died! You survived', turns, 'turns, and killed', killed, "monsters.")