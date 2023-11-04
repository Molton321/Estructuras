import Tree 
import node as node


def main():
  arbol = Tree.Tree()
  arbol.add_Children(arbol.root)
  for child in arbol.root.children:
    arbol.add_Children(child)
  
  print(arbol.node_count)

  #arbol.create_Tree(arbol.root)
  
  arbol.to_json("arbol1.json")
 
  #deberia soltar un error





if __name__ == "__main__":
    main()
