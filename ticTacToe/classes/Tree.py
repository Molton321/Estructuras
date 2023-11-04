"""
Posibles formas de importar 
import node as node
from node import Node
from node import *
"""
import node as node
import json


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
        

    def get_Root(self):
        return self.root

    """Busqueda de un nodo en el arbol
    
    Keyword arguments:
        status: list[list] -- El estado del tablero a buscar
    Return:
        Retorna el nodo encontrado
    """
        
    def search(self, status: list):
        for child in self.root.children:
            if child.status == status:
                return child
            else:
                find = self.search(status)
                if find is not None:
                    return find
                
    """Copiar el estado de un nodo
    Este metodo es para evitar que se modifique el estado del tablero de cualquier
    nodo al crear una copia profunda eliminando las referencias tanto de la lista 
    externa como de la lista interna
    
    keyword arguments:
        status: list[list] -- El estado del tablero a ser copiado
        
    return:
        Retorna el estado del tablero copiado sin referencias a la lista original 
    """
    
    def copy_Status(self, status):
        return list(map(lambda x: x.copy(), status))
    
    """Agregar los hijos a un nodo
    
    Keyword arguments:
        father: Node -- El nodo al que se le van a agregar los hijos
    """
    
    def add_Children(self, father: node):
        children = father.children
        status = self.copy_Status(father.status)
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
                    children.append(child)
                    status = self.copy_Status(father.status)
                elif status[i][j] == "X" or status[i][j] == "O":
                    continue
                    
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    def create_Tree(self, father: node):
        if father.leaf:
            father.leaf = False
            self.add_Children(father)
            if father.children != []:
                for child in father.children:
                    self.create_Tree(child)
        
    """
    Convierte el árbol a un archivo JSON

    Keyword arguments:
        filename: str -- El nombre del archivo JSON

    Return:
        None
    """

    def to_json(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.root.to_dict(), f, indent=4)
    
    
                  

    