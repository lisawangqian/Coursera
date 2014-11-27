# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []	
    
    def __str__(self):
        # return a string representation of a hand
        s=''
        for h in self.hand:
            s+=str(h)+' '
        return "Hand contains "+ s	
    
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)	
    
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        for h in self.hand:
           hand_value += VALUES[h.get_rank()]
        for h in self.hand:
           if (h.get_rank()=='A') and (hand_value<=11):
                hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        n = 0
        for h in self.hand:
            h.draw (canvas,[(pos[0]+88*n), pos[1]])
            n+=1
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck=[Card(s_deck, r_deck) for s_deck in SUITS for r_deck in RANKS]
                

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        s=''
        for c in self.deck:
            s += str(c) + ' '
        return "Deck contains "+ s	
    


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer_hands, player_hands, deck_dealer, score
    
    dealer_hands = Hand()
    player_hands = Hand()
    deck_dealer = Deck()
    deck_dealer.shuffle()
    
    dealer_hands.add_card(deck_dealer.deal_card())
    dealer_hands.add_card(deck_dealer.deal_card())
    
    player_hands.add_card(deck_dealer.deal_card())
    player_hands.add_card(deck_dealer.deal_card())
    
    if in_play==True:
       score -= 1
       outcome = "You lose. New deal. Hit or stand?"
    if in_play==False:
       outcome = "New deal. Hit or stand?"
    
    in_play = True

def hit():
    # replace with your code below
    global outcome, in_play, dealer_hands, player_hands, deck_dealer, score
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    if in_play==True:
        if player_hands.get_value()<=21:
             player_hands.add_card(deck_dealer.deal_card())
             outcome="Hit or stand?"
        
        if player_hands.get_value()>21:
             outcome="You have busted. You lose. New deal? "
             score-=1
             in_play=False
                
             
    
def stand():
    # replace with your code below
    global outcome, in_play, dealer_hands, player_hands, deck_dealer, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    if in_play==True:
        while dealer_hands.get_value()<17:
            dealer_hands.add_card(deck_dealer.deal_card())
        
        if dealer_hands.get_value()>21:
            outcome="Dealer has busted. You win. New deal?"
            score+=1
        else:
            if dealer_hands.get_value() < player_hands.get_value():
               outcome="You win. New deal?"
               score+=1
            else:
               outcome="You lose. New deal?"
               score-=1
            
    in_play=False        
            
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    dealer_hands.draw (canvas, [100, 200])
    
    if in_play==True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
    player_hands.draw (canvas, [100, 400])
    
    canvas.draw_text("Blackjack", [190,60], 55, "Blue")
    canvas.draw_text("Score: " + str(score), [400,150], 35, "Black")
    canvas.draw_text("Dealer", [90,180], 35, "Black")
    canvas.draw_text("Player", [90,380], 35, "Red")
    canvas.draw_text(outcome, [170,350], 26, "Black")
    


    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
