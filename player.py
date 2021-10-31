import pygame 
from pot import Pot,Pot2
from chipentry import ChipEntry
from chiptype import ChipType
from pokerhand import PokerHand

class Player(object):

  INITIAL_POT_1 = {
    "white": 1000,
    "red": 200,
    "blue": 100,
    "green": 40,
    "black": 10
  }

  INITIAL_POT_2 = [
    ChipEntry(ChipType.White,1000),
    ChipEntry(ChipType.Red,200),
    ChipEntry(ChipType.Blue,100),
    ChipEntry(ChipType.Green,40),
    ChipEntry(ChipType.Black,10)
  ]


  def __init__(self):
    self.pot = Pot2(Player.INITIAL_POT_2)
    self.pokerHand = PokerHand()