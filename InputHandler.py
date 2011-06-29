# -*- coding: utf-8 -*-
#!/usr/bin/python

# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

class InputChecker():
  def __init__(self, panel):
    self.last_pressed_cooldown = 0
    self.panel = panel
 
  def check_input(self, mouse_x, mouse_y):
        panel = self.panel
    #if pygame.mouse.get_pressed()[0]:
        #print 'get_pressed'
	#mouse_x = pygame.mouse.get_pos()[0]
	#mouse_y = pygame.mouse.get_pos()[1]
	if mouse_x >= self.panel.menu_start:
	  if mouse_y <= 20:
	    exit_game()
	  #elif mouse_y <= 40:
	    #panel.displayed_type = "animal"
	    #panel.displayed_entity_number = 0
	  #elif mouse_y <= 60:
	    #panel.displayed_type = "site"
	    #panel.displayed_entity_number = 0
	  #elif mouse_y <= 80:
	    #panel.displayed_type = "human"
	    #panel.displayed_entity_number = 0
	  elif mouse_y <= 120:
	    if mouse_x <= panel.menu_start + 15:
	      panel.displayed_entity_number -= 1 
	      panel.displayed_entity_number = panel.displayed_entity_number % len(panel.displayed_entities)
	    else:
	      panel.displayed_entity_number += 1 % len(panel.displayed_entities)
	      panel.displayed_entity_number = panel.displayed_entity_number % len(panel.displayed_entities)	      
	elif mouse_x <= panel.lower_info_area[3] and mouse_y >= panel.lower_info_area[1]:
	  panel.displayed_entity_number = (mouse_y - panel.lower_info_area[1] -40) / 20
	   

  def graphic_list_choice(self, choice_list, caption, extra_info = ''):
    choice = None
    choice_list.append(Cancel())
    self.panel.draw_choice(choice_list, caption, extra_info)
    while choice == None:
      for event in pygame.event.get():
	if event.type == MOUSEBUTTONDOWN:
	  mouse_x = pygame.mouse.get_pos()[0]
	  mouse_y = pygame.mouse.get_pos()[1]
	  for item in choice_list:
	    y_value = 100 + 20*(choice_list.index(item) +1)
	    if 150 <= mouse_x <= self.panel.menu_start:
	      if y_value  <= mouse_y <= y_value + 20:
		choice_list.pop()
		return item 
		#choice = item
		#break
	  self.check_input(mouse_x, mouse_y)
	  self.panel.draw_choice(choice_list, caption, extra_info)
    #return choice
    
class Cancel(object):
  def __init__(self):
    self.name = 'Cancel'

def exit_game():
  sys.exit()