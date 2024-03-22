import random
import unittest
import copy
from BlackJack import Card
from BlackJack import Deck
from BlackJack import BlackJack

class TestCard(unittest.TestCase):
    
    def test_card_color_black(self):
        self.assertEqual(Card('c', 2).color, 'black')
        self.assertEqual(Card('s', 3).color, 'black')
        
    def test_card_color_red(self):
        self.assertEqual(Card('d', 2).color, 'red')
        self.assertEqual(Card('h', 3).color, 'red')
        
    def test_invalid_suite(self):
        with self.assertRaises(ValueError):
            Card('x', 4)


class TestDeckInitialization(unittest.TestCase):
    
    def test_empty_init(self):
        deck = Deck()
        suites_init = [card.suite for card in deck.cards]
        values_init = [card.value for card in deck.cards]
        colors_init = [card.color for card in deck.cards]
        #preparation of a deck of orderd cards
        ordered_one_deck = [Card(suite, value) for suite in ['s', 'd', 'c', 'h'] for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']]
        suites_ref = [card.suite for card in ordered_one_deck]
        values_ref = [card.value for card in ordered_one_deck]
        colors_ref = [card.color for card in ordered_one_deck]
        
        self.assertEqual([suites_init,values_init,colors_init], [suites_ref,values_ref,colors_ref], "The initialized deck is not " + str(ordered_one_deck))
    
    def test_shuffled_list_init(self):
        #Preparation of shuffled deck
        custom_carads = [Card(suite, value) for suite in ['s', 'd', 'c', 'h'] for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']]
        random.shuffle(custom_carads)
        print(custom_carads)
        
        #Intance with shuffled deck
        deck = Deck(custom_carads)
        #Test
        self.assertEqual(deck.cards, custom_carads, "The initial deck is not " + str(custom_carads))
    
class TestDeckMethods(unittest.TestCase):
    def test_shuffle(self):
        game = Deck()
        dc_game = copy.deepcopy(game)
        inital_cards = dc_game.cards
        game.shuffle()
        isShuffeld = (game.cards != inital_cards)
        test_msg = (
            "\nThe \n" 
            + str(inital_cards) 
            + "\n after the shuffle is \n" 
            + str(game.cards)
            )
        print(test_msg )
        assert_msg = (
            "The .shuffle method is not working!"
            + "\nThe initial deck was\n" 
            + str(inital_cards)
            + "\nbut after the shuffle, it is\n"
            + str(game.cards)
            )
        self.assertTrue(isShuffeld,assert_msg )


class testBlackJack(unittest.TestCase):
    def test_empty_init(self):
        game = BlackJack()
        
        
        
        
    def test_black_jack_5player_init(self):
        game_with_5_player = BlackJack(number_of_players=5)
        game_with_5_player.player_cards
        expected_player_cards_for_5_player = {1: ['',''],
                                              2: ['',''],
                                              3: ['',''],
                                              4: ['',''],
                                              5: ['','']}
        
        asset_msg = (
            '\nThe expected players_card variable \n '
            + str(expected_player_cards_for_5_player)
            +'\nand the BlackJakc.players_card variable\n'
            + str(game_with_5_player.player_cards)
            +'are not same!'
        )
    
        self.assertEqual(game_with_5_player.player_cards, expected_player_cards_for_5_player, asset_msg)
    
    def test_black_jack_shuffled_deck_init(self):
        deck_1 = Deck()
        deck_1.shuffle
        game_shuffled_deck = BlackJack(deck = deck_1)
        blackjackdeck, input_deck = game_shuffled_deck.deck.cards,deck_1.cards 
        asset_msg = (
            '\nThe input deck \n '
            + str(input_deck)
            +'\nand the deck in the BlackJack object\n'
            + str(blackjackdeck)
            +'are not same!'
        )
        self.assertEqual(game_shuffled_deck.deck.cards,deck_1.cards, asset_msg)
        
    def test_black_jack_deal_to_player(self):
        game =  BlackJack(number_of_players=3,deck=Deck())
        game.inital_deal()
        for player_number in range(1,game.number_of_players+1,1):
            game.deal_to_player(player_number)
            print(str(game.player_cards[player_number][:-1]))
        
        
if __name__ == '__main__':
    unittest.main()

