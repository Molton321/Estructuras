import Tree 
import node as node


def main():
  arbol = Tree.Tree()
  arbol.create_Tree(arbol.root)
  
  arbol.to_json("arbol1.json")
 
  #deberia soltar un error





if __name__ == "__main__":
    main()
