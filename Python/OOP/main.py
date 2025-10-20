# from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

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

# zombie = Zombie(10, 1)
# print(zombie.get_type_of_enemy())
# print(zombie.talk())
#
# print(zombie.spread_disease())
#
# ogre = Ogre(20, 3)
#
# print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do an attack of {zombie.attack_damage}')
# print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do an attack of {ogre.attack_damage}')
#
# zombie.talk()
# ogre.talk()


# def battle(e: Enemy):
#     e.talk()
#     e.attack()

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('----------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')

        e2.attack()
        e1.health_points -= e2.attack_damage

        e1.attack()
        e2.health_points -= e1.attack_damage
    print('----------')

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')

def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('----------')
        enemy.special_attack()
        print(f'Hero: {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')

        enemy.attack()
        hero.health_points -= enemy.attack_damage

        hero.attack()
        enemy.health_points -= hero.attack_damage
    print('----------')

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie)
# battle(ogre)

# battle(zombie, ogre)
hero_battle(hero, ogre)
hero_battle(hero, zombie)