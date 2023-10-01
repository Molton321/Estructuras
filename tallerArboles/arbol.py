import nodeClass as Node

class Tree:
    root = None
     
    def __init__(self):
        self.root = None
    
    def add(self, newData):
        if self.root == None:
            self.root = Node.Node(newData)
            print("Added: " + str(newData) +" at node: " + str(id(self.root)) + " as root")
        else:
            self.addRecursive(self.root, newData)
    
    def addRecursive(self, currentNode, newData):
        self.altura += 1
        if newData < currentNode.getData():
            if currentNode.getSonLeft() == None:
                currentNode.setSonLeft(Node.Node(newData))
                print("Added: " + str(newData) +" at node: " + str(id(currentNode.getSonLeft())))
            else:
                self.addRecursive(currentNode.getSonLeft(), newData)
        
        if newData > currentNode.getData():
            if currentNode.getSonRight() == None:
                currentNode.setSonRight(Node.Node(newData))
                print("Added: " + str(newData) +" at node: " + str(id(currentNode.getSonRight())))
            else:
                self.addRecursive(currentNode.getSonRight(), newData)
    
    def print(self):
        if self.root != None:
            print("---------------------------------------------------")
            print("Tree root: " )
            self.printRecursive(self.root)
        else:
            print("Empty tree")
    
    def printRecursive(self, currentNode):
        currentNode.print()
        if currentNode.getSonLeft() != None:
            self.printRecursive(currentNode.getSonLeft())
        if currentNode.getSonRight() != None:
            self.printRecursive(currentNode.getSonRight())
    
    def isComplete(self):
        print("In function")
        if self.root != None:
            return self.isCompleteRecursive(self.root)
        else:
            return False
    
    def isCompleteRecursive(self, currentNode):
        print("In recursive function")
        if ((currentNode.getSonLeft() == None or currentNode.getSonRight() == None) and currentNode.isLeaf == False):
            return False
        else:
            if currentNode.getSonLeft() != None:
                return self.isCompleteRecursive(currentNode.getSonLeft())
            if currentNode.getSonRight() != None:
                return self.isCompleteRecursive(currentNode.getSonRight())
            return True
            
    def getHeight(self):
        if self.root != None:
            return self.getHeightRecursive(self.root)
        else:
            return 0
    
    # def getHeightRecursive(self, currentNode):
    #     if currentNode.
        
        