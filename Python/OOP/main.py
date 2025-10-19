# from Enemy import *
from Zombie import *
from Ogre import *

# enemy = Enemy()
# enemy1 = Enemy()
# enemy2 = Enemy()
# enemy2.health_points = 100
#
# print(enemy1.health_points)
# print(enemy2.health_points)
#
# enemy.type_of_enemy ='Zombie'
#
# print(f"{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage}")

# print(enemy.health_points)
# zombie = Enemy()
# zombie.type_of_enemy ='Zombie'
# print(zombie.talk())
# print(zombie.walk_forward())
# print(zombie.attack())
# print(zombie.attack_damage)

# zombie = Enemy('Zombie', 10, 1)
# zombie.type_of_enemy ='Ogre'
# print(zombie.attack_damage)
# print(zombie.type_of_enemy)
#
# big_zombie = Enemy('Big Zombie', 100, 10)
# print(big_zombie.attack_damage)

# zombie.__type_of_enemy ='Ogre'
# print(zombie.__type_of_enemy)

# print(zombie.talk())
# print(zombie.__type_of_enemy) # Throws error

# print(zombie.get_type_of_enemy())

zombie = Zombie(10, 1)
print(zombie.get_type_of_enemy())
print(zombie.talk())

print(zombie.spread_disease())

ogre = Ogre(20, 3)

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do an attack of {zombie.attack_damage}')
print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do an attack of {ogre.attack_damage}')

zombie.talk()
ogre.talk()


def battle(e: Enemy):
    e.talk()
    e.attack()


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)
