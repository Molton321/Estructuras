class Node:
    self = 0

    def __init__(self, newData):
        self.self = newData
        self.left = None
        self.right = None
        self.isLeaf = True
        self.height = 1

    def getData(self):
        return self.self

    def setData(self, Data):
        self.self = Data

    def getSonLeft(self):
        return self.left
    
    def setSonLeft(self, newLeft):
        self.left = newLeft
        self.isLeaf = False
    
    def getSonRight(self):
        return self.right
    
    def setSonRight(self, newRight):
        self.right = newRight
        self.isLeaf = False
    
    def print(self):
        print("[address: " + str(id(self))+" ]")
        print("Data: " + str(self.getData()))
        print("Is leaf: " + str(self.isLeaf))
        if self.left != None:
            print("-Left self: [address: " + str(id(self.left.getData())) +" ]")
            print("Data: " + str(self.left.getData()))
        else:
            print("-Left self: None")
        if self.right != None:
            print("-Right self: [address: " + str(id(self.right.getData())) +" ]")
            print("Data: " + str(self.right.getData()))
        else:
            print("-Right self: None")
        print("---------------------------------------------------")



