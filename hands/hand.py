import utils.cards as cards
import random

class Hand:
    
    def __init__(self, bet, player):
        self.bet = bet
        self.player = player
        self.hand_cards = [] 
        self.status = "InGame"
        self.max_value = 0

  

    def deal_card(self):
        random_card = random.choice(cards.cards_list) 
        self.hand_cards.append(random_card)



    def hit(self):
        self.deal_card()



    def hand_value(self):
        """"Create a list with the sum of the cards in the hand"""
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



    def check_hand_status(self):
        if self.hand_value()[0] > 21:
            self.status = "Bust"
            self.stand()
        elif self.status == "DoubleDown":
            self.stand()
            
        if self.status != "InGame" and self.status != "Split" and self.status != "Playing":
            return False
        else:
            return True



    def check_max_value(self):
        hand_values = self.hand_value()
        if len(hand_values) == 2:
            if hand_values[1] <= 21:
                self.max_value = hand_values[1]
        else:
            self.max_value = hand_values[0]
        #return self.max_value
    

            