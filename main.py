from game.game import Game
import utils.clear as clear

def play(game):
    game.place_bet()  
    game.deal_round_cards()
    game.show_all_hands()
    game.play()
    game.payout()

def main():
    game = Game()
    game.create_players()
    lets_play = True
    while lets_play:
        play(game)
        game.buy_chips()
        lets_play = game.check_balances()
    clear.farewell()
        
    
        
if __name__ == '__main__':
    main()