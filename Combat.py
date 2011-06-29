# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Equipment, Characters, Panel, pygame, InputHandler
from pygame.locals import *

class Combat(object):
  def __init__(self, SCREEN_SIZE, screen):
    self.id = 1
    self.characters = {}
    self.combatants = {}
    self.ini_list = []
    self.panel = Panel.StatusPanel(self, SCREEN_SIZE, screen)
    self.screen = screen
    self.input_handler = InputHandler.InputChecker(self.panel)   

  def add_combatant(self, combatant):
    if not self.characters.has_key(combatant.name):
      self.combatants[combatant.name] = combatant
      self.characters[combatant.name] = combatant
    else:
      combatant.name = combatant.name + str(self.id)
      self.combatants[combatant.name] = combatant
      self.characters[combatant.name] = combatant
      self.id += 1
    combatant.combat = self
    
  def del_combatant(self, combatant):
    del self.combatants[combatant.name]
    
  def roll_initiative(self):
    panelmessage = ['INITIATIVE', '#####']
    for combatant in self.combatants.itervalues():
      inivalue = random.randint(1,20) + combatant.ini_bonus
      self.ini_list.append([inivalue, combatant.ini_bonus, 0, combatant])
      panelmessage.append(combatant.name + ' ->> ' + str(inivalue))
    self.panel.send_message(panelmessage)
      
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
    self.ini_list = self.combat.ini_list
    self.characters = self.combat.characters
    self.count = count
    
  def get_init_list(self):
    return self.combat.ini_list
        
  def process_round(self):
    self.panel.send_caption('ROUND' + str(self.count))
    self.sort_ini()
    for entry in self.ini_list:
      entry[3].process_combatant()

  
  def sort_ini(self):
    ini_list = self.ini_list
    number_list = range(len(ini_list))
    for item in ini_list:
      item[2] = random.choice(number_list)
      number_list.remove(item[2])
    ini_list.sort()
    ini_list.reverse()