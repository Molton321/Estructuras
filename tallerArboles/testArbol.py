import arbol as a


def main():
    arbol = a.Tree()
    
    arbol.add(50)
    arbol.add(40)
    arbol.add(60)
    arbol.add(30)
    arbol.add(45)
    arbol.add(53)
    arbol.add(61)
    
    arbol.print()
    
    if arbol.isComplete():
        print("Is complete")
    else:
        print("Is not complete")
        
    if arbol.isFull():
        print("Is full")
    else:
        print("Is not full")
        
    print("inOrder: ")
    arbol.inOrder()
        
    
    
    

if __name__ == '__main__':
    main()