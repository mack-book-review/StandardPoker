from rank import Rank
from suit import Suit 
from card import Card
from deck import Deck 

def testDeck():
  d1 = Deck()
  print(len(d1))
  print(d1)
  card1 = d1.deal() 
  print("Dealt card is: " + str(card1))
  print(d1)

def testSuit():
  for suit in (Suit):
    print(suit,end="  ")
    print(type(suit))

def testRank(): 
  for rank in (Rank):
    print(rank,end="  ")
    print(type(rank)) 

def testCard(): 
  h1 = Card(Rank.Two,Suit.Hearts)
  h2 = Card(Rank.Three,Suit.Hearts)
  h3 = Card(Rank.Ten,Suit.Hearts)
  h4 = Card(Rank.Jack,Suit.Hearts)

  c1 = Card(Rank.Two,Suit.Clubs)
  c2 = Card(Rank.Three,Suit.Clubs)
  c3 = Card(Rank.Ten,Suit.Clubs)
  c4 = Card(Rank.Ace,Suit.Clubs)

  c1a = Card(Rank.Two,Suit.Clubs)

  print(c1,c2,c3,end="\n")

  try:
    print("c3 > c1 ->",c3 > c1)
    print("c1 == c1a ->",c1==c1a)
    print("c3 > h1 ->",c3 > h1)
  except RuntimeError as re:
    print(re)
  
  print(h1.getImagePath())
  print(h2.getImagePath())
  print(h3.getImagePath())
  print(h4.getImagePath())

  print(c1.getImagePath())
  print(c2.getImagePath())
  print(c3.getImagePath())
  print(c4.getImagePath())

  