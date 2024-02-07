class Action:
    """
    Represents an action in the game.

    Attributes:
        player (str): The player making the action ('G' for goats, 'T' for tigers).
        pos (int): The current position of the piece making the action.
        next_pos (int): The next position of the piece after making the action.
        jumped_pos (int): The position of the jumped piece if the action involves a jump.
    """

    def __init__(self, player, pos, next_pos=None, jumped_pos=None):
        """
        Initializes an Action object with the given parameters.

        Args:
            player (str): The player making the action ('G' for goats, 'T' for tigers).
            pos (int): The current position of the piece making the action.
            next_pos (int): The next position of the piece after making the action (default None).
            jumped_pos (int): The position of the jumped piece if the action involves a jump (default None).
        """
        self.player = player
        self.pos = pos
        self.next_pos = next_pos
        self.jumped_pos = jumped_pos

    def __str__(self):
        """
        Returns a string representation of the action.

        Returns:
            str: A string representing the action.
        """
        repr = f"{self.player}->"
        repr += f"{self.pos}"
        if self.next_pos:
            repr += f"->{self.next_pos}"
        if self.jumped_pos:
            repr += f"->{self.jumped_pos}"
        return repr

    def __repr__(self):
        """
        Returns a string representation of the action (same as __str__).

        Returns:
            str: A string representing the action.
        """
        return str(self)

    def __eq__(self, other):
        """
        Checks if two Action objects are equal.

        Args:
            other (Action): Another Action object to compare with.

        Returns:
            bool: True if the two Action objects are equal, False otherwise.
        """
        return (self.__class__ == other.__class__ and 
                self.pos == other.pos and 
                self.player == other.player and 
                self.next_pos == other.next_pos and 
                self.jumped_pos == other.jumped_pos)

    def __hash__(self):
        """
        Computes the hash value of the Action object.

        Returns:
            int: The hash value of the Action object.
        """
        return hash((self.pos, self.player))
