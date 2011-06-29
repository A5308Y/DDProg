# -*- coding: utf-8 -*-

import pygame

class StatusPanel(object):
  def __init__(self, combat, SCREEN_SIZE, screen):
    self.screen_font = pygame.font.SysFont("umpush", 16)
    self.combat = combat
    self.screen = screen
    self.displayed_entities = []
    self.SCREEN_SIZE = SCREEN_SIZE
    self.messages = []
    self.message_row = 0
    self.caption = 'COMBAT'
    self.combatant_list = []
    self.height = 600
    self.menu_width = 50
    self.menu_start = self.SCREEN_SIZE[0]-self.menu_width
    self.displayed_entity_number = 0
    self.message_area = (SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/3, self.menu_start, SCREEN_SIZE[1])
    self.upper_info_area = (0, 0, 300, 400)
    self.lower_info_area = (0, 400, SCREEN_SIZE[0]/4, SCREEN_SIZE[1])
    self.caption_area = (SCREEN_SIZE[0]/3, 0, self.menu_start, 80)
    self.menu_area = (self.menu_start, 0, SCREEN_SIZE[0], 500)
    self.dialog_area = (SCREEN_SIZE[0]/3, 80, self.menu_start, 300)

  def blitrendertext(self, text, row, screen):
    statustext = self.screen_font.render(text, True, (0,0,0))
    screen.blit(statustext, (10, 20*row, 15, 15))

  def define_displayed_entities(self):
      self.displayed_entities = []
      for entity in self.combat.combatants.itervalues():
	  self.displayed_entities.append(entity)
	  
  def show_all_entities(self, screen):
      self.screen.set_clip(self.upper_info_area)
      for entity in self.displayed_entities:
	if self.displayed_entities.index(entity) == self.displayed_entity_number:
	  description_list = entity.get_stat_list()
	  for entry in description_list:
	    self.blitrendertext(entry, description_list.index(entry), screen)  
      self.screen.set_clip(None)

  def draw_menu(self, screen):
    menu_start = self.menu_start
    pygame.draw.rect(screen, (180, 200, 210), pygame.Rect((menu_start,0),self.SCREEN_SIZE))
    screen.blit(self.screen_font.render("Quit", True, (0,0,0)), (menu_start, 0, 15, 15))
    screen.blit(self.screen_font.render("Text2", True, (0,0,0)), (menu_start, 20, 15, 15))
    screen.blit(self.screen_font.render("Text3", True, (0,0,0)), (menu_start, 40, 15, 15))
    screen.blit(self.screen_font.render("Text4", True, (0,0,0)), (menu_start, 60, 15, 15))
    screen.blit(self.screen_font.render("Text5", True, (0,0,0)), (menu_start, 80, 15, 15))
    screen.blit(self.screen_font.render("<", True, (0,0,0)), (menu_start, 100, 15, 15))
    screen.blit(self.screen_font.render(">", True, (0,0,0)), (menu_start + 20, 100, 15, 15))

  def draw_choice(self, choice_list, caption, extra_info = ''):
    screen = self.screen
    menu_start = self.menu_start
    self.draw_panel()
    self.draw_list(choice_list, caption, self.dialog_area, extra_info)
    pygame.display.update()
  
  def send_message(self, message):
    if type(message) is list:
      count = 1
      for entry in message:
	self.messages.append((entry, self.message_row + len(message) - count))
	count += 1
      self.message_row += len(message)
    else:
      self.messages.append((message, self.message_row))
      self.message_row += 1

  def draw_messages(self):
    self.screen.set_clip(self.message_area)
    for message in self.messages:
      y_value = 20*(len(self.messages) - message[1])
      blit_area = (self.message_area[0], self.message_area[1] + y_value, 15, 15)
      self.screen.blit(self.screen_font.render(message[0], True, (0,0,0)), blit_area)
    self.screen.set_clip(None)
    
  def draw_list(self, itemlist, caption, area, extra_info=''):
    self.screen.set_clip(area)
    blit_area = (area[0], area[1], 15, 15)
    self.screen.blit(self.screen_font.render(caption, True, (0,0,0)), blit_area)
    blit_area = (area[0], area[1] + 20, 15, 15)
    self.screen.blit(self.screen_font.render(extra_info, True, (0,0,0)), blit_area)
    for item in itemlist:
      y_value = 20*(itemlist.index(item) + 2)
      blit_area = (area[0], area[1] + y_value, 15, 15)
      self.screen.blit(self.screen_font.render(item.name, True, (0,0,0)), blit_area)
    self.screen.set_clip(None)
    
  def show_combatants(self):
    self.combatant_list = []
    for combatant in self.combat.combatants.itervalues():
      self.combatant_list.append(combatant)
    self.draw_list(self.combatant_list, 'Combatants', self.lower_info_area)
    
  def draw_info(self):
    self.show_combatants()
    self.define_displayed_entities()
    self.screen.set_clip(self.upper_info_area)
    self.show_all_entities(self.screen)
    self.screen.set_clip(None)
    
  def send_caption(self, caption):
    self.caption = caption
    
  def draw_caption(self, caption):
    self.screen.set_clip(self.caption_area)
    blit_area = (self.caption_area[0], self.caption_area[1], 15, 15)
    self.screen.blit(self.screen_font.render(caption, True, (0,0,0)), blit_area)
    self.screen.set_clip(None)

  def draw_panel(self, *screen):
    screen = self.screen
    rectangle = pygame.Rect((0,0),self.SCREEN_SIZE)
    pygame.draw.rect(screen, (180, 210, 210), rectangle)
    self.draw_caption(self.caption)
    self.draw_info()
    self.draw_menu(screen)
    self.draw_messages()
    pygame.display.update()