import nodeClass as Node


class Tree:
    root = None
    height = 0
    isFull = True
    isComplete = True

    def __init__(self):
        self.root = None
        self.height = 0

    def getHeight(self):
        return self.height

    def add(self, newData):
        if self.root == None:
            self.root = Node.Node(newData, 1)
            print("Added: " + str(newData) + " at node: " +
                  str(id(self.root)) + " as root")
        else:
            self.addRecursive(self.root, newData, 1)

    def addRecursive(self, currentNode, newData, height):
        if self.height < height:
            self.height = height

        if newData < currentNode.getData():
            if currentNode.getSonLeft() == None:
                currentNode.setSonLeft(Node.Node(newData, height))
                print("Added: " + str(newData) + " at node: " +
                      str(id(currentNode.getSonLeft())) + " and " + str(self.height))
            else:
                self.addRecursive(currentNode.getSonLeft(),
                                  newData, height + 1)

        if newData > currentNode.getData():
            if currentNode.getSonRight() == None:
                currentNode.setSonRight(Node.Node(newData, height))
                print("Added: " + str(newData) + " at node: " +
                      str(id(currentNode.getSonRight())) + " and " + str(self.height))

            else:
                self.addRecursive(currentNode.getSonRight(),
                                  newData, height + 1)

    def print(self):
        if self.root != None:
            print("---------------------------------------------------")
            print("Tree root: ")
            self.printRecursive(self.root)
        else:
            print("Empty tree")

    def printRecursive(self, currentNode):
        currentNode.printo()
        if currentNode.getSonLeft() != None:
            self.printRecursive(currentNode.getSonLeft())
        if currentNode.getSonRight() != None:
            self.printRecursive(currentNode.getSonRight())
            


# problema 1

    def isComplete(self):
        if self.root != None:
            return self.isCompleteRecursive(self.root)
        else:
            return False

    def isCompleteRecursive(self, currentNode):
        if ((currentNode.getSonLeft() == None or currentNode.getSonRight() == None) and currentNode.height != self.height):
            self.isComplete = False
        else:
            if currentNode.getSonLeft() != None:
                self.isCompleteRecursive(currentNode.getSonLeft())
            if currentNode.getSonRight() != None:
                self.isCompleteRecursive(currentNode.getSonRight())
  
        return self.isComplete
    
# Problema 2

    def isFull(self):
        if self.root != None:
            return self.isFullRecursive(self.root)

    def isFullRecursive(self, currentNode):
        if ((currentNode.getSonLeft() == None or currentNode.getSonRight() == None) and currentNode.isLeaf == False):
            self.isFull = False
        else:
            if currentNode.getSonLeft() != None:
                self.isFullRecursive(currentNode.getSonLeft())
            if currentNode.getSonRight() != None:
                self.isFullRecursive(currentNode.getSonRight())
        
        return self.isFull

### Recorridos del arbol
# Problema 3
#nodo - izquierda - derecha
    def preOrder(self):
        if self.root != None:
            print("---------------------------------------------------")
            print("Tree root: ")
            self.preOrderRecursive(self.root)
        else:
            print("Empty tree")
    
    def PreOrderRecursive(self, currentNode):
        currentNode.printo()
        if currentNode.getSonLeft() != None:
            self.PreorderRecursive(currentNode.getSonLeft())
        if currentNode.getSonRight() != None:
            self.PreorderRecursive(currentNode.getSonRight())
    
# Problema 4
#izquierda - nodo - derecha
    def inOrder(self,):
        if self.root != None:
            self.inOrderRecursive(self.root)
 

### Busqueda de un nodo

    def search(self,data):
        if self.root != None:
            return self.searchRecursive(self.root,data)
        else:
            return False
    
    def searchRecursive(self, currentNode, data):
        if currentNode.getData() == data:
            return True
        