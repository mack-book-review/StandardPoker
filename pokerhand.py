from suit import Suit 
from rank import Rank 
from card import Card

class PokerHand(object):
  DEFAULT_SIZE = 5

  def __init__(self,cards = []):

    self.hand = cards

    #Error need to fix
    # self._rankCounts = {}
    # for rank in (Rank):
    #   self._rankCounts[rank] = 0
    
    # self._handInfo = {}

  
  #ADD CARD OPERATIONS
  def addCards(self,cards):
    for card in self:
      self.addCard(card)

  def addCard(self,card):
    if len(self) >= PokerHand.DEFAULT_SIZE:
      print("Cannot add additional cards to hand; card limit reached")
    self.hand.append(card)

  #REMOVE CARD OPERATIONS
  def removeCards(self,cards):
    for card in self: 
        self.removeCard(card)
      
  def removeCard(self,card):
    if len(self) <= 0:
        print("No cards remaining; cannot complete remove operation")
    else:
      self.hand.remove(card)
   
  
  def hasFullHouse(self):
    return self.hasThreeOfKind() and self.hasOnePair()
  
  def hasTwoPairs(self):
    return len(list(filter(lambda rank,count: count == 2,self._handInfo.items()))) == 2
  
  def hasOnePair(self):
    return len(list(filter(lambda rank,count: count == 2,self._handInfo.items()))) == 1

  def hasThreeOfKind(self):
    return len(list(filter(lambda rank,count: count >= 3,self._handInfo.items()))) == 3
  
  def hasFourOfKind(self):
    return len(list(filter(lambda rank,count: count >= 4,self._handInfo.items()))) == 4

  def _updateRankCounts(self):
    for card in self:
      self._rankCounts[card.rank] += 1

  def _analyzeHand(self):
    for rank,count in self._rankCounts():
        if count == 4:
          self._handInfo[rank] = count
        if count == 3:
          self._handInfo[rank] = count
        if count == 2:
          self._handInfo[rank] = count
    
  def hasStraightFlush(self):
    return self.hasStraight() and self.hasFlush()
  
  def hasStraight(self): 
    ranks = list(map(lambda card: card.rank,self.hand)) 
    ranks.sort()
    return self._hasSequence(ranks)
  
  def _hasSequence(self,hand):
    for i in range(len(self)):
      if self[i] > self[i+1]:
        return False 
    return True

  def hasFlush(self):
    return self.numberClubs() == 5 or self.numberDiamonds() == 5 or self.numberHearts() == 5 or self.numberSpades() == 5

  

  def numberHearts(self):
    return len(list(filter(lambda card: card.suit == Suit.Hearts,self.hand))) 
  
  def numberSpades(self):
    return len(list(filter(lambda card: card.suit == Suit.Spades,self.hand)))

  def numberClubs(self):
    return len(list(filter(lambda card: card.suit == Suit.Clubs,self.hand))) 
  
  def numberDiamonds(self):
    return len(list(filter(lambda card: card.suit == Suit.Diamonds,self.hand))) 

  def sortAdd(self):
    pass

  def longestConsecutiveSequence(self):
    pass


  #iterate one time over the hand, counting the number of different suits and number of cards for each rank
  #returns a numerical index summarizing the quality of the poker hand
  # def analyzeHand(self):
  #   sorted_hand = []
  #   ranks = []
  #   num_diamonds,num_clubs,num_spades,num_hearts = 0,0,0,0
  #   suits_counts = []
  #   for i in range(len(self.hand)):
  #       if self.hand[i].suit == Suit.Spades:
  #         num_spades += 1
  #       elif self.hand[i] == Suit.Clubs:
  #         num_clubs += 1
  #       elif self.hand[i] == Suit.Hearts:
  #         num_hearts += 1
  #       elif self.hand[i] == Suit.Diamonds:
  #         num_diamonds += 1
  #
  #       suits_counts = [num_diamonds,num_hearts,num_spades,num_clubs]
  #       ranks.append(self.hand[i].rank)
  #       self.sortAdd(sorted_hand,self.hand[i])
  #       sorted_ranks = [card.rank for card in sorted_hand]
  #       #iterate through sorted_ranks from i = 0 to i = len(sorted_ranks)
  #         #increment count
  #         #has_one_pair to False, has_three_of_kind to False, has_four_of_kind to False, has_two_pairs to False
  #         when i == 0, set count to 1
  #
  #         if i == 1 and count == 2:
  #           #has_one_pair is True
  #
  #         if i == 2 and count == 3:
  #           #has_one_pair is False, has_three_of_kind is True
  #         elif i == 2 and count == 1:
  #           #if count resets to 1, and has_one_pair is still True, so no need to change it
  #
  #         if i == 3 and count == 4:
  #           #has_four_of_kind is true, has_three_of_kind reset to False
  #         elif i == 3 and count == 3:
  #           #has_three_of_kind is set to True
  #         elif i == 3 and count == 2:
  #           #if has_one_pair is already True, then has_two_pair is true
  #           #otherwise, has_one_pair is now set to true
  #
  #         if i == 4 and count == 5:
  #           #has_straight is True, has_four_of_kind is reset to False
  #         elif i == 4 and count == 4:
  #           #has_four_of_kind is true, has_three_of_kind rest to False
  #         elif i ==4 and count == 3:
  #           #if has one pair True, then has_full_house_true
  #           #if has_one_pair is False, the three_of_kind is set to true
  #         elif i == 4 and count == 2:
  #           #pass
  #
  #
  #
  #
  #
  #       longest_consecutive_sequence = self.longestConsecutiveSequence(sorted_hand)
  #
  #       rank_set = set(self.ranks)
  #       '''
  #       Use set analysis
  #       if len(set of ranks) is 4, there could be 1 pair and 3 unique cards
  #       if  len(set of ranks) is 3, then are 2 pairs or (3 of a kind plus 2 unique cards)
  #       if  len(set of ranks) is 2, then there could be 3 of a kind + pair, 4 of a kind + 1 unique card,
  #       '''
  #       hand_rank = 0
  #
  #       if 5 in suits_counts and longest_consecutive_sequence:
  #         return "Straight Flush"
  #       elif has four of kind
  #         return "Four of Kind"
  #       elif self.hasFullHouse() and other.hasFullHouse():
  #         return "Full house"
  #       elif self.hasFlush
  #         return "Flush"
  #       elif self.hasStraight():
  #         return "Straight"
  #       elif self.hasThreeOfKind():
  #         return  "Three of Kind"
  #       elif self.hasTwoPairs():
  #         return "Two Pairs"
  #         add fractional values for the kind of two pairs
  #       elif self.hasOnePair():
  #         return "One pair"
  #         add fractional value for the rank of the pair
  #       else:
  #         return False
  #
  #       return hand_rank


  def __contains__(self, item):
    return item in self.hand

  def __len__(self):
    return len(self.hand)
  
  def __getitem__(self,key):
    return self.hand[key]
  
  def __setitem__(self,key,value):
    self.hand[key] = value
  
  def __iter__(self):
    return self.hand.__iter__()

  def __ne__(self,other): 
    pass

  def __eq__(self,other): 
    #cards are equal if they have no pairs and no sequences
    pass
  
  def __lt__(self,other):
    pass

  def __ge__(self,other):
    pass 
  
  def __le__(self,other):
    pass
  
  #version 1
  def __gt__(self,other):
    if self.isStraightFlush() and other.isStraightFlush():
      pass #compare sequences 
    elif self.isStraightFlush() and not other.isStraightFlush():
      return True
    elif self.hasFourOfKind() and other.hasFourOfKind():
      pass #compare sequences 
    elif self.hasFourOfKind() and not other.hasFourOfKind(): 
      return True 
    elif self.hasFullHouse() and other.hasFullHouse(): 
      pass #compare ranks 
    elif self.hasFullHouse() and not other.hasFullHouse():
      return True  
    elif self.hasFlush() and other.hasFlush():
      pass #compare relative ranks of suits 
    elif self.hasFlush() and not other.hasFlush():
      return True  
    elif self.hasStraight() and other.hasStraight(): 
      pass #compare ranks 
    elif self.hasStraight() and not other.hasStraight():
      return True 
    elif self.hasThreeOfKind() and other.hasThreeOfKind(): 
      pass #compare ranks. 
    elif self.hasThreeOfKind() and not other.hasThreeOfKind(): 
      return True
    elif self.hasTwoPairs() and other.hasTwoPairs():
      pass #compare ranks of pairs 
    elif self.hasTwoPairs() and not other.hasTwoPairs():
      return True 
    elif self.hasOnePair() and other.hasOnePair():
      pass #compare ranks of pairs 
    elif self.hasOnePair() and not other.hasOnePair():
      return True 
    else:
      return False
