import unittest
from hands.handdealer import HandDealer
from hands.handplayer import HandPlayer
from player.player import Player

class test_hands(unittest.TestCase):

    def setUp(self) -> None:
        """
        It helps me to create player and hand, and use them in all functions. Instead of create them in each function
        """
        self.player = Player(name='Jorge',chips=100)
        self.handplayer = HandPlayer(bet=20, player=self.player)
        self.dealer = Player(name = "Dealer", chips = "1000000")
        self.handdealer = HandDealer(bet=10, player=self.dealer)
    


    def test_deal_card(self):
        """
        Test that can deal a card
        """
        self.handplayer.deal_card()
        self.assertEqual(len(self.handplayer.hand_cards), 1)
        self.handplayer.deal_card()
        self.assertEqual(len(self.handplayer.hand_cards), 2)
    


    def test_hand_value(self):
        """
        Test that check the hand values
        """
        test_cases = [
            (["2","3"], [5]),
            (["K","J"], [20]),
            (["4","A","10"], [15,25])
        ]

        for cards, expected_value in test_cases:
            with self.subTest(cards = cards):
                self.handplayer.hand_cards = cards
                self.assertEqual(self.handplayer.hand_value(), expected_value)



    def test_check_max_value(self):
        """
        Test to check max value of a hand
        """

        test_cases = [
            (["4","A","10"], 15),
            (["K","7","2"], 19),
            (["K","A"], 21)
        ]

        for cards, expected_max_value in test_cases:
            with self.subTest(cards = cards):
                self.handplayer.hand_cards = cards
                self.handplayer.check_max_value()
                self.assertEqual(self.handplayer.max_value, expected_max_value)

        

    def test_bet_result(self):
        """
        Test to check if the bet result is increasing or decreasing the player chips correctly
        """
        test_cases = [
            (["7","A"], ["7","J"], 20, 100, 20),
            (["8","A"], ["9","J"], 20, 100, 0),
            (["K","A"], ["K","J"], 20, 100, 30),
            (["K","A"], ["K","J","A"], 20, 100, 30),
            (["K","J","A"], ["A","J"], 20, 100, -20),
            (["K","A"], ["A","J"], 20, 100, 0)
        ]

        for player_cards, dealer_cards, bet, chips, profit in test_cases:
            with self.subTest(player_cards = player_cards):
                self.handplayer.hand_cards = player_cards
                self.handdealer.hand_cards = dealer_cards
                self.handplayer.bet = bet
                self.player.chips = chips
                self.handdealer.check_max_value()
                self.assertEqual(self.handplayer.bet_result(self.handdealer), profit)




if __name__ == '__main__':
    unittest.main()