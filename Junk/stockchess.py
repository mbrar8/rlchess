#import numpy as np
#import tensorflow as tf
from stockfish import Stockfish

stockfish = Stockfish(path="/mnt/c/users/mahee/ARC/RLChess/stockfish/stockfish_15_x64_avx2.exe")


stockfish.set_elo_rating(3600)
stockfish.set_depth(25)

# Starting by having stockfish play white (as more often I assume we'll have user play white)
fishFirst = True


stockMove = stockfish.get_best_move()
stockAction = stockMove
state.apply_action(stockAction)

legal_actions = state.legal_actions()
action = legal_actions[0]
state.apply_action(action)
reward = stockfish.get_evaluation()


