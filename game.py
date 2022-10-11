from player import Player
from hand import Hand
import random
import cards
import clear

class Game:

    all_players = []
    round_hands = []

    def create_players(self):
        clear.reset_screen()
        number_players = int(input("How many players are there? "))
        dealer = Player(name = "Dealer", chips = "1000000")
        self.all_players.append(dealer)
        for player in range(number_players):
            name_player = input(
                f"\nWhat is the name of player number {player + 1 }? ")
            chips = int(input(f"How many chips will buy {name_player}? "))
            new_player = Player(name_player, chips)
            self.all_players.append(new_player)
        
      
  
    def place_bet(self):
        clear.reset_screen()
        self.round_hands.clear()
        sum_bet = 0
        for player in self.all_players:
            if player.name == "Dealer":
                player_bet = 0
                new_hand = Hand(bet = player_bet, player = player)
                self.round_hands.append(new_hand)
            else:
                print(f"{player.name} your balance is {player.chips} chips")
                player_bet = int(input(f"What is your bet? "))
                if player_bet != 0:
                    new_hand = Hand(bet = player_bet, player = player)
                    self.round_hands.append(new_hand)
            sum_bet += player_bet
        if sum_bet == 0:
            print("No player place a bet")
            self.place_bet()
         
  
    def deal_round_cards(self):
        for i in range(2):
            for hand in self.round_hands:
                hand.deal_card()

      
    def show_all_hands(self):
        clear.reset_screen()
        print("These are the hands:\n")
        for hand in self.round_hands:
            hand.show_hand()
        input("\nType any character to continue.")


    def play(self):
        dealer_hand = self.round_hands[0]
        for hand in self.round_hands:
            if hand.player.name != "Dealer":
                while hand.check_hand_status():
                    clear.reset_screen()
                    dealer_hand.show_hand()
                    hand.show_hand()
                    hand.player_decision()
        
    