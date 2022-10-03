from player import Player
from hand import Hand
import random
import cards


class Game:

    all_players = []
    round_hands = []

  
    def create_players(self):
        number_players = int(input("How many players are there? "))
        for player in range(number_players):
            name_player = input(
                f"\nWhat is the name of player number {player + 1 }? ")
            chips = int(input(f"How many chips will buy {name_player}? "))
            new_player = Player(name_player, chips)
            self.all_players.append(new_player)
        dealer = Player(name = "Dealer", chips = "1000000")
        self.all_players.append(dealer)
      
  
    def place_bet(self):
        self.round_hands.clear()
        sum_bet = 0
        for player in self.all_players:
            if player.name == "Dealer":
                player_bet = 0
                new_hand = Hand(bet = player_bet, player = player)
                self.round_hands.append(new_hand)
            else:
                player_bet = int(input(f"{player.name}, what is your bet? "))
                if player_bet != 0:
                    new_hand = Hand(bet = player_bet, player = player)
                    self.round_hands.append(new_hand)
                
            sum_bet += player_bet
        if sum_bet == 0:
            print("No player place a bet")
            self.place_bet()
    

    def deal_card(self, hand):
        random_card = random.choice(cards.cards_list)
        hand.hand_cards.append(random_card)
         
  
    def deal_round_cards(self):
        
        for i in range(2):
            for hand in self.round_hands:
                self.deal_card(hand)

  
    def show_cards(self):
        dealer_hand = self.round_hands[len(self.round_hands) - 1].hand_cards
        dealer_hand[0] = " "
        for hand in self.round_hands:
            print(f"\n{hand.player.name}:")
            if hand.bet != 0:
                print(f"   Cards: {hand.hand_cards}")
                print(f"   Bet: {hand.bet}")
                print(f"   Balance: {hand.player.chips - hand.bet}")
            else:
                print(f"   Cards: {dealer_hand}")

  
    def decision_options(self, hand_cards):
        
        def get_decision(total):
            decision = int(input("Type the number of your decision"))
            if decision < 1 or decision > total:
                print("The number is not a valid option")
                get_decision(total)
            return decision

        if len(hand_cards) == 2:
            total = 4
            print("1. Surrender")
            print("2. Stand")
            print("3. Hit")
            print("4. Double Down")
            if hand_cards[0] == hand_cards[1]:
                print("5. Split")
                total = 5
        else:
            total = 2
            print("1. Stand")
            print("2. Hit")

        return get_decision(total)
      
    
    def players_decision(self):    #Not finished
        sum_cards = []
        for hand in self.round_hands:
            sum_cards = hand.hand_value()
            if len(sum_cards) == 2 and sum_cards[0] == 11:
                print(f"{hand.player.name}, you have a BLACKJACK")
                decision = "stand"  # Fix
                input("To continue type: OK")
            else:
                deicision = self.decision_options(hand.hand_cards)