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
    # print('Simulating For', simulation_for,'End of Simulation:',current_state)
    # repr = ''
    # repr += f"{current_state.board[0]}|{current_state.board[1]}|{current_state.board[2]}|{current_state.board[3]}|{current_state.board[4]}\n"
    # repr += f"{current_state.board[5]}|{current_state.board[6]}|{current_state.board[7]}|{current_state.board[8]}|{current_state.board[9]}\n"
    # repr += f"{current_state.board[10]}|{current_state.board[11]}|{current_state.board[12]}|{current_state.board[13]}|{current_state.board[14]}\n"
    # repr += f"{current_state.board[15]}|{current_state.board[16]}|{current_state.board[17]}|{current_state.board[18]}|{current_state.board[19]}\n"
    # repr += f"{current_state.board[20]}|{current_state.board[21]}|{current_state.board[22]}|{current_state.board[23]}|{current_state.board[24]}\n"
    # print(repr)
    # print('Reward',current_state.get_result(simulation_for))
    return current_state.get_result()


    # # Game Over Already
    # if (len(state.getPossibleActions()) == 0):
    #     return 5
    
    # # The winner should be the one who performed a move
    # simulating_for = 'G' if state.currentPlayer == 'T' else 'T'
    # win_reward = 0.75
    # decay_factor = 0
    # play_reward = 0

    # # until game is over
    # while not state.isTerminal():
    #     decay_factor += 1
    #     all_actions = state.getPossibleActions()
        
    #     if(state.currentPlayer == 'T'):
    #         favourable_action = [item for item in all_actions if item.jumped_pos]

    #         if len(favourable_action) == 0:
    #             action = random.choice(all_actions)
    #         elif len(favourable_action) == 1:
    #             action = favourable_action[0]
    #         else:
    #             action = random.choice(favourable_action)     
            
    #         goats_killed = state.goats_killed
    #         state = state.takeAction(action)
    #         updated_goats_killed = state.goats_killed
    #         is_goat_killed = updated_goats_killed - goats_killed
            
    #         if(simulating_for == 'T'):
    #             if(is_goat_killed): play_reward+=1/decay_factor
    #         else:
    #             if(is_goat_killed): play_reward-=1/decay_factor

    #     else:
    #         action = random.choice(all_actions)     
    #         state = state.takeAction(action)
            
    # # the one who performed last move
    # # print('Winner:',action.player,state)
    # # input()
    # if(action):
    #     last_player = action.player
    # else:
    #     raise Exception(state.currentPlayer,simulating_for)

    # if simulating_for == last_player:
    #     return win_reward+play_reward
    # else:
    #     return play_reward