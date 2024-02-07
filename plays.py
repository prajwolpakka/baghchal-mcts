import random

def random_play(state):
    """
    Perform a random play from the given state until a terminal state is reached.

    Args:
        state (State): The initial state of the game.

    Returns:
        result: The result of the game after random play.
    """
    current_state = state

    # Continue playing until a terminal state is reached
    while not current_state.isTerminal():
        legal_actions = current_state.getPossibleActions()

        # Check if it's the turn of 'T' player
        if current_state.currentPlayer == 'T':
            # Filter actions that result in jumping positions
            favourable_action = [item for item in legal_actions if item.jumped_pos]

            # Select action randomly based on availability of jumping positions
            if len(favourable_action) == 0:
                action = random.choice(legal_actions)
            elif len(favourable_action) == 1:
                action = favourable_action[0]
            else:
                action = random.choice(favourable_action)     

        # If it's the turn of 'G' player, choose action randomly
        else:
            action = random.choice(legal_actions)

        # Update the current state with the chosen action
        current_state = current_state.takeAction(action)

    # Return the result of the game after random play
    return current_state.get_result()
