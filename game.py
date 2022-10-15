from player import Player
from hand import Hand
from handplayer import HandPlayer
from handdealer import HandDealer
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
                new_hand = HandDealer(bet = player_bet, player = player)
                self.round_hands.append(new_hand)
            else:
                print(f"{player.name} your balance is {player.chips} chips")
                player_bet = int(input(f"What is your bet? "))
                if player_bet != 0:
                    new_hand = HandPlayer(bet = player_bet, player = player)
                    player.chips -= player_bet
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


    def split(self, index):
        clear.reset_screen()
        first_hand = self.round_hands[index]
        player = first_hand.player
        split_card = first_hand.hand_cards[1]
        first_hand.hand_cards.pop(1)
        print(f"{player.name}, you split a pair of {split_card}")
        second_bet = int(input(f"\nYour current balance is {player.chips}.\nWhat is your bet for your second hand?: "))

        if second_bet != 0:
            second_hand = HandPlayer(bet = second_bet, player = player)
            second_hand.status = "Split"
            second_hand.player.chips -= second_bet
            self.round_hands.insert(index + 1, second_hand)

        first_hand.deal_card()
        second_hand.hand_cards.append(split_card)
        second_hand.deal_card()


    def play(self):
        dealer_hand = self.round_hands[0]
        index = 0
        while index < len(self.round_hands):
            hand = self.round_hands[index]
            if hand.player.name != "Dealer":
                while hand.check_hand_status():
                    clear.reset_screen()
                    dealer_hand.show_hand()
                    hand.show_hand()
                    decision = hand.player_decision()
                    if decision == 5:
                        self.split(index)
                if hand.status == "Split":
                    index -= 1
            index += 1
            
    
        
    