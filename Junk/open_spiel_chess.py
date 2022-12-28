import numpy as np
import tensorflow as tf
import pyspiel
import stockfish

game = pyspiel.load_game("chess")
stockfish.set_elo_rating(3600)
stockfish.set_depth(25)

# Starting by having stockfish play white (as more often I assume we'll have user play white)

state = game.new_initial_state()
stockPlayer = 1
rlPlayer = 0

while not state.is_terminal():
    if state.current_player() == stockPlayer:
        stockMove = stockfish.get_best_move()
        stockAction = stockMove
        state.apply_action(stockAction)
        continue

    legal_actions = state.legal_actions()
    action = legal_actions[0]
    state.apply_action(action)
    reward = stockfish.get_evaluation()


