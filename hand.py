import cards
class Hand:
    
    def __init__(self, bet, player):
        self.bet = bet
        self.player = player
        self.hand_cards = []    

    def surrender(self):
        return True

    def double_down(self):
        pass

    def stand(self):
        pass

    def split(self):
        pass

    def hit(self):
        pass

    def hand_value(self):  # IN PROCESS
        sum = []
        sum.append(0)
        for card in self.hand_cards:
            sum[0] += cards.cards_values[card]
        if "A" in self.hand_cards:
            sum.append(0)
            sum[1] = sum[0] + 10
        return sum