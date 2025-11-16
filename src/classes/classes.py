import random, time

class Mob:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.base_hp = kwargs['base_hp']
        self.hp = kwargs['base_hp']
        self.base_attack = kwargs['base_attack']
        self.base_defense = kwargs['base_defense']
        self.defense = kwargs['base_defense']
        self.base_energy = kwargs['base_energy']
        self.energy = kwargs['base_energy']

    def regenerate_energy(self):
        self.energy = self.base_energy

class Player(Mob):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = kwargs['inventory']

    def check_inventory(self):
        count=1
        for i in self.inventory:
            if type(i) == Weapon:
                stats = f"Weapon Damage: {i.damage}, Multiplier: {i.damage_multiplier}"
            elif type(i) == HealingItem:
                stats = f"Healing Amount: {i.heal_amount}"
            elif type(i) == Armor:
                stats = f"Defense: {i.defense}"
            else:
                raise ValueError('Unknown item type in inventory. Please check configuration in src/classes/objects.py')
            print(count, i.name, stats, sep='. ')
            count+=1

    def choose_an_iteam(self, parameter):
        self.check_inventory()
        while True:
            choice = input("Choose an item by index:\n")
            if choice == 'back':
                return 'back'
            else:
                try:
                    choice = int(choice)
                except ValueError:
                    print("Invalid choice.")
                else:
                    try:
                        if type(self.inventory[choice - 1]) == parameter:
                            return self.inventory[choice - 1]
                        else:
                            print("Invalid choice.")
                    except IndexError:
                        print("Invalid choice.")

    def heal(self):
        heal_item = self.choose_an_iteam(HealingItem)
        if heal_item == 'back':
            return True
        heal = heal_item.heal_amount + random.randint(-2, 5)
        self.hp += heal
        self.energy -= 1
        self.inventory.remove(heal_item)
        print(f"You used {heal_item.name}, restoring {heal} HP. Your HP is now {self.hp}.")

    def attack(self, other):
        weapon = self.choose_an_iteam(Weapon)
        if weapon == 'back':
            return True
        damage = round((weapon.damage + (self.base_attack * weapon.damage_multiplier))/other.defense - random.randint(-5, 0))
        other.hp -= damage
        self.energy -= 1
        print(f"You attacked {other.name} with {weapon.name}, dealing {damage} damage. {other.name}'s HP is now {other.hp}.")

    def turn(self, other):
        while self.energy > 0:
            choice = input("1. Attack\n2. Use Healing Item\n3. Check status\nChoose your action:\n")
            while choice not in ["1", "2", "3"]:
                choice = input("Invalid choice. Choose your action:\n")
            if choice == "1":
                to_back = self.attack(other)
            elif choice == "2":
                to_back = self.heal()
            elif choice == "3":
                print(self.name.upper())
                print(f"HP: {self.hp}, Energy: {self.energy}")
                print(f"Defense: {self.defense}, Attack: {self.base_attack}")
                print("Inventory:")
                self.check_inventory()
                print()
                print(other.name.upper())
                print(f"HP: {other.hp}, Energy: {other.energy}")
                print(f"Defense: {other.base_defense}, Attack: {other.base_attack}\n")
                time.sleep(1)
                continue
            if to_back == True:
                continue
            if other.hp <= 0:
                self.regenerate_energy()
                return True
        self.regenerate_energy()
        return None

    def get_an_item(self, other):
        if type(other) == Armor:
            self.defense += other.defense-(self.defense - self.base_defense)
        else:
            self.inventory.append(other)
        print(f"You obtained: {other.name}!")

class Enemy(Mob):
    enemies_spawned = 0

    def __init__(self, **kwargs):
        Enemy.enemies_spawned += 1
        new_atributes = {}
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and key != 'base_energy' and key != 'defense':
                new_atributes[key] = round(value * Enemy.enemies_spawned/2) + 1
            else:
                new_atributes[key] = value
        super().__init__(**new_atributes)

    def attack(self, other):
        damage = round(self.base_attack/other.defense - random.randint(-2, 0))
        other.hp -= damage
        print(f"{self.name} attacked you, dealing {damage} damage! Your HP is now {other.hp}.")
        self.energy -= 1

    def turn(self, other):
        while self.energy > 0:
            if self.hp/self.base_hp < 0.5 and isinstance(self, Boss):
                self.last_breath()
            else:
                self.attack(other)
                if other.hp <= 0:
                    return False
        self.regenerate_energy()
        return None

class Boss(Enemy):
    def last_breath(self):
        print('something is happening...')
        time.sleep(1)
        print(f"{self.name} is powered up!")
        self.hp = self.base_hp
        self.defense = round(self.base_defense*1.5)
        self.base_attack = round(self.base_attack*1.5)

class Hydra(Boss):
    def attack(self, other):
        damage = round(self.base_attack/other.defense - random.randint(-2, 0))
        self.hp += round(damage * 0.5)
        other.hp -= damage
        print(f"{self.name} attacked you, dealing {damage} damage! Your HP is now {other.hp}.")
        self.energy -= 1

class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']

class Weapon(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.damage = kwargs['damage']
        self.damage_multiplier = kwargs['damage_multiplier']

class HealingItem(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heal_amount = kwargs['heal_amount']

class Armor(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.defense = kwargs['defense']
