"""

    For Texas Hold'em, there are 4 rounds of betting:
        (1) Preflop:  Each player has 2 hole cards which only they can see.  There are no community
        cards on the table at this point.  The hole cards need to be checked if a pair is formed.
        If the two hole cards are of the same suit, it increases the possibility of a flush.
        This also may influence betting in this round.
        (2) Flop:   In addition to the 2 hole cards, there are 3 community cards available.
            Here, we analyze the standard 5 card poker hand.  More advanced algorithms would also
            take into account that 4 cards of the same suit could lead to a flush or that 4 cards that are in consecutive order
            could lead to a straight.  Three of kind might very well lead to four of a kind.
        (3) Turn:   In addition to the 2 hole cards, there are 4 community cards.  There are 6 combinations of 5-card poker hands
        that have to be analyzed to determine the quality of the hand.
        (4) River:  In addition to the 2 hole cards, there are 5 community cards.  There are 21 combinations of 5-card poker hands
        that have to be analyze to determine the quality of a hand.
"""

def factorial(n):
    if n == 1:
        return 1
    if n > 1:
        return n*factorial(n-1)

def combinations(n,r):
    return (factorial(n)/(factorial(n-r)*factorial(r)))

def main():
    print("Factorial of 4: " + str(factorial(4)))
    turn_combos = combinations(6,5)     #turn
    river_combos = combinations(7,5)    #river
    print("Turn Combinations: " + str(turn_combos))
    print("River Combinations: " + str(river_combos))

if __name__ == "__main__":
    main()