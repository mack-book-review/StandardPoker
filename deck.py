from suit import Suit 
from rank import Rank
from card import Card 
from constants import * 
import random 

class Deck(object):

  def __init__(self):
    self.deck = []

    for suit in (Suit):
      for rank in (Rank):
        self.deck.append(Card(rank,suit))
    
    random.shuffle(self.deck)

  

  def shuffle(self):
    random.shuffle(self.deck) 

  def deal(self):
    index = random.randint(0,len(self))
    return self.deck.pop(index)

  def size(self):
    return len(self)
  
  def isEmpty(self):
    return len(self) == 0

  def __len__(self):
    return len(self.deck)
  
  def __str__(self):
    user_str = f"Size of deck: {str(len(self))}\n"
    user_str += "Cards in Deck: \n"
    for card in self.deck:
      user_str += "\t" + str(card) + "\n"
    return user_str
