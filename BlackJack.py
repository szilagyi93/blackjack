import random
class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.color = self.get_color()

    def get_color(self):
        if self.suite == 'c' or self.suite == 's':
            return 'black'
        elif self.suite == 'd' or self.suite == 'h':
            return 'red'
        else:
            raise ValueError("Invalid suite value")

class Deck:
    def __init__(self,cards=None):
        self.cards = list()
        self.deck_number = int()
        
        cardsIsNone = cards is None
        if cardsIsNone:
            for suit in ['s','d','c','h']:
                for value in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']:
                    self.cards.append(Card(suit,value))
            self.deck_number = self.number_of_decks()
        else:
            if not cardsIsNone:
                cards_is_list_type = isinstance(cards,list)
                if cards_is_list_type:
                    self.cards = cards
                    self.deck_number = self.number_of_decks()     
                else: 
                    
                    raise TypeError("ERROR: cards wrong type! Plese use list!")         
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def number_of_decks(self, custom_cards=None):
        if custom_cards:
            number_of_custom_cards = len(custom_cards)
            return self.can_be_div_by_52(number_of_custom_cards)
        else: 
            number_of_cards = len(self.cards)
            return self.can_be_div_by_52(number_of_cards)
        
    def can_be_div_by_52(self, number):
        if number % 52 == 0:
            return number / 52
        else:
            raise ValueError
        

class BlackJack(): 
    def __init__(self,number_of_players=None, deck=None):
        deckIsNone = deck is None
        numberOfPlayersIsNone = number_of_players is None
        self.dealer_cards = { 0 : ['','']}
        self.player_cards = {int : ['','']}
        if deckIsNone and numberOfPlayersIsNone:
            self.deck = Deck()
            self.number_of_players = 1
            self.player_cards = { 1 : ['','']}
        else:
            if not deckIsNone:
                deck_is_Deck_type = isinstance(deck,Deck)
                if deck_is_Deck_type:
                    self.deck = deck
                    self.number_of_players = 1
                    self.player_cards = { 1 : ['','']}
                else: 
                    raise TypeError("ERROR: deck wrong type! Plese use Deck!")
            
            if not numberOfPlayersIsNone:
                number_of_players_is_int = isinstance(number_of_players,int)
                if number_of_players_is_int:
                    if number_of_players >= 1:
                        self.deck = Deck()
                        self.number_of_players = number_of_players
                        self.player_cards = {num_player : ['', ''] for num_player in range(1, self.number_of_players + 1)}
                    else: 
                        raise TypeError("ERROR: number_of_players must be positive!")
                else: 
                    raise TypeError("ERROR: number_of_players wrong type! Plese use int!")
        None
        
    def inital_deal(self):
        for i in [0,1]:
            for player_number in  self.player_cards.keys():
                self.player_cards[player_number][i] = self.deck.cards[0]
                self.deck.cards.pop(0)
            self.dealer_cards[0][i] = self.deck.cards[0]
            self.deck.cards.pop(0)
        self.dealer_cards

    def deal_to_player(self,player_number):
        self.player_cards[player_number][i] = self.deck.cards[0]
        self.deck.cards.pop(0)
        
        

     
if __name__ == '__main__':
    Card()
    Deck()
    BlackJack()
    game = BlackJack(number_of_players=5)
    game.deal()