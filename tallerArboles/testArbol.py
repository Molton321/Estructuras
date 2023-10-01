import arbol as a
import random

def main():
    arbol = a.Tree()
    
    arbol.add(50)
    arbol.add(40)
    arbol.add(60)
    arbol.add(30)
    arbol.add(45)
    arbol.add(53)
    arbol.add(46)
        
    arbol.print()
    arbol.isComplete()
    print(arbol.isComplete())  

if __name__ == '__main__':
    main()