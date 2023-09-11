import math


class Node:
    def __init__(self, state, last_action=None, name='root', parent=None):
        self.state = state
        self.parent = parent
        self.last_action = last_action  # Store the last action
        self.children = []
        self.visits = 0
        self.score = 0

    def __str__(self, depth=0):
        indent = "         " * depth
        repr = f""
        # repr += f"{indent}isTerminal:{self.state.isTerminal()}, "
        repr += f"{indent}lastAction:{self.last_action}, "
        repr += f"Visits:{self.visits}, "
        repr += f"Score:{self.score:.2f}, "
        if(self.last_action):
            exploitation_term = self.score / (self.visits + 1)
            exploration_term = math.sqrt(math.log2(self.parent.visits + 1) / (self.visits + 1))
            score = exploitation_term + math.sqrt(2) * exploration_term
            repr+= f"UCB:{score:.2f}"
        # repr+='\n'
        # repr += f"{indent}State: {self.state}"
        # repr += f"{indent}{self.state.board[0]}|{self.state.board[1]}|{self.state.board[2]}|{self.state.board[3]}|{self.state.board[4]}\n"
        # repr += f"{indent}{self.state.board[5]}|{self.state.board[6]}|{self.state.board[7]}|{self.state.board[8]}|{self.state.board[9]}\n"
        # repr += f"{indent}{self.state.board[10]}|{self.state.board[11]}|{self.state.board[12]}|{self.state.board[13]}|{self.state.board[14]}\n"
        # repr += f"{indent}{self.state.board[15]}|{self.state.board[16]}|{self.state.board[17]}|{self.state.board[18]}|{self.state.board[19]}\n"
        # repr += f"{indent}{self.state.board[20]}|{self.state.board[21]}|{self.state.board[22]}|{self.state.board[23]}|{self.state.board[24]}\n"
        # repr+='\n'



        # if self.children:
        #     repr += f"{indent}Children:\n"
        #     for child in self.children:
        #         repr += child.__str__(depth + 1)
        # repr += f""
        return repr

    def __repr__(self):
        return str(self)
        
    def __eq__(self, other):
        return self.__class__ == other.__class__ 
