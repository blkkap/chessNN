import chess
import chess.pgn
from boardState import boardState
import numpy as np

def generate_train_set(numLines=None):
    values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    gn = 0
    X, y =  [],[]

    with open('data/lichess_db_standard_rated_2019-05.pgn') as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
           # print(game)
            res = game.headers['Result']
            if res not in values:
                continue
            value = values[res]
            board = game.board()
            
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                ser = boardState(board).serialize()
                X.append(ser)
                y.append(value)
            print("parsing game %d, got %d examples" % (gn, len(X)))
            if numLines is not None and len(X) > numLines:
                return X,y
            gn += 1
        X = np.array(X)
        y = np.array(y)
        return X,y
                

if __name__ == "__main__":

  # test_data(2)
    X,y = generate_train_set(100000)
    
