import chess
import chess.pgn
from io import StringIO

def generate_train_set(numLines=None):
    values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    games = []
    with open('data/lichess_db_standard_rated_2019-05.pgn') as pgn:
            for i in range(numLines):

                game = chess.pgn.read_game(pgn)
                if game is None:
                    break
                print(game)
                res = game.headers['Result']
                if res not in values:
                    continue
                value = values[res]
                board = game.board()
            
                for move in game.mainline_moves():
                    board.push(move)
                    if (board.is_game_over()):
                        print("-----------",res)
                print(board,"\n")
                print(board.fen())


'''
def test_data(x=None):
    with open('data/lichess_db_standard_rated_2019-05.pgn') as pgn:
        games = []

        for i in range(x):
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            games.append(game)
            print(games)
    
            for s in games:
                g = chess.pgn.read_game(s)
                g.headers['Result']
                board = g.board()
                for move in g.main_line():
                    board.push(move)

            print(games)
            print(board)

'''


if __name__ == "__main__":

  # test_data(2)
    generate_train_set(1)
