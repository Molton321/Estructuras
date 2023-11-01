class Node:
    def __init__(self, playerzz, data=[[x,o,x],
                                     [0,0,0], 
                                     [0,0,0]], score=0):
        self.status = data
        self.score = score
        self.player = player
        self.children = []  # Initialize with three empty lists

    def get_Status(self):
        return self.status

    def set_Status(self, data):
        self.status = data

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_children(self):
        return self.children

    def new_children(self, player, data):
        self.children.append(Node(player, data))

