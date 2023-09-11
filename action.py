class Action:
    def __init__(self, player, pos, next_pos=None,jumped_pos=None):
        self.player = player
        self.pos = pos
        self.next_pos = next_pos
        self.jumped_pos = jumped_pos

    def __str__(self):
        repr = f""
        repr += f"{self.player}->"
        repr += f"{self.pos}"
        if self.next_pos:
            repr += f"->{self.next_pos}"
        if(self.jumped_pos):
            repr += f"->{self.jumped_pos}"
        return repr

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.pos == other.pos and self.player == other.player and self.next_pos == other.next_pos and self.jumped_pos == other.jumped_pos

    def __hash__(self):
        return hash((self.pos, self.player))