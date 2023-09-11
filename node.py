import math


class Node:
    def __init__(self, state, last_action=None, parent=None):
        self.state = state
        self.parent = parent
        self.last_action = last_action
        self.children = []
        self.visits = 0
        self.score = 0