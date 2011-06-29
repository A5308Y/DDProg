# -*- coding: utf-8 -*-
#!/usr/bin/python

class Character_Class(object):
  def __init__(self, name):
    self.name = name
    self.start_hp = 0
    self.hp_per_level = 0

class Fighter(Character_Class):
  def __init__(self):
    self.start_hp = 15
    self.hp_per_level = 6