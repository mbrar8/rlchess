import chess
import stockfish
#import tensorflow as tf
import sys

board = chess.Board()

stockfish = Stockfish(path="/mnt/c/users/mahee/ARC/RLChess/stockfish/stockfish_15_x64_avx2.exe")

stockfish.set_elo_rating(3600)
stockfish.set_depth(25)

#agent = something

RLAGENT = 0
STOCKFISH = 1

if len(sys.argv) > 1:
    RLAGENT = sys.argv[1]
    if RLAGENT == 1:
        STOCKFISH = 0
    else:
        STOCKFISH = 1

currentPlayer = 0

while (True):    
    legalMoves = board.legal_moves
    moveText = None
    if currentPlayer == STOCKFISH:
        moveText = stockfish.get_best_move()

    else:
        moveText = agent.getMove(legalMoves)

    move = chess.Move.from_uci(moveText)
    board.push(move)
    stockfish.make_moves_from_current_position([moveText])
    
    if board.is_checkmate():
        print(str(currentPlayer) + " wins")
        # If using win/loss as reward
        if currentPlayer == RLAGENT:
            agent.updateReward(1)
        else:
            agent.updateReward(-1)
        break

    else if board.is_stalemate() or board.is_insufficient_material():
        print("Draw")
        agent.updateReward(0)
        break


    evaluation = stockfish.get_evaluation()[1]["value"]
    # Negative value means player 1 is winning
    if RLAGENT == 1:
        evaluation *= -1

    # Using stockfish evaluation as step by step reward
    agent.updateReward(evaluation)
    
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0


    
    





