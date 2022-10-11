import cards
import clear
import random
import cards

class Hand:
    
    def __init__(self, bet, player):
        self.bet = bet
        self.player = player
        self.hand_cards = [] 
        self.status = "InGame"

  
    def deal_card(self):
        random_card = random.choice(cards.cards_list)
        self.hand_cards.append(random_card)


    def stand(self):
        clear.reset_screen()
        if self.status != "Bust":
            self.status = "Stand"
            print(f"\n{self.player.name.upper()}, YOUR FINAL HAND IS:")
        else:
            print(f"{self.player.name.upper()}, YOU BUST...")
        self.show_hand()
        input()


    def hit(self):
        self.deal_card()


    def surrender(self):
        clear.reset_screen()
        self.status = "Surrender"
        print(f"\n{self.player.name.upper()}, YOU HAVE GIVEN UP")
        input()


    def double_down(self):   # Se está ejecutando doble vez cuando se hace bust
        self.bet *= 2
        self.hit()
        self.status = "Stand"
        
      

    def split(self):
        pass


    def hand_value(self):
        sum = []
        sum.append(0)
        for card in self.hand_cards:
            sum[0] += cards.cards_values[card]
        if "A" in self.hand_cards:
            sum.append(0)
            sum[1] = sum[0] + 10
        return sum


    def show_hand(self):
        print(f"\n{self.player.name}:")
        if self.bet != 0:
            print(f"   Cards: {self.hand_cards}")
            print(f"   Bet: {self.bet}")
            print(f"   Balance: {self.player.chips - self.bet}")
        else:
            dealer_hand = self.hand_cards
            dealer_hand[0] = " "
            print(f"   Cards: {dealer_hand}")

  
    def check_hand_status(self):
        if self.hand_value()[0] > 21:
            self.status = "Bust"
            self.stand()
        elif self.status == "Stand":
            self.stand()
        if self.status != "InGame":
            return False
        else:
            return True

    
    def decision_options(self):
        def get_decision(total):
            decision = int(input("\nType the number of your decision: "))
            if decision < 1 or decision > total:
                print("The number is not a valid option")
                get_decision(total)
            return decision

        if len(self.hand_cards) == 2:
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
            self.split()
            