from game import Game

def main():
    game = Game()
    game.create_players()
    game.place_bet()  
    game.deal_round_cards()
    game.show_cards()
    game.players_decision()

if __name__ == '__main__':
    main()