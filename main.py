import random
import time

from mcts import MCTS
from node import Node
from state import State

state = State(
    [
        'T', ' ', ' ', ' ', 'T',
        ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ',
        'T', ' ', ' ', ' ', 'T'
    ],
    currentPlayer='G',
    goats_killed=0,
    goats_placed=0
)

mcts = MCTS(search_limit=1000)
node = mcts.search(Node(state))
print(node.last_action)