import node as node

class Tree:
    def __init__(self, root = node.Node()):
        self.root = root

    def getNode(self, node, index):
        return node.getChildren()[index]
    
    def newNode(self, data, score):
        return node.Node(data, score)
    