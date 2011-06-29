# -*- coding: utf-8 -*-
#!/usr/bin/python

import Actions, Characters

Kandorn = Characters.Character('Kandorn')

def process_combatant(self):
  self.remove_sont_situations()
  if self.conscious:
    self.print_actions()
    action_choice = InputHandler.number_choice('Which Action? ', self.actions)
    this_action = self.actions[int(action_choice)]
    this_action.process()
    raw_input('')
  self.saving_throws()