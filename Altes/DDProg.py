# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Equipment, Characters

class Combat(object):
  def __init__(self):
    self.characters = {}
    self.combatants = {}
    self.inilist = {}
    
  def add_combatant(self, combatant):
    self.combatants[combatant.name] = combatant
    self.characters[combatant.name] = combatant
    combatant.combat = self
    
  def del_combatant(self, combatant):
    del self.combatants[combatant.name]
    
  def roll_initiative(self):
    print 'INITIATIVE'
    print '#####'
    for combatant in self.combatants.itervalues():
      inivalue = random.randint(1,20) + combatant.ini_bonus
      self.inilist[combatant] = inivalue
      #Fuer Testzwecke
      print combatant.name, '->> ', str(inivalue)
  
  def show_combatants(self):
    print 'COMBATANTS'
    print '#####'
    for combatant in self.combatants.itervalues():
      print combatant.name
    print '#####'
    print ''
    
  def process(self):
    self.roll_initiative()
    combat_round = 1
    while len(self.combatants) > 1:
      Combat_Round(self, combat_round).process_round()
      combat_round += 1

class Combat_Round(object):
  def __init__(self, combat, count):
    self.combat = combat
    self.characters = self.combat.characters
    #self.combatants = self.combat.combatants
    self.acts_this_round = {}
    self.count = count
    for combatant in self.combat.combatants.itervalues():
      self.acts_this_round[combatant.name] = combatant
        
  def process_round(self):
    #for combatant in self.combat.combatants.itervalues():
    #  combatant.calculate_stats()
    print ''
    print '#####'
    print 'ROUND', self.count
    print '#####'
    print ''
    self.combat.show_combatants()
    max_ini = max(self.combat.inilist.itervalues())
    min_ini = min(self.combat.inilist.itervalues())
    for ini_turn in range(max_ini, min_ini -1, -1):
      Turn(ini_turn, self).process_ini_turn()
    
class Turn(object):
  def __init__(self, count, combat_round):
    self.acts_this_turn = []
    self.turn_count = count
    self.combat_round = combat_round
    
  def process_ini_turn(self):
    #print ''
    #print '#####'
    #print 'INI-TURN', self.turn_count
    #print '#####'   
    for combatant in self.combat_round.acts_this_round.itervalues():
      if self.turn_count == self.combat_round.combat.inilist[combatant]:
	self.acts_this_turn.append(combatant)
    for char in self.acts_this_turn:
      print '#####'
      print char.name, 'acts this turn (Turn', self.turn_count, ')'
      print '#####'
      print ''
    while self.acts_this_turn != []:
      active_character = self.determine_active_character()
      active_character.process_combatant()
      self.acts_this_turn.remove(active_character)
      del self.combat_round.acts_this_round[active_character.name]
    #print '#####'
    #print ''

  def determine_active_character(self):
    if len(self.acts_this_turn) > 1:
      print 'Same Initiative. Comparing Ini Modifier'
      ini_mod_dic = {}
      for combatant in self.acts_this_turn:
	ini_mod_dic[combatant] = combatant.ini_bonus
        print combatant.name, '->> Ini modifier', combatant.ini_bonus
      max_ini_mod = max(ini_mod_dic.itervalues())
      min_ini_mod = min(ini_mod_dic.itervalues())
      for ini_mod in range(max_ini_mod, min_ini_mod -1, -1):
	now_ini_mod_list = []
	for combatant in self.acts_this_turn:
	  if ini_mod == ini_mod_dic[combatant]:
	    now_ini_mod_list.append(combatant)
	if len(now_ini_mod_list) >1:
	  print 'Same ini modifier. Choosing at random.'
	  choice = random.choice(now_ini_mod_list)
	else:
	  choice = combatant
    if len(self.acts_this_turn) == 1:
      choice = self.acts_this_turn[0]
    print '->>', choice.name, 'acts now'
    return choice