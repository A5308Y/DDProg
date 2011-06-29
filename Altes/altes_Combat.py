# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Equipment, Characters, Panel, pygame, InputHandler
from pygame.locals import *

class Combat(object):
  def __init__(self, SCREEN_SIZE, screen):
    self.characters = {}
    self.combatants = {}
    self.inilist = {}
    self.ini_list = []
    self.panel = Panel.StatusPanel(self, SCREEN_SIZE, screen)
    self.screen = screen
    self.input_handler = InputHandler.InputChecker(self.panel)
    
  def add_combatant(self, combatant):
    self.combatants[combatant.name] = combatant
    self.characters[combatant.name] = combatant
    combatant.combat = self
    
  def del_combatant(self, combatant):
    del self.combatants[combatant.name]
    
  def roll_initiative(self):
    self.panel.send_message('INITIATIVE')
    self.panel.send_message('#####')
    for combatant in self.combatants.itervalues():
      inivalue = random.randint(1,20) + combatant.ini_bonus
      self.inilist[combatant] = inivalue
      #Fuer Testzwecke
      self.panel.send_message(combatant.name + '->> ' + str(inivalue))
  
  def show_combatants(self):
    self.panel.send_message('COMBATANTS')
    self.panel.send_message('#####')
    for combatant in self.combatants.itervalues():
      self.panel.send_message(combatant.name)
    self.panel.send_message('#####')
    self.panel.send_message('')
    
    
    
  def process(self):
    self.roll_initiative()
    self.panel.draw_panel()
    combat_round = 1
    while len(self.combatants) > 1:
      Combat_Round(self, combat_round).process_round()
      combat_round += 1




class Combat_Round(object):
  def __init__(self, combat, count):
    self.panel = combat.panel
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
    self.panel.send_message('')
    self.panel.send_message('#####')
    self.panel.send_message('ROUND' + str(self.count))
    self.panel.send_message('#####')
    self.panel.send_message('')
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
    self.panel = combat_round.panel
    self.combat = self.combat_round.combat
    
  def process_ini_turn(self):
    self.combat.panel.draw_panel()
    pygame.display.update()
    for combatant in self.combat_round.acts_this_round.itervalues():
      if self.turn_count == self.combat_round.combat.inilist[combatant]:
	self.acts_this_turn.append(combatant)
    for char in self.acts_this_turn:
      self.panel.send_message(char.name + 'acts this turn (Turn' + str(self.turn_count) + ')')
    while self.acts_this_turn != []:
      active_character = self.determine_active_character()
      active_character.process_combatant()
      self.acts_this_turn.remove(active_character)
      del self.combat_round.acts_this_round[active_character.name]

  def determine_active_character(self):
    if len(self.acts_this_turn) > 1:
      self.panel.send_message('Same Initiative. Comparing Ini Modifier')
      ini_mod_dic = {}
      for combatant in self.acts_this_turn:
	ini_mod_dic[combatant] = combatant.ini_bonus
 #       print combatant.name, '->> Ini modifier', combatant.ini_bonus
      max_ini_mod = max(ini_mod_dic.itervalues())
      min_ini_mod = min(ini_mod_dic.itervalues())
      for ini_mod in range(max_ini_mod, min_ini_mod -1, -1):
	now_ini_mod_list = []
	for combatant in self.acts_this_turn:
	  if ini_mod == ini_mod_dic[combatant]:
	    now_ini_mod_list.append(combatant)
	if len(now_ini_mod_list) >1:
	  self.panel.send_message('Same ini modifier. Choosing at random.')
	  choice = random.choice(now_ini_mod_list)
	if len(now_ini_mod_list) == 1 :
	  choice = now_ini_mod_list[0]
    if len(self.acts_this_turn) == 1:
      choice = self.acts_this_turn[0]
    self.panel.send_message('->>' + choice.name + 'acts now')
    return choice