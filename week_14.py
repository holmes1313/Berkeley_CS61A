
import random
import sqlite3

points = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
points.update({n: n for n in range(2, 11)})

def hand_score(hand):
    """Total score for a hand."""
    total  = sum([points[card] for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

db = sqlite3.Connection('cards.db')
sql = db.execute
#sql('DROP TABLE if exits cards;')
sql('CREATE TABLE cards(card, who);')

def deal(card, who):
    """Deal a card face up."""
    sql('INSERT INTO cards VALUES (?, ?);', (card, who))
    db.commit()
    
def score(who):
    """Compute the hand score for the player or dealer"""
    cards = sql('SELECT * FROM cards WHERE who=?;', [who])
    return hand_score([card for card, who in cards.fetchall()])

def bust(who):
    """check if the player or dealer went bust."""
    return score(who) > 21

player, dealer = "Player", "Dealer"

def play_hand(deck):
    deal(deck.pop(), player)
    deal(deck.pop(), dealer)
    deal(deck.pop(), player)
    hidden = deck.pop()
    
    while 'y' in input("Hit? ").lower():
        deal(deck.pop(), player)
        if bust(player):
            print(player, 'went bust!')
            return
        
    deal(hidden, dealer)
    
    while score(dealer) < 17:
        deal(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, 'went bust!')
            return
    
    print(player, score(player), "and", dealer, score(dealer))
    
deck = list(points.keys()) * 4
random.shuffle(deck)
while len(deck) > 10:
    print('\nDealing...')
    play_hand(deck)
    sql('UPDATE cards SET who="Discard";')








