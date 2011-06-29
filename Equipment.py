# -*- coding: utf-8 -*-
#!/usr/bin/python

class Item(object):
  def __init__(self, name, price=0, weight=0):
    self.name = name
    
    
    
class Weapon(object):
  def __init__(self, name, dmg_dicerange=3, dmg_dicecount=1, prof_bonus=2, weapon_group='None', properties='-'):
    self.name = name
    self.dmg_dicerange = dmg_dicerange
    self.dmg_dicecount = dmg_dicecount
    self.weapon_group = weapon_group
    self.properties = properties


class Dagger(Weapon):
  def __init__(self):
    #Item.__init__(self, "Dagger", 1, 1)
    Weapon.__init__(self, "Dagger", 4, 1, 3)

class Longsword(Weapon):
  def __init__(self):
    Weapon.__init__(self, "Longsword", 8, 1, 3)
    
    
    
    
    
class Armor(Item):
  def __init__(self, name='None', armorbonus=0, armor_type = 'None'):
    #Item.init
    self.name = name
    self.armorbonus = armorbonus
    self.armor_type = armor_type
    
    
    
class LeatherArmor(Armor):
  def __init__(self):
    Armor.__init__(self, 'Leather armor', 2, 'Light')
    self.price = 25
    self.weight = 15