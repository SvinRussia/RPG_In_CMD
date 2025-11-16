
# Weapon
weapons = [
{'name':"Fire Sword", 'damage':-5, 'damage_multiplier':3.0},
{'name':"Ice Dagger", 'damage':15, 'damage_multiplier':0.8},
{'name':"Wind Hammer", 'damage':8, 'damage_multiplier':1.5},
{'name':"Earth Axe", 'damage':-10, 'damage_multiplier':6.0}
]

# Boss weapon
boss_weapons = [{'name':"Dark Blade", 'damage':-15, 'damage_multiplier':24.0}, {'name':"Rapire of Light", 'damage':120, 'damage_multiplier':0.8}]

# Heal
healing_items = [{'name':"Small Potion", 'heal_amount':15}, {'name':'Medium Potion', 'heal_amount':35}, {'name':"Large Potion", 'heal_amount':55}]

# Armor
armors = [{'name': "Leather Jacket", 'defense': 1.5}, {'name': "Iron Armor", 'defense': 2}, {'name': "Steel Armor", 'defense': 2.5}]

# Enemies
enemies = [{'name': "Orc", 'base_hp': 60, 'base_attack': 25, 'base_defense': 1.3, 'base_energy': 1},
{'name': "Goblin", 'base_hp': 30, 'base_attack': 34, 'base_defense': 1.2, 'base_energy': 1},
{'name': "Troll", 'base_hp': 80, 'base_attack': 20, 'base_defense': 1.4, 'base_energy': 2},
{'name': "Fog Killer", 'base_hp': 10, 'base_attack': 30, 'base_defense': 0.8, 'base_energy': 2}]

# Bosses
hydra = {'name': "Hydra", 'base_hp': 160, 'base_attack': 50, 'base_defense': 2.5, 'base_energy': 2}

# Classes
classes = [{'name' : None, 'base_hp' : 100, 'base_attack' : 35, 'base_defense' : 1.4, 'base_energy' : 1, 'inventory' : [{'name':"Base Axe", 'damage':10, 'damage_multiplier':1.2}, {'name':'Medium Potion', 'heal_amount':35}]},
{'name':None, 'base_hp' : 80, 'base_attack' : 10, 'base_defense' : 1.0, 'base_energy' : 3, 'inventory' : [{'name':"Base Dagger", 'damage':2, 'damage_multiplier':1.5},{'name':'Medium Potion', 'heal_amount':35}]},
{'name' : None, 'base_hp' : 150, 'base_attack' : 20, 'base_defense' : 1.8, 'base_energy' : 2, 'inventory' : [{'name':"Base Sword", 'damage':10, 'damage_multiplier':1.2}, {'name':'Medium Potion', 'heal_amount':35}]}]