import math
import random
from copy import deepcopy

from node import Node
from plays import random_play


class MCTS:
    def __init__(self, search_limit):
        self.search_limit = search_limit

    def search(self, root):
        exploring_factor = 4
        for i in range(self.search_limit):
            if (i + 1) % (self.search_limit // 10) == 0:  # Check if we've reached a 10% increment
                exploring_factor -= 0.25  # Decrease the exploring factor by 0.1
            selected_node = self.select(root,exploring_factor)
            if not selected_node.state.isTerminal():
                expanded_node = self.expand(selected_node)
                reward = random_play(expanded_node.state)
                self.backpropagate(expanded_node, reward)
        return self.get_best_node(root,0)
    
    # select most promising node
    def select(self, node,exploring_factor):
        while not node.state.isTerminal() and len(node.children) == len(node.state.getPossibleActions()):
            node = self.get_best_node(node, exploring_factor)
        return node

    def expand(self, node):
        legal_actions = node.state.getPossibleActions()
        tried_actions = [child.last_action for child in node.children]
        untried_actions = [action for action in legal_actions if action not in tried_actions]

        if (untried_actions):
            selected_action = random.choice(untried_actions)
            new_state = node.state.takeAction(selected_action)
            new_child = Node(new_state,last_action=selected_action, parent=node)
            node.children.append(new_child)
            return new_child

        return random.choice(node.children)

    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, reward):
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
