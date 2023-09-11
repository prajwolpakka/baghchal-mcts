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

# current_state = state
# cpu='T'
winner_dict ={'G':0,'T':0}
turn_history = []
goats_placed_history = []
goats_kill_history = []
total_simulation = 2
total_mcts_time = 0
for index in range(total_simulation):
    current_state = state
    print('Simulation:',index/total_simulation * 100,'%')
    turn = 0
    while not current_state.isTerminal():
        # if cpu ==current_state.currentPlayer:
        start_time = time.time()
        mcts = MCTS(search_limit=1000)
        node = mcts.search(Node(current_state))
        current_state = current_state.takeAction(node.last_action)
        end_time = time.time()
        total_mcts_time += (end_time-start_time)
        turn+=1
        # else:
        #     legal_actions = current_state.getPossibleActions()
        #     selected_action = random.choice(legal_actions)
        #     current_state = current_state.takeAction(selected_action)
    print(current_state)
    winner = 'T' if current_state.goats_killed == 5 else 'G'
    winner_dict[winner]+=1
    turn_history.append(turn/2)
    goats_placed_history.append(current_state.goats_placed)
    goats_kill_history.append(current_state.goats_killed)

print('Win is:',winner_dict)
print('Average turns per game:',sum(turn_history)/len(turn_history))
print('Average goats killed per game:',sum(goats_kill_history)/total_simulation)
print('Average goats placed per game:',sum(goats_placed_history)/total_simulation)
print('Average MCTS decision time is:',total_mcts_time/sum(turn_history),'seconds')