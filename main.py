# Import necessary classes from modules
from mcts import MCTS
from node import Node
from state import State

# Define the initial state of the game board
initial_board_state = [
    'T', ' ', ' ', ' ', 'T',
    ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ',
    'T', ' ', ' ', ' ', 'T'
]

# Create a State object representing the initial state of the game
state = State(
    board=initial_board_state,         # List representing the game board
    currentPlayer='G',                 # Player currently taking their turn ('G' for goats)
    goats_killed=0,                    # Number of goats killed in the game
    goats_placed=0                     # Number of goats currently placed on the board
)

# Initialize the Monte Carlo Tree Search (MCTS) with a search limit of 1000 iterations
mcts = MCTS(search_limit=1000)

# Perform MCTS search to determine the next move
node = mcts.search(Node(state))

# Retrieve and print the last action taken by the MCTS algorithm
print("Last action chosen by MCTS:", node.last_action)
