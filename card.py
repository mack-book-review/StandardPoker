from rank import Rank 
from suit import Suit 
from cardcolor import CardColor 

class Card(object):

  def __init__(self,rank,suit,cardcolor = CardColor.green1):
    self.cardcolor = cardcolor
    self.rank = rank
    self.suit = suit

  
  def getImagePath(self):
    return f"card{self.suit.name}{self.rank}.png"
  
  def getBackImagePath(self):
    return f"cardBack_{self.cardcolor.name}.png"
      
  
  def __gt__(self,other):
    if self.suit == other.suit: 
      return self.rank > other.rank
    else:
      raise RuntimeError(f"Invalid comparison: the cards {self} and {other} do not have the same suit and cannot be compared using the __gt__ operator")
    
  def __lt__(self,other):
    if self.suit == other.suit: 
      return self.rank < other.rank
    else:
      raise RuntimeError(f"Invalid comparison: the cards {self} and {other} do not have the same suit and cannot be compared using the __lt__ operator") 

  def __ne__(self,other):
    return not(self == other)
    
  def __eq__(self,other):
    hasEqualSuits = other.suit == self.suit 
    hasEqualRanks = other.rank == self.rank 
    return hasEqualSuits and hasEqualRanks 

  def __ge__(self,other): 
    return self == other or self > other
    
  def __le__(self,other):
    return self == other or self < other 

  def __str__(self):
    cardcolor = self.cardcolor.name.capitalize()
    return f"{cardcolor} Card:{self.rank.name} of {self.suit.name}"