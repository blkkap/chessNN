import chess 
import chess.pgn
from  parsita import *
from parsita.util import constant
import json


def formatannotations(annotations):
    return {ant[0]: ant[1] for ant in annotations}

def formatgame(game):
    return{
        'moves': game[0],
        'outcome': game[1]
    }
def formatentry(entry):
    return {'annotations': entry[0], 'game': entry[1]}

def handleoptional(optionalmove):
    if len(optionalmove) > 0:
        return optionalmove[0]
    else:
        return None

# PGN Grammar
quote = lit(r'"')
tag = reg(r'[\u0021-\u0021\u0023-\u005A\u005E-\u007E]+')
string = reg(r'[\u0020-\u0021\u0023-\u005A\u005E-\U0010FFFF]+')
whitespace = lit(' ') | lit('\n')
annotation = '[' >> (tag) << ' ' & (quote >> string << quote) << ']'
annotations = repsep(annotation, '\n') > formatannotations
nullmove = lit('--') # Illegal move rarely used in annotations
longcastle = reg(r'O-O-O[+#]?')
castle = reg(r'O-O[+#]?')
regularmove = reg(r'[a-h1-8NBRQKx\+#=]+') # Matches more than just chess moves
move = regularmove | longcastle | castle | nullmove
movenumber = (reg(r'[0-9]+') << '.' << whitespace) > int
turn = movenumber & (move << whitespace) & (opt(move << whitespace) > handleoptional)
draw = lit('1/2-1/2')
white = lit('1-0')
black = lit('0-1')
outcome = draw | white | black
game = (rep(turn) & outcome) > formatgame
entry = ((annotations << rep(whitespace)) & (game << rep(whitespace))) > formatentry
file = rep(entry)

with open('data/lichess_db_standard_rated_2025-12.pgn', 'r') as f:
    games = []
    
    def read_games(data):
        while True:
            game = file.parse(data.read())
            if game is None:
                break
            yield game

    for idx, game in enumerate(read_games(f)):
        if idx < 10:
            games.append(game)
        else:
            break
for game in games:
    print(game)

