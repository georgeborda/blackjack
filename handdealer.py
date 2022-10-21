from hand import Hand
import clear

class HandDealer(Hand):

    def __init__(self, bet, player):
        super().__init__(bet, player)



    def stand(self):
        clear.reset_screen()
        if self.status != "Bust":
            self.status = "Stand"
            print(f"\nTHE DEALER FINAL HAND IS:")
        else:
            print(f"THE DEALER BUST...")
        self.show_hand()
        input()


    
    def show_hand(self):
        super().show_hand()
        dealer_hand = list(self.hand_cards)
        if self.status == "InGame":
            dealer_hand[0] = " "
        print(f"   Cards: {dealer_hand}")
        


    def dealer_play(self):
        clear.reset_screen()
        sum_cards = []
        sum_cards = self.hand_value()
        max_value = sum_cards[len(sum_cards) - 1]
        self.status = "Playing"
        self.show_hand()
        if max_value > 21 and len(sum_cards) == 2:
            max_value = sum_cards[0]
            
        if max_value >= 17:
            input("\nThis is the dealer's final hand")
            check = self.check_hand_status()
            if check:
                self.stand()
        else:
            input("\nThe dealer has to hit...")
            self.hit()
            self.dealer_play()