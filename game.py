import pygame,sys,os
from functions import *
from constants import * 
from rank import Rank 
from suit import Suit 
from card import Card
from pokerhand import PokerHand
from cardsprite import CardSprite
from pokerhandsprite import PokerHandSprite
class Game():

  def __init__(self,screenSize = DEFAULT_SCREEN_SIZE): 
    #initialize screen variables
    self.screenSize = screenSize 

    #initialize timer-related variables
    self.current_time = 0 
    self.previous_time = 0
    self.clock = pygame.time.Clock()

    #initialize game
    self.initialize()
  
  def input(self,events):
    for event in events: 
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN: 
        pass
      elif event.type == pygame.KEYUP:
        pass
      elif event.type == pygame.MOUSEBUTTONDOWN: 
        mousePos = pygame.mouse.get_pos()
        self.phand.toggleSelection(mousePos)

      elif event.type == pygame.MOUSEBUTTONUP:
        pass

  
  def initialize(self):

    pygame.init()
    self.screen = pygame.display.set_mode(self.screenSize)
    pygame.display.set_caption("Serious Poker")

    self.area = self.screen.get_rect()
    self.center = self.area.center
    self.bottomleft = self.area.bottomleft
    self.bottomright = self.area.bottomright
    self.topleft = self.area.topleft
    self.topright = self.area.topright

    self.phand = PokerHandSprite([
      Card(Rank.Two, Suit.Hearts),
      Card(Rank.Three, Suit.Hearts),
      Card(Rank.Four, Suit.Hearts),
      Card(Rank.Five, Suit.Hearts),
      Card(Rank.Six, Suit.Hearts)
    ])

  def update(self,elapsedTime):
    pass

  def run(self):
    print("Starting to run game...")

    while True:
      self.input(pygame.event.get())

      ticks = pygame.time.get_ticks()
      self.current_time = ticks 
      elapsed = self.current_time - self.previous_time 

      self.update(elapsed)

      self.screen.fill(POKER_GREEN)


      self.phand.draw(self.screen)
      
      pygame.display.flip()
      self.clock.tick(60)

     
      self.previous_time = self.current_time
    
    pygame.quit()

