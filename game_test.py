import random
import time
from mcts import MCTS
from node import Node
from state import State

# Initialize the initial state of the game board
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

# Specify the CPU player
cpu = 'G'

# Initialize variables for tracking game statistics
winner_dict = {'G': 0, 'T': 0}
turn_history = []
goats_placed_history = []
goats_kill_history = []
total_simulation = 1000
total_mcts_time = 0

# Perform simulations
for index in range(total_simulation):
    # Reset the state of the game for each simulation
    current_state = state
    print('Simulation:', index/total_simulation * 100, '%')
    turn = 0

    # Play the game until a terminal state is reached
    while not current_state.isTerminal():
        if cpu == current_state.currentPlayer:
            # CPU's turn: use MCTS to make the decision
            start_time = time.time()
            mcts = MCTS(search_limit=1000)
            node = mcts.search(Node(current_state))
            current_state = current_state.takeAction(node.last_action)
            end_time = time.time()
            total_mcts_time += (end_time - start_time)
            turn += 1
        else:
            # Opponent's turn: choose a random action
            legal_actions = current_state.getPossibleActions()
            selected_action = random.choice(legal_actions)
            current_state = current_state.takeAction(selected_action)

    # Determine the winner of the game
    winner = 'T' if current_state.goats_killed == 5 else 'G'
    winner_dict[winner] += 1
    turn_history.append(turn)
    goats_placed_history.append(current_state.goats_placed)
    goats_kill_history.append(current_state.goats_killed)

# Print game statistics
print('Win % for CPU', cpu, 'is:', winner_dict[cpu]/total_simulation * 100, '%')
print('Average turns per game:', sum(turn_history)/len(turn_history))
print('Average goats killed per game:', sum(goats_kill_history)/total_simulation)
print('Average goats placed per game:', sum(goats_placed_history)/total_simulation)
print('Average MCTS decision time for', cpu, 'is:', total_mcts_time/sum(turn_history), 'seconds')
