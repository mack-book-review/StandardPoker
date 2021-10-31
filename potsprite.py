import pygame
from pot import Pot 


class PotSprite(pygame.sprite.Sprite):

  def __init__(self,pot):
    self.pot = pot
  

  def draw(self,screen):