# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, Equipment, Actions, Conditions, Characters

class GoblinBlackblade(Characters.Character):
  def __init__(self, combat):
    Characters.Character.__init__(self, 'Goblin Blackblade', combat)
    Attribute = Characters.Attribute
    Defence = Characters.Defence
    self.size = 'small'
    self.hp = 25
    self.ini_bonus = 7
    self.attributes = {'str': Attribute('Strength', self, 14), 'con':
Attribute('Constitution', self, 13), 'dex':Attribute('Dexterity', self, 17),
'int':Attribute('Intelligence', self, 8), 'wis':Attribute('Wisdom', self, 12),
'cha':Attribute('Charisma', self, 8)}
    self.defenses = {'AC': Defence('Armor Class',self, 16), 'fort':
Defence('Fortitude',self, 12), 'refl': Defence('Reflex',self, 14), 'will':
Defence('Will',self, 11)}
    self.actions.append(GoblinShortSwordAttack(self))
    
  def is_missed(self):
    self.panel.send_message(self.name + ' may shift 1 square')

class GoblinShortSwordAttack(Actions.AttackPower):
  def __init__(self, combatant):
    Actions.AttackPower.__init__(self, 'Short Sword (Basic Melee Attack)', combatant, 'Standard Action', 'melee',
0, 'one creature', 'str', 'AC', '1D + str')
    self.attack_modifier = 5
    self.dmg_dicerange = 6
    self.dmg_dicecount = 1
    
  def hit(self, actual_target):
    Actions.DealDamage(self,actual_target,self.weapon_damage()).process()
    if actual_target.sont_situations.has_key('combat advantage'):
      self.panel.send_message(self.combatant.name + ' deals extra damage against targets it has combat advantage against.')
      Actions.DealDamage(self,actual_target,random.randint(1,6)).process()
    #self.harm(actual_target)
    #actual_target.add_condition(Conditions.Weakened(actual_target))