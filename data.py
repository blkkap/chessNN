import chess
import chess.pgn






def generate_train_set(numLines=None):
    values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    games = []
    with open('data/lichess_db_standard_rated_2019-05.pgn') as pgn:
            for i in range(numLines):

                game = chess.pgn.read_game(pgn)
                if game is None:
                    break
                games.append(game)
                for j in games:

                    res = j.headers['Result']
                    if res not in values:
                        continue
                    value = values[res]
                    board = j.board()
            
                    for move in j.mainline_moves():
                        board.push(move)
                        if (board.is_game_over()):
                            print("-----------",res)
                    print(board,"\n")

if __name__ == "__main__":
    generate_train_set(3)
