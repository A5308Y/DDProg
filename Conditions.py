# -*- coding: utf-8 -*-
#!/usr/bin/python

class Condition(object):
  def __init__(self, combatant):
    self.combatant = combatant
    self.name = 'condition'
  
class Weakened(Condition):
  def __init__(self, combatant):
    Condition.__init__(self,combatant)
    self.name = 'weakened'
    self.description = 'Your attacks deal half damage.'