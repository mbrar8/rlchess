import mcts_simple
import chess


class ChessMCTS(mcts_simple.Game):


    def __init__(self):
        self.board = chess.Board()
        self.players = {chess.WHITE: 0, chess.BLACK: 1}

    def render(self):
        return str(self.board)


    def get_state(self):
        return tuple(self.board.move_stack)



    def number_of_players(self):
        return 2


    def current_player(self):
        return self.players[self.board.turn]


    def possible_actions(self):
        return [move.uci() for move in self.board.legal_moves]

    def take_action(self, action):
        if action in self.board.legal_moves:
            self.board.push(chess.Move.from_uci(action))

    def delete_last_action(self):
        self.board.pop()

    def has_outcome(self):
        if self.board.outcome() is None:
            return False
        return True

    def winner(self):
        if self.has_outcome():
            if self.board.outcome().winner is None:
                return None
            return self.players[self.board.outcome().winner]

