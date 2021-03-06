# -*- coding: utf-8 -*-

import pygame, random,  Panel, InputHandler, Combat, PlayerCharacters, Monster
from pygame.locals import *

SCREEN_SIZE = (1024, 720)

def run():
  pygame.init()
  screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
  pygame.display.set_caption('D&D4: Kampfsimulator')
  combat = Combat.Combat(SCREEN_SIZE, screen)
  clock = pygame.time.Clock()
    
  #Testing_Section
  combat.add_combatant(PlayerCharacters.Kurt(combat))
  for i in range(3):
    combat.add_combatant(Monster.GoblinBlackblade(combat))
  
  combat.process()
  



if __name__ == "__main__":
  run()