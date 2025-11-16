from classes.classes import *
from classes.objects import *
import random, time

def battle(player, enemy):
    print(f'{enemy.name} appeared!')
    time.sleep(1)
    print('The fight is starting now!')
    time.sleep(1)
    if toss_coin():
        print('\nYou will be first!')
        main = player
        other = enemy
    else:
        print('\nEnemy will be first!')
        main = enemy
        other = player
    while player.hp > 0 and enemy.hp > 0:
        result = main.turn(other)
        main, other = other, main
        time.sleep(1)
        if result != None:
            del enemy
            return result
        else:
            continue


def toss_coin(message = "Let's see who goes first"):
    print(message , end='')
    for i in range(3):
        print('.', end ='')
        time.sleep(0.3)
    if random.randint(0, 1) == 0:
        return True
    else:
        return False

def printlogo():
    return ("\n ____  ____   ____                            \n|  _ \\|  _ \\ / ___|   __ _  __ _ _ __ ___   ___ \n| |_) | |_) | |  _   / _` |/ _` | '_ ` _ \\ / _ \\\n|  _ <|  __/| |_| | | (_| | (_| | | | | | |  __/\n|_| \\_\\_|    \\____|  \\__, |\\__,_|_| |_| |_|\\___|\n                     |___/                      \n")

def drop_items(player):
    weapon = random.choice(weapons)
    armor = random.choice(armors)
    healing_item = random.choice(healing_items)
    print('You found some items on the enemy:')
    print(f'1. Weapon: {weapon["name"]} (Damage: {weapon["damage"]}, Multiplier: {weapon["damage_multiplier"]})')
    print(f'2. Armor: {armor["name"]} (Defense: {armor["defense"]})')
    print(f'3. Healing Item: {healing_item["name"]} (Heal Amount: {healing_item["heal_amount"]})')
    choice = None
    while choice not in ['1','2','3']:
        choice = input('Choose an item to pick up (1-3):\n')
    choice = int(choice)
    if choice == 1:
        item = Weapon(**weapon)
    elif choice == 2:
        item = Armor(**armor)
    else:
        item = HealingItem(**healing_item)
    return item

def main():
    while True:
        print(printlogo())
        print('Welcome to the RPG Battle Simulator!')
        print('Choose your class:')
        print('1. Berserk - Super strong attack, low Energy, HP an defense.')
        print('2. Rogue - High energy, low damage, HP and Defense.')
        print('3. Knight - High HP and Defense, moderate Attack, moderate Energy.')
        class_=None
        while class_ not in ["1","2","3"]:
            class_ = (input('Enter the number of your choice:\n'))
        for i in classes[int(class_)-1]['inventory']:
            ind = classes[int(class_)-1]['inventory'].index(i)
            if 'damage' in i:
                item = Weapon(**i)
            elif 'heal_amount' in i:
                item = HealingItem(**i)
            elif 'defense' in i:
                item = Armor(**i)
                classes[int(class_)-1]['base_defense']+=item.defense-(player.defense - player.base_defense)
            else:
                raise ValueError('Unknown item type in inventory. Please check configuration in src/classes/objects.py')
            classes[int(class_)-1]['inventory'][ind] = item
        player = Player(**classes[int(class_)-1])
        player.name = input('Enter your character name:\n')
        for i in range(4):
            res = battle(player, Enemy(**random.choice(enemies)))
            if res:
                print('You won!')
                player.get_an_item(drop_items(player))
                player.regenerate_energy()
                time.sleep(1)
            else:
                print('You lost!')
                del player
                replay = input('Do you want to play again? (y/n):\n')
                if replay.lower() != 'y':
                    print('Thank you for playing! Goodbye!')
                    return
                break
        res = battle(player, Hydra(**hydra))
        if res:
            print('Congratulations! You defeated the Hydra and completed the game!')
            replay = input('Do you want to play again? (y/n):\n')
            if replay.lower() != 'y':
                print('Thank you for playing! Goodbye!')
                return
        else:
            print('You lost!')
            del player
            replay = input('Do you want to play again? (y/n):\n')
            if replay.lower() != 'y':
                print('Thank you for playing! Goodbye!')
                return

main()