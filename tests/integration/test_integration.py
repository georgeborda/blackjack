import unittest
from unittest.mock import patch
# Let change some parameters of code to test
from game.game import Game
from player.player import Player
import main

class IntegrationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    user_responses = [20, "", 1,"","","","","","","",0]

    @patch('builtins.input', side_effect=iter(user_responses))
    # Let change the user inputs to the variable user_responses
    def test_game_play(self, mock_input):
        """
        Test the execution a round of the game
        """
        test_cases = [
            ("Jorge", 100, 80, 130)
        ]

        dealer = Player(name = "Dealer", chips = 100000)
        self.game.all_players.append(dealer)
        for name, init_chips, less_chips, greater_chips in test_cases:
            new_player = Player(name, init_chips)
            self.game.all_players.append(new_player)
            main.play(self.game)
            self.assertGreaterEqual(self.game.all_players[1].chips, less_chips)
            self.assertLessEqual(self.game.all_players[1].chips, greater_chips)

if __name__ == "__main__":
    unittest.main()