import chess
from mcts_simple import *
import tensorflow as tf



class PUCTNode(Node):

    def __init__(self, prev_state=None, state=None, action=None, player=None, nn = None, c=1.0):

        super().__init__(prev_state, state, action, player)

        self.nn = nn
        self.c = c


    def proba(self, parent):
        if self.nn is None:
            raise ValueError
        else:
            # TODO
            return self.nn.predict([parent.state])[0]

    def add_child_node(self, action, node):
        child_states = [child.state for child in self.children]
        if node.state not in child_states:
            self.children.append(node)
            node.transposed_from[self.state] = action
        else:
            node = self.children[child_states.index(node.state)]
        return node


    def add_child(self, state = None, action = None, player = None):
        child_states = 
