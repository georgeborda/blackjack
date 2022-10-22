from turtle import clear
from game import Game
import clear

def main():
    game = Game()
    game.create_players()
    lets_play = True
    while lets_play:
        game.place_bet()  
        game.deal_round_cards()
        game.show_all_hands()
        game.play()
        game.payout()
        game.buy_chips()
        lets_play = game.check_balances()
    clear.farewell()

if __name__ == '__main__':
    main()