"""
Posibles formas de importar 
import node as node
from node import Node
from node import *
"""
import node 
import json

"""se presenta un caso de herencia en el que la clase Tree hereda de la clase Node
la herencia se hace al momento de declarar la clase Tree y se le pasa como parametro
el objeto Node que se quiere heredar """
class Tree(node.Node):
    """Constructor de la clase

    Keyword arguments:
        Player: str -- El jugador va a ser el que empieza
        Status: list[list] -- El estado inicial del tablero
    Return: 
        Crea el arbol con el nodo raiz
    """
    
    def __init__(self, player: str = "X", status: list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        super().__init__(player, status)
        self.root = self
        self.node_count = 1
        

    def get_Root(self):
        return self.root

    """Busqueda de un nodo en el arbol
    
    Keyword arguments:
        status: list[list] -- El estado del tablero a buscar
        node: Node -- El nodo desde el cual se va a buscar(root por defecto)
    Return:
        Retorna el nodo encontrado
    """
      
    def search(self, status: list , node: node = None):
        if node is None:
            node = self.root
            
        for child in node.get_Children():
            if child.status == status:
                return child
            else:
                find = self.search(status, child)
                if find is not None:
                    return find            
    
    
    """Agregar los hijos a un nodo
    
    Keyword arguments:
        father: Node -- El nodo al que se le van a agregar los hijos
    """
    
    def add_Children(self, father: node):
        children = father.children
        status = father.copy_Status()
        print(id(status), id(father.status))
        """print(status) """
        for i in range(3):
            for j in range(3):
                if status[i][j] == 0:
                    status[i][j] = father.player
                    if father.player == "X":
                        child = node.Node("O",self.copy_Status(status),father)
                    elif father.player == "O":
                        child = node.Node("X", self.copy_Status(status),father)
                    self.node_count += 1
                    children.append(child)
                    
                    status = father.copy_Status()
                elif status[i][j] == "X" or status[i][j] == "O":
                    continue
                    
    """ Crea el arbol a partir de un nodo
    
    Keyword arguments:
        father: Node -- El nodo desde el cual se va a crear el arbol
    """
    
    def create_Tree(self, father: node):
        if father.leaf and not father.fin:
            father.leaf = False
            self.add_Children(father)
            if father.children != []:
                for child in father.children:
                    self.create_Tree(child) 
        
    """
    Convierte el árbol a un archivo JSON

    Keyword arguments:
        filename: str -- El nombre del archivo JSONs
    """

    def to_json(self, filename: str):
        with open(filename, "w") as json_file:
            json.dump(self.root.to_dict(), json_file, indent=4)
    #with es un manejador de contexto que se encarga de cerrar el archivo
    #open abre el archivo en modo escritura, as es para dar un alias al archivo
    #json.dump convierte el diccionario a un archivo json
    
                  

    