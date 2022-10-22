from hand import Hand
import clear

class HandPlayer(Hand):

    def __init__(self, bet, player):
        super().__init__(bet, player)



    def stand(self):
        clear.reset_screen()
        if self.status != "Bust":
            self.status = "Stand"
            print(f"\n{self.player.name.upper()}, YOUR FINAL HAND IS:")
        else:
            print(f"{self.player.name.upper()}, YOU BUST...")
        self.show_hand()
        input()



    def surrender(self):
        clear.reset_screen()
        self.status = "Surrender"
        print(f"\n{self.player.name.upper()}, YOU HAVE GIVEN UP")
        input()



    def double_down(self):
        self.player.chips -= self.bet
        self.bet *= 2
        self.hit()
        self.status = "DoubleDown"


    
    def show_hand(self):
        super().show_hand()
        print(f"   Cards: {self.hand_cards}")
        print(f"   Bet: {self.bet}")           
        print(f"   Balance: {self.player.chips}")
   


    def decision_options(self):
        def get_decision(total):
            while True:
                try:
                    decision = int(input("\nType the number of your decision: "))
                except ValueError:
                    print(f"Input a number between 1 and {total}")
                    continue
                if decision < 1 or decision > total:
                    print(f"Input a number between 1 and {total}")
                else:
                    break
            return decision

        if self.bet > self.player.chips:
            total = 3
            print("1. Stand")
            print("2. Hit")
            print("3. Surrender")
        elif len(self.hand_cards) == 2 and self.status != "Split":
            total = 4
            print("1. Stand")
            print("2. Hit")
            print("3. Surrender")
            print("4. Double Down")
            if self.hand_cards[0] == self.hand_cards[1]:
                print("5. Split")
                total = 5
        else:
            total = 2
            print("1. Stand")
            print("2. Hit")

        return get_decision(total)



    def player_decision(self):
        sum_cards = []
        sum_cards = self.hand_value()
        print(f"\n{self.player.name}, what do you want to do?:\n")
        if len(sum_cards) == 2 and sum_cards[0] == 11:
            print(f"{self.player.name}, you have a BLACKJACK")
            decision = 1
            input("To continue type: OK")
        else:
            decision = self.decision_options()

        if decision == 1:
            self.stand()
        elif decision == 2:
            self.hit()
        elif decision == 3:
            self.surrender()
        elif decision == 4:
            self.double_down()
        elif decision == 5:
            self.status = "Split"

        return decision
 


    def bet_result(self, dealer_hand):
        profit = int
        self.check_max_value()
        if self.max_value == 21 and len(self.hand_cards) == 2:
            if dealer_hand.max_value == 21 and len(dealer_hand.hand_cards) == 2:
                # player and dealer have blackjack
                profit = 0
            else:
                # player has blackjack
                profit = 1.5 * self.bet
        else:
            if self.status == "Surrender":
                profit = -self.bet / 2
            elif self.status == "Bust":
                profit = -self.bet 
            elif dealer_hand.status == "Bust":
                profit = self.bet
            elif dealer_hand.max_value == 21 and len(dealer_hand.hand_cards) == 2:
                # the dealer has blackjack
                profit = -self.bet
            else:
                if self.max_value == dealer_hand.max_value:
                    #Push
                    profit = 0
                elif self.max_value > dealer_hand.max_value:
                    #Player win
                    profit = self.bet
                else:
                    #Player lose
                    profit = -self.bet
        self.player.chips = self.player.chips + self.bet + profit
        return profit

    

    def show_payout(self, profit):
        print(f"\n{self.player.name.upper()}")
        print(f"   Cards: {self.hand_cards}")
        print(f"   Previous balance: {self.player.chips - profit}")
        print(f"   Bet: {self.bet}")
        print(f"   New balance: {self.player.chips}") 