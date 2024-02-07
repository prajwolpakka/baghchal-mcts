import math
from copy import deepcopy
from action import Action
from movement_dict import MOVEMENTS

class State:
    """
    Represents the state of the game.

    Attributes:
        board (list): The game board represented as a list of characters.
        currentPlayer (str): The player currently taking a turn ('G' for goats, 'T' for tigers).
        goats_killed (int): The number of goats killed in the game.
        goats_placed (int): The number of goats placed on the board.
        turn (int): The current turn number.
        kill_history (list): History of turns in which goats were killed.
    """

    def __init__(self, init_board, currentPlayer, goats_killed, goats_placed):
        """
        Initializes a State object with the given parameters.

        Args:
            init_board (list): The initial state of the game board.
            currentPlayer (str): The player currently taking a turn ('G' for goats, 'T' for tigers).
            goats_killed (int): The number of goats killed in the game.
            goats_placed (int): The number of goats placed on the board.
        """
        self.board = init_board
        self.currentPlayer = currentPlayer
        self.goats_killed = goats_killed
        self.goats_placed = goats_placed
        self.turn = 1
        self.kill_history = []

    def jump_position(self, tiger_idx, goat_idx):
        """
        Calculates the position of the leap during a tiger's jump action.

        Args:
            tiger_idx (int): The index of the tiger's current position.
            goat_idx (int): The index of the goat's current position.

        Returns:
            int: The index of the leap position if valid, None otherwise.
        """
        # Calculate the row and column indices of the tiger and goat
        tiger_row, tiger_col = tiger_idx // 5, tiger_idx % 5
        goat_row, goat_col = goat_idx // 5, goat_idx % 5

        # Calculate the row and column indices of the leap position
        leap_row = 2 * goat_row - tiger_row
        leap_col = 2 * goat_col - tiger_col

        # Calculate the new index based on the leap position
        leap_idx = leap_row * 5 + leap_col

        # Check if the leap position is valid
        if 0 <= leap_row < 5 and 0 <= leap_col < 5 and self.board[leap_idx] == ' ':
            return leap_idx
        else:
            return None  # Invalid leap, return None

    def getPossibleActions(self):
        """
        Generates all possible actions for the current player.

        Returns:
            list: A list of Action objects representing possible actions.
        """
        possibleActions = []

        if self.currentPlayer == 'G':
            if self.goats_placed < 20:
                # Goats placing phase
                possibleActions = [
                    Action(player=self.currentPlayer, pos=idx)
                    for idx, data in enumerate(self.board) if data == " "
                ]
            else:
                # Goats moving phase
                possibleActions = [
                    Action(player=self.currentPlayer, pos=idx, next_pos=next_pos)
                    for idx, data in enumerate(self.board) if data == 'G'
                    for next_pos in MOVEMENTS[idx] if self.board[next_pos] == ' '
                ]

        else:  # For tiger's turn
            for pos, data in enumerate(self.board):
                if data == 'T':
                    for adj_idx in MOVEMENTS[pos]:
                        adj_data = self.board[adj_idx]
                        if adj_data == ' ':
                            possibleActions.append(Action(player=self.currentPlayer, pos=pos, next_pos=adj_idx))
                        elif adj_data == 'G':
                            next_idx = self.jump_position(pos, adj_idx)
                            if next_idx:
                                possibleActions.append(Action(player=self.currentPlayer, pos=pos, next_pos=next_idx, jumped_pos=adj_idx))

        return possibleActions

    def takeAction(self, action):
        """
        Applies the given action to the current state and returns the new state.

        Args:
            action (Action): The action to be applied.

        Returns:
            State: The new state after applying the action.
        """
        newState = deepcopy(self)  # Creates a clone of the current state

        if self.currentPlayer == 'G':
            # Goats Placing Phase
            if self.goats_placed < 20:
                newState.board[action.pos] = 'G'
                newState.goats_placed += 1
            
            # Goat Moving Phase
            else:
                newState.board[action.pos] = ' '
                newState.board[action.next_pos] = 'G'

            newState.currentPlayer = 'T'

        else:
            # Tiger's turn: handle movement or capturing
            newState.board[action.pos] = ' '
            newState.board[action.next_pos] = 'T'
            if action.jumped_pos:
                newState.goats_killed += 1
                newState.kill_history.append(self.turn)
                newState.board[action.jumped_pos] = ' '
            
            newState.turn += 1
            newState.currentPlayer = 'G'

        return newState

    def isTerminal(self):
        """
        Checks if the current state is a terminal state.

        Returns:
            bool: True if the state is terminal, False otherwise.
        """
        return True if self.goats_killed >= 5 or len(self.getPossibleActions()) == 0 else False

    def zmf(self, x, a=2, b=8):
        """
        Computes the Z-shaped membership function.

        Args:
            x (float): The input value.
            a (float): Lower bound of the function (default 2).
            b (float): Upper bound of the function (default 8).

        Returns:
            float: The output value of the function.
        """
        if x < a:
            return 1.0
        elif a <= x <= (a + b) / 2:
            return 1 - 2 * ((x - a) / (b - a)) ** 2
        elif (a + b) / 2 < x <= b:
            return 2 * ((x - b) / (b - a)) ** 2
        else:
            return 0.0

    def get_result(self):
        """
        Computes the result of the game based on the current state.

        Returns:
            dict: A dictionary containing the result of the game.
        """
        weight = sum([self.zmf(item) for item in self.kill_history]) * 10
        winner = 'G' if self.currentPlayer == 'T' else 'T'

        if winner == 'G':
            return {'loss': self.goats_killed + self.turn * 0.1 + weight, 'win': 15, 'winner': 'G'}
        else:
            return {'loss': self.goats_placed + self.turn * 0.1, 'win': 15 + weight, 'winner': 'T'}

    def __str__(self):
        """
        Returns a string representation of the state.

        Returns:
            str: A string representing the state.
        """
        repr = ""
        repr += f"Killed:{self.goats_killed}, "
        repr += f"Placed:{self.goats_placed}, "
        repr += f"Turn:{self.currentPlayer}\n" 
        repr += f"{self.board[0]}|{self.board[1]}|{self.board[2]}|{self.board[3]}|{self.board[4]}\n"
        repr += f"{self.board[5]}|{self.board[6]}|{self.board[7]}|{self.board[8]}|{self.board[9]}\n"
        repr += f"{self.board[10]}|{self.board[11]}|{self.board[12]}|{self.board[13]}|{self.board[14]}\n"
        repr += f"{self.board[15]}|{self.board[16]}|{self.board[17]}|{self.board[18]}|{self.board[19]}\n"
        repr += f"{self.board[20]}|{self.board[21]}|{self.board[22]}|{self.board[23]}|{self.board[24]}\n"
        return repr
