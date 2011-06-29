# -*- coding: utf-8 -*-
#!/usr/bin/python

import Equipment, Actions, Characters, CharacterClasses

Attribute = Characters.Attribute
Defence = Characters.Defence

class Kurt(Characters.Character):
  def __init__(self, combat):
    Characters.Character.__init__(self, 'Kurt', combat)
    self.character_class = CharacterClasses.Fighter()
    self.level = 2
    
    self.attributes = {'str': Attribute('Strength', self, 17), 'con':
Attribute('Constitution', self, 16), 'dex':Attribute('Dexterity', self, 13),
'int':Attribute('Intelligence', self, 10), 'wis':Attribute('Wisdom', self, 10),
'cha':Attribute('Charisma', self, 8)}

    self.defenses = {'AC': Defence('Armor Class',self), 'fort':
Defence('Fortitude',self), 'refl': Defence('Reflex',self), 'will':
Defence('Will',self)}

    self.equip_weapon(Equipment.Longsword())
    self.equip_armor(Equipment.LeatherArmor())
    self.actions.append(Actions.Basic_Melee(self))
    self.actions.append(Actions.Cleave(self))
    self.actions.append(Actions.SureStrike(self))
    self.calculate_stats()