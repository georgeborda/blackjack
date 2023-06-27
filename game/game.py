from player.player import Player
from hands.handplayer import HandPlayer
from hands.handdealer import HandDealer
import utils.clear as clear

class Game:

    all_players = []
    round_hands = []
    players_name = []


    def create_players(self):
        clear.reset_screen()
        while True:
            try:
                number_players = int(input("How many players are there (1 - 5)? "))
            except ValueError:
                print("Input a number")
                continue
            if number_players < 1 or number_players > 5:
                print("Input a number between 1 and 5")
            else:
                break

        dealer = Player(name = "Dealer", chips = "1000000")
        self.all_players.append(dealer)
        clear.reset_screen()
        for player in range(number_players):
            name_player = input(
                f"What is the name of player number {player + 1 }? ")
            self.players_name.append(name_player)
            while True:
                try:
                    chips = int(input(f"How many chips will buy {name_player}? "))
                    print("\n")
                except ValueError:
                    print("Input a number")
                    continue
                if chips < 1:
                    print("Input a number greater than 0")
                else:
                    break
                
            new_player = Player(name_player, chips)
            self.all_players.append(new_player)
        
      
  
    def place_bet(self):
        """Ask for a bet, create the hands and link each one with the player"""
        clear.reset_screen()
        self.round_hands.clear()
        sum_bet = 0
        for player in self.all_players:
            if player.name == "Dealer":
                player_bet = 0
                new_hand = HandDealer(bet = player_bet, player = player)
                self.round_hands.append(new_hand)
            elif player.chips != 0:
                print(f"{player.name} your balance is {player.chips} chips")
                while True:
                    try:
                        player_bet = int(input(f"What is your bet? "))
                    except ValueError:
                        print("Input a number")
                    if player_bet < 0:
                        print("The bet can´t be negative")
                    elif player_bet > player.chips:
                        print("The bet can´t be greater than your balance")
                    else:
                        break
                if player_bet != 0:
                    new_hand = HandPlayer(bet = player_bet, player = player)
                    player.chips -= player_bet
                    self.round_hands.append(new_hand)
                print("\n")
            sum_bet += player_bet
        if sum_bet == 0:
            print("\nNo player place a bet")
            input()
            self.place_bet()
         
  

    def deal_round_cards(self):
        for i in range(2):
            for hand in self.round_hands:
                hand.deal_card()



    def show_all_hands(self, is_final_hand = False):
        clear.reset_screen()
        print("These are the hands:\n")
        for hand in self.round_hands:
            hand.show_hand()
        input("")



    def split(self, index):
        """Split the hand when the player has two equal cards, deal a new card for each hand and place a bet for the second hand"""
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
        """The players play, take their decisions, the dealer shows his hidden card and plays too"""
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
                    if decision  == 5:
                        self.split(index)
                if hand.status == "Split":
                    index -= 1
            index += 1
        print("The dealer hand is:\n")
        dealer_hand.dealer_play()



    def payout(self):
        """The dealer takes or gives money depending on the hands and bets"""
        clear.reset_screen()
        dealer_hand = self.round_hands[0]
        dealer_hand.check_max_value()
        print(f"\n{dealer_hand.player.name.upper()}")
        print(f"   Cards: {dealer_hand.hand_cards}")
        for index in range(1, len(self.round_hands)):
            hand = self.round_hands[index]
            profit = hand.bet_result(dealer_hand)
            hand.show_payout(profit)
        input()



    def buy_chips(self):
        clear.reset_screen()
        print("Will any player buy chips?\n")
        for i in range(len(self.players_name)):
            print(f"{i + 1}. {self.players_name[i]}")
        buy = True
        while buy:
            try:
                selection = int(input("\nSelect the number of the player or type 0 to continue: "))
            except ValueError:
                print(f"Type a number between 0 and {len(self.players_name)}")
                continue
            if selection < 0 or selection > len(self.players_name):
                print(f"Type a number between 0 and {len(self.players_name)}")
            else:
                if selection == 0:
                    buy = False
                else:
                    while True:
                        try:
                            chips = int(input(f"\n{self.all_players[selection].name}, how many chips will you buy? "))
                        except ValueError:
                            print("Type a number.")
                            continue
                        if chips < 0:
                            print("Type a number greater than 0.")
                        else: 
                            break
                    self.all_players[selection].chips += chips
                    another_buy = input("\nType 'yes' if another player wants to buy chips: ")
                    if another_buy.lower() != 'yes':
                        buy = False

            
         #self.all_players[selection].chips += 



    def check_balances(self):
        any_player_with_chips = False
        for index in range(1, len(self.all_players)):
            if self.all_players[index].chips > 0:
                any_player_with_chips = True
        return any_player_with_chips
            
            
            
    
        
    