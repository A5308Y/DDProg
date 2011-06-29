# -*- coding: utf-8 -*-
#!/usr/bin/python

class Situation(object):
  def __init__(self, combatant):
      self.name = 'situation'
      self.combatant = combatant
  
  def add_situation(self):
      if not self.combatant.situations.has_key(self.name):
        self.combatant.sont_situations[self.name] = self
        self.add_effects()
  
  def remove_situation(self):
      del self.combatant.situations[self.name]
      self.remove_effects()
      
  def add_effects():
      pass
  def remove_effects():
      pass
     

class Marked(Situation):
  def __init__(self, combatant):
      Situation.__init__(self, combatant)
      self.name = 'marked'
    
  def add_effects(self):
      self.combatant.situational_attack_modifier -= 2
      
  def remove_effects(self):
      self.combatant.situational_attack_modifier += 2
      

class SontSituation(object):
  def __init__(self, combatant):
      self.name = 'situation'
      self.combatant = combatant
      self.panel = self.combatant.panel
  
  def add_situation(self):
    if not self.combatant.sont_situations.has_key(self.name):
      self.combatant.sont_situations[self.name] = self
      self.add_effects()
  
  def remove_situation(self):
      del self.combatant.sont_situations[self.name]
      self.remove_effects()
  
  def add_effects():
      pass
  def remove_effects():
      pass
  
class Grant_Combat_Advantage(SontSituation):
  def __init__(self, combatant):
      SontSituation.__init__(self, combatant)
      self.name = 'combat advantage'
  
  def add_effects(self):
      self.combatant.situational_defense_modifiers -= 2
      self.panel.send_message(self.combatant.name + ' is now granting combat advantage.')
    
  def remove_effects(self):
      self.combatant.situational_defense_modifiers += 2
      self.panel.send_message(self.combatant.name+ ' is no longer granting combat advantage.')

class Running(SontSituation):
  def __init__(self, combatant):
      SontSituation.__init__(self, combatant)
      self.name = 'running'

  def add_effects(self):  
      Grant_Combat_Advantage(self.combatant).add_situation()
      self.combatant.situational_attack_modifiers -= 5
      self.panel.send_message( self.combatant.name + ' is now running.')

  def remove_effects(self):
      self.combatant.situational_attack_modifiers += 5
      self.panel.send_message(self.combatant.name + ' is no longer running.')