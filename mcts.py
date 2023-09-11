import math
import random
from copy import deepcopy

from node import Node
from plays import random_play


class MCTS:
    def __init__(self, search_limit):
        self.search_limit = search_limit

    def search(self, root):
        # print(root.state.getPossibleActions())
        exploring_factor = 4
        for i in range(self.search_limit):
            if (i + 1) % (self.search_limit // 10) == 0:  # Check if we've reached a 10% increment
                exploring_factor -= 0.25  # Decrease the exploring factor by 0.1
                # print(f"Step {i + 1}: Exploration Factor = {exploring_factor:.1f}")
                # input()
            selected_node = self.select(root,exploring_factor)
            # print('Selected Node:')
            # repr = ''
            # repr += f"{selected_node.state.board[0]}|{selected_node.state.board[1]}|{selected_node.state.board[2]}|{selected_node.state.board[3]}|{selected_node.state.board[4]}\n"
            # repr += f"{selected_node.state.board[5]}|{selected_node.state.board[6]}|{selected_node.state.board[7]}|{selected_node.state.board[8]}|{selected_node.state.board[9]}\n"
            # repr += f"{selected_node.state.board[10]}|{selected_node.state.board[11]}|{selected_node.state.board[12]}|{selected_node.state.board[13]}|{selected_node.state.board[14]}\n"
            # repr += f"{selected_node.state.board[15]}|{selected_node.state.board[16]}|{selected_node.state.board[17]}|{selected_node.state.board[18]}|{selected_node.state.board[19]}\n"
            # repr += f"{selected_node.state.board[20]}|{selected_node.state.board[21]}|{selected_node.state.board[22]}|{selected_node.state.board[23]}|{selected_node.state.board[24]}\n"
            # print(repr)
            # input()
            if not selected_node.state.isTerminal():
                expanded_node = self.expand(selected_node)
                # print('Expanded node:')
                # print(expanded_node)
                reward = random_play(expanded_node.state)
                # print('Reward',reward)
                # input()
                self.backpropagate(expanded_node, reward)
                # print('_____________Root___________')
                # print(root)
                # input()
                
        # print('_____________Root___________')
        # for child in root.children:
        #     print(child)
        # print(root)
        return self.get_best_node(root,0)
    
    # select most promising node
    def select(self, node,exploring_factor):
        # print('NODE',node.state)
        # input()
        # print('NODE_CHILDREN',node.children)
        # print('Actions:',node.state.getPossibleActions())
        # input()
        while not node.state.isTerminal() and len(node.children) == len(node.state.getPossibleActions()):
            # print(node)
            # print(node.state.isTerminal())
            # print(node.state.isTerminal())
            # input(len(node.children) == len(node.state.getPossibleActions()))
            node = self.get_best_node(node, exploring_factor)
        return node

    def expand(self, node):
        legal_actions = node.state.getPossibleActions()
        tried_actions = [child.last_action for child in node.children]
        untried_actions = [action for action in legal_actions if action not in tried_actions]

        if (untried_actions):
            selected_action = random.choice(untried_actions)
            new_state = node.state.takeAction(selected_action)
            new_child = Node(new_state,last_action=selected_action,name=str(new_state), parent=node)
            node.children.append(new_child)
            return new_child

        return random.choice(node.children)

    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, reward):
        # update nodes's up to root node
        # print(reward)
        simulating_for = 'G' if node.state.currentPlayer == 'T' else 'T'
        multiplier = 1 if simulating_for == reward['winner'] else -1
        while node is not None:
            node.visits += 1
            node.score += multiplier*(reward['win'] - reward['loss'])
            node = node.parent
            multiplier = -multiplier
            
    # select the best node basing on UCB1 formula
    def get_best_node(self, node, exploration_constant):
        best_children = []  # List to store children with the best score
        best_score = float('-inf')

        # Loop over child nodes
        for child in node.children:
            exploitation_term = child.score / (child.visits + 1)
            exploration_term = math.sqrt(math.log2(node.visits + 1) / (child.visits + 1))
            score = exploitation_term + exploration_constant * exploration_term

            if score > best_score:
                best_score = score
                best_children = [child]
            elif score == best_score:
                best_children.append(child)

        return random.choice(best_children)
