# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Equipment, PlayerCharacters, Combat, Monster

combat = Combat.Combat()

#def Test1():
  #for being in ['Goblin1', 'Goblin2']:
    #combatant = Characters.Character(being)
    #combatant.generate_attributes()
    #combatant.calculate_stats()
    #combatant.equip_weapon(Equipment.Longsword())
    #combat.add_combatant(combatant)
    #combatant.show_stats()
  #combat.process()
  
#def Test2():
  #for being in ['Kandorn']:
    #combatant = Characters.Character(being)
    #combatant.generate_attributes()
    #combatant.calculate_stats()
    #combatant.equip_weapon(Equipment.Longsword())
    #combat.add_combatant(combatant)
    #combatant.show_stats()
  #combat.add_combatant(Monster.GoblinBlackblade())
  #combat.process()
  
def Test3():
  combat.add_combatant(PlayerCharacters.Kurt())
  combat.add_combatant(Monster.GoblinBlackblade())
  combat.process()
  
Test3()