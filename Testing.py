# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Characters, Equipment, DDProg

#Testsuite
def Test1():
  combat = DDProg.Combat_Round()
  combat.add_combatant('Kandorn')
  combat.combatants['Kandorn'].generate_attributes()
  combat.combatants['Kandorn'].calculate_stats()
  combat.combatants['Kandorn'].print_stats()
  combat.combatants['Kandorn'].print_actions()
  combat.combatants['Kandorn'].equip_weapon(Equipment.Longsword())
  combat.combatants['Kandorn'].print_equipped_items()
  combat.add_combatant('Orc')
  combat.combatants['Orc'].generate_attributes()
  combat.combatants['Orc'].calculate_stats()
  combat.combatants['Orc'].print_stats()
  for i in range(34):
    print combat.combatants
    combat.combatants['Kandorn'].actions[0].attack(combat.combatants['Orc'])
    combat.combatants['Orc'].actions[0].attack(combat.combatants['Kandorn'])

def Test2():
  combat = DDProg.Combat()
  combat.add_combatant('Ryker')
  combat.combatants['Ryker'].attributes['dex'].setvalue(12)
  combat.add_combatant('Orc')
  combat.combatants['Orc'].attributes['dex'].setvalue(12)
  combat.add_combatant('Goblin1')
  combat.combatants['Goblin1'].attributes['dex'].setvalue(12)
  combat.add_combatant('Goblin2')
  combat.combatants['Goblin2'].attributes['dex'].setvalue(12)
  combat.add_combatant('Goblin3')
  combat.combatants['Goblin3'].attributes['dex'].setvalue(12)
  combat.process()

#Test1()
Test2()