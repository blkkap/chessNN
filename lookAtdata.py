import chess
import chess.pgn 


def info():
    with open('data/lichess_db_standard_rated_2019-05.pgn') as pgn:
        while 1:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            results = game.headers['Result']
            print(game)
            print("game results: ", {results})




if __name__ == '__main__':
    info()
