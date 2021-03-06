# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Equipment, Actions, CharacterClasses, InputHandler, Conditions

class Character(object):
  def __init__(self, name, combat):
    self.name = name
    self.conscious = True
    self.combat = combat
    self.panel = self.combat.panel
    self.character_class = CharacterClasses.Fighter()
    self.situations = {}
    self.sont_situations = {}
    self.conditions = {}
    self.situational_attack_modifiers = 0
    self.situational_defense_modifiers = 0
    self.situational_damage_modifiers = 0
    self.level = 1
    self.size = 'medium'
    self.hp = 0
    self.exp = 0
    self.speed = 6
    self.ini_bonus = 0
    self.attributes = {'str': Attribute('Strength', self), 'con':
Attribute('Constitution', self), 'dex':Attribute('Dexterity', self),
'int':Attribute('Intelligence', self), 'wis':Attribute('Wisdom', self),
'cha':Attribute('Charisma', self)}
    self.defenses = {'AC': Defence('Armor Class',self), 'fort':
Defence('Fortitude',self), 'refl': Defence('Reflex',self), 'will':
Defence('Will',self)}
    self.equip_weapon(Equipment.Weapon('Unarmed'))
    self.equip_armor(Equipment.Armor('No Armor'))
    self.actions = [Actions.Run(self), Actions.Walk(self), Actions.Shift(self)]
    self.actions.append(Actions.Action('End Turn', self, 'Free Action'))

  def __str__(self):
    return self.name

  def equip_weapon(self, weapon):
    self.equ_weap = weapon
    
  def equip_armor(self, armor):
    self.equ_armor = armor
    
  def add_condition(self, condition):
    self.conditions[condition.name] = condition
    self.panel.send_message(self.name + ' under condition: ' + condition.name)
    
  def remove_condition(self, condition):
    del self.conditions[condition.name]
    self.panel.send_message('Condition ' + condition.name + ' ended.')
    
  def remove_sont_situations(self):
    situations_to_remove = []
    for situation in self.sont_situations.itervalues():
      situations_to_remove.append(situation)
    for situation in situations_to_remove:
      situation.remove_situation()
    
  def saving_throws(self):
    conditions_to_save = []
    for condition in self.conditions.itervalues():
      conditions_to_save.append(condition)
    for condition in conditions_to_save:
      if random.randint(1,20) >= 10:
	self.remove_condition(condition)
      else:
	self.panel.send_message('Condition ' + condition.name + ' continues.')
  
  def reduce_hp(self, damage):
    msg = [self.name + ' takes ' + str(damage) + ' damage.']
    self.hp -= damage
    if self.hp <= 0:
      msg.append(self.name + ' died.')
      self.combat.del_combatant(self)
      self.conscious = False
    self.panel.send_message(msg)
    
  def is_missed(self):
    pass

  def generate_attributes(self):
    for attr in self.attributes.itervalues():
      attr.setvalue(random.randint(8,18))
      
  def calculate_stats(self):
    atts = self.attributes
    self.hp = atts['con'].value + self.character_class.start_hp + self.level * self.character_class.hp_per_level
    self.defenses['AC'].setvalue(10 + self.equ_armor.armorbonus)
    fortvalue = 10 + max([atts['str'].get_modifier(), atts['con'].get_modifier()])
    self.defenses['fort'].setvalue(fortvalue)
    reflvalue = 10 + max([atts['dex'].get_modifier(), atts['int'].get_modifier()])
    self.defenses['refl'].setvalue(reflvalue) 
    willvalue = 10 + max([atts['wis'].get_modifier(), atts['cha'].get_modifier()])
    self.defenses['will'].setvalue(willvalue)
    self.ini_bonus = atts['dex'].get_modifier()
    
  def get_stat_list(self):
    description_list = []
    description_list.append('Statistics for' +' ' + self.name)
    description_list.append('#####')
    description_list.append('HP' + str(self.hp))
    description_list.append('')
    description_list.append('ATTRIBUTES')
    for attribute in self.attributes.itervalues():
      description_list.append(attribute.name + ' ' + str(attribute.value))
    description_list.append('')
    description_list.append('DEFENCES')
    for defence in self.defenses.itervalues():
      description_list.append(defence.name + ' ' + str(defence.value))
    return description_list

  def show_stats(self):
    print 'STATS FOR', self.name
    print '#####'
    print 'HP', self.hp
    print 'Attributes'
    for attribute in self.attributes.itervalues():
      print attribute.name, attribute.value
    print 'Defences'
    for defence in self.defenses.itervalues():
      print defence.name, defence.value
    print '#####'
  
  def print_equipped_items(self):
    print 'EQUIPPED ITEMS:'
    print '#####'
    print self.equ_armor.name
    print self.equ_weap.name
    print '#####'
      
  def print_actions(self):
    print 'Possible Actions for', self.name, ':'
    print '#####'
    for action_nr in range(len(self.actions)):
      print str(action_nr), self.actions[action_nr], '(', self.actions[action_nr].action_type, ')'
    print self.action_count
    print '#####'
    
  def process_combatant(self):
    end_of_turn = False
    self.remove_sont_situations()
    self.action_count = {'Standard Action': 1, 'Move Action' : 1, 'Free Action' : 5}
    if self.conscious:
      while not end_of_turn:
	choice = self.combat.input_handler.graphic_list_choice
	action_choice_item = choice(self.actions, self.name + ' chooses which Action?', str(self.action_count)) 
	#action_choice = self.actions.index(action_choice_item)
	if action_choice_item.name == 'End Turn' or action_choice_item.name == 'Cancel':
	  end_of_turn = True
	else:
	  action_choice = self.actions.index(action_choice_item)
	  this_action = self.actions[int(action_choice)]
	  if self.action_count[this_action.action_type] >= 1:
	    this_action.process()
	    self.action_count[this_action.action_type] -= 1
	  elif this_action.action_type == 'Move Action' and self.action_count['Standard Action'] >= 1:
	      self.panel.send_message('Trading Standard Action for Move Action')
	      this_action.process()
	      self.action_count['Standard Action'] -= 1
	  else:
	      self.panel.send_message('No ' + this_action.action_type + ' left.')
    self.saving_throws()
    self.panel.send_message(self.name + ' finishes turn.')
       
class Value:
  def __init__(self, value):
    self.value = 0
  def setvalue(self, value):
    self.value = value
  def getvalue(self):
    return self.value
    
class Attribute(Value):
  def __init__(self, name, combatant, value=10):
    Value.__init__(self, value)
    self.name = name
    self.combatant = combatant
    self.value = value
  def check_att(self):
    if self.value < 1:
      self.value = 1
  def get_modifier(self):
    return (self.value - 10) / 2

class Defence(Value):
  def __init__(self, name, combatant, value = 10):
    self.name = name
    self.combatant = combatant
    self.value = 10 + self.combatant.level / 2