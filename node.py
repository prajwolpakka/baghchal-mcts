class Node:
    """
    Represents a node in the search tree for Monte Carlo Tree Search (MCTS).

    Attributes:
        state (State): The state of the game associated with this node.
        parent (Node): The parent node in the search tree.
        last_action: The last action taken to reach this node.
        children (list): The list of child nodes.
        visits (int): The number of times this node has been visited.
        score (float): The cumulative score associated with this node.
    """

    def __init__(self, state, last_action=None, parent=None):
        """
        Initializes a Node object with the given state, last action, and parent node.

        Args:
            state (State): The state of the game associated with this node.
            last_action: The last action taken to reach this node (default None).
            parent (Node): The parent node in the search tree (default None).
        """
        self.state = state
        self.parent = parent
        self.last_action = last_action
        self.children = []
        self.visits = 0
        self.score = 0
