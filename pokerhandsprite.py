import pygame  
from card import Card
from cardsprite import CardSprite
from pokerhand import PokerHand
from functions import *
from constants import * 

class PokerHandSprite(pygame.sprite.Sprite):

  def __init__(self,cards):
    super().__init__()
    self.pokerHand = PokerHand(cards)
    self.rects = []
    self.selections = [False for _ in range(len(self.pokerHand))]

  def removeSelectedCards(self):
    toRemoveCards = [self.pokerHand[i] for i in range(len(self.pokerHand)) if self.selections[i]]
    for i in range(len(toRemoveCards)):
      self.removeCard(toRemoveCards[i])
      self.selections.pop(i)


  def addCards(self,cards):
    self.pokerHand.addCards(cards)

  def addCard(self,card):
    self.pokerHand.addCard(card)

  def removeCards(self,cards):
    self.pokerHand.removeCards(cards)

  def removeCard(self,card):
    if card in self.pokerHand:
      self.pokerHand.removeCard(card)

  def toggleSelection(self,mousePos):
    index = self.getIndexAtMouseClick(mousePos)
    print("Toggled Index: ",str(index))
    if index != None and index >= 0:
      print("Index has been toggled")
      self.selections[index] = not self.selections[index]



  def getIndexAtMouseClick(self,mousePos):
    for i in range(len(self.rects)):
      if self.rects[i].collidepoint(mousePos):
        return i
    return None

  def draw(self,screen):
    startX,startY = DEALER_HAND_START_POS
  
    for i in range(len(self.pokerHand)):
      x = startX + i*DEFAULT_CARD_SIZE[0]*1.2
      card = self.pokerHand[i]
      cardSprite = CardSprite(card)
      if self.selections[i]:
        cardSprite.isFlipped = True
      cardSprite.setPosition(x,startY)
      self.rects.append(cardSprite.rect)
      cardSprite.draw(screen)