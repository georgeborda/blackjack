import cards
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


    def hit(self):
        self.deal_card()


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
        elif self.status == "DoubleDown":
            self.stand()
            
        if self.status != "InGame":
            return False
        else:
            return True

    

            