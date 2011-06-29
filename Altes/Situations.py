# -*- coding: utf-8 -*-
#!/usr/bin/python

class Situation(object):
  def __init__(self, combatant):
    self.name = 'situation'
    self.combatant = combatant
  
  def add_situation(self):
    pass
  
  def remove_situation(self):
    pass
  
class Running(Situation):
  def __init__(self, combatant):
    Situation.__init__(self, combatant)
    self.name = 'running'

  def add_situation(self):
    self.combatant.situations[self.name] = self
    self.combatant.situations['grant combat advantage from running'] = self
    self.combatant.situational_attack_modifiers -= 5
    
  def remove_situation(self):
    del self.combatant.situations[self.name]
    del self.combatant.situations['grant combat advantage from running']
    self.combatant.situational_attack_modifiers += 5