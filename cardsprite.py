import pygame  
from card import Card
from functions import * 
from constants import * 

class CardSprite(pygame.sprite.Sprite):

  def __init__(self,card):
    super().__init__()
    self.card = card
    self.frontImage = load_image(card.getImagePath())
    self.frontImage = pygame.transform.scale(self.frontImage,DEFAULT_CARD_SIZE)
    self.currentImage = self.frontImage
    self.rect = self.currentImage.get_rect()

    self.loadBackImage()
    self.rect = self.currentImage.get_rect()
    self.isFlipped = False

  def setPosition(self,x,y):
    self.rect.topleft = x,y

  def setX(self,x):
    self.rect.x = x

  def getX(self,x):
    return self.rect.x

  def setY(self, x):
    self.rect.y = x

  def getY(self):
    return self.rect.y

  def loadBackImage(self):
    self.backImage = load_image(self.card.getBackImagePath())
    self.backImage = pygame.transform.scale(self.backImage,DEFAULT_CARD_SIZE) 
   



  def draw(self,screen,pos = None):
    originalRect = self.rect
    if not self.isFlipped:
      self.currentImage = self.frontImage
    else:
      self.currentImage = self.backImage

    self.rect = self.currentImage.get_rect()
    self.rect = originalRect

    if pos:
      screen.blit(self.currentImage,pos)
    else:
      screen.blit(self.currentImage,self.rect.topleft)
