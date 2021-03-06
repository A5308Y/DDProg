# -*- coding: utf-8 -*-
#!/usr/bin/python

import random, InputHandler, SontSituations, Conditions

class Effect(object):
  def __init__(self, cause, target):
    self.cause = cause

class DealDamage(Effect):
  def __init__(self, cause, target, damage):
    Effect.__init__(self, cause, target)
    
  def process(self):
    for i in range(self.dmg_dicecount):
      damage = random.randint(1,self.dmg_dicerange)
      damage += self.combatant.situational_damage_modifiers
      if self.combatant.conditions.has_key('weakened') != 0:
	damage = damage / 2
	self.panel.send_message('weakened attack.')
      if damage <= 1:
	damage = 1
      actual_target.reduce_hp(damage)