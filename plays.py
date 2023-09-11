import random


def random_play(state):
    current_state = state
    while not current_state.isTerminal():
        legal_actions = current_state.getPossibleActions()
        if(state.currentPlayer == 'T'):
            favourable_action = [item for item in legal_actions if item.jumped_pos]

            if len(favourable_action) == 0:
                action = random.choice(legal_actions)
            elif len(favourable_action) == 1:
                action = favourable_action[0]
            else:
                action = random.choice(favourable_action)     
            
            current_state = current_state.takeAction(action)
        else:
            selected_action = random.choice(legal_actions)
            current_state = current_state.takeAction(selected_action)
    return current_state.get_result()