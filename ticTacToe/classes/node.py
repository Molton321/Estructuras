import node as Node
"""Aclaracion: Se importa el modulo node simplemente para 
poder darle tipo a los parametros de los metodos
si se quiere eliminar se debe eliminar todos los : Node en los parametros"""

class Node:

    """Constructor del nodo

    Keyword arguments:
        player: str -- El jugador va a ser el que empieza 
        data: list[list] -- El estado inicial del tablero
        father: Node -- El nodo padre
        score: int -- El score de la jugada

    Return: 
        Crea el nodo con sus respectivos atributos
    """

    def __init__(self, player: str, data: list, father : Node = None, score: int = 0):
        self.status = data
        self.score = score
        self.player = player
        self.children = []
        self.father = father
        self.leaf = True
        #TODO faktan atributos

    """Docstring for Getters y Setters de los atributos del nodo
    
    Keyword arguments:
        Getters => No recibe ningun parametro
        Setters =>  data: list[list] -- El nuevo estado del tablero 
                    score: int -- El nuevo score de la jugada
    
    Return: 
        Getters => Retorna el atributo solicitado
        Setters => Cambia el valor del atributo solicitado por el argumento recibido
    """

    def get_Status(self):
        return self.status

    def set_Status(self, data: list):
        self.status = data

    def get_Score(self):
        return self.score

    def set_Score(self, score: int):
        self.score = score

    def get_Children(self):
        return self.children

    """----------------------------------------"""
    
    """Creacion de los hijos del nodo
    
    Keyword arguments:
        father: Node -- El nodo padre
        node: Node -- El nodo a ser agregado
    
    Return:
        Agrega el nodo a la lista de hijos del nodo padre
    """

    def add_Child(self, father: Node, node: Node):
        father.children.append(node)

    """Eliminacion de los hijos del nodo
    
    keyword arguments:
        father: Node -- El nodo padre
        node: Node -- El nodo a ser eliminado
    
    Return:
        Elimina el nodo de la lista de hijos del nodo padre si es que existe
    """
    def remove_Child(self, father: Node, node: Node):
        for node in father.children:
            if node == node:
                father.children.remove(node)
    

    
    def to_dict(self):
        
        return {
            "player": self.player,
            "status": [str(self.status[0]), str(self.status[1]), str(self.status[2])],
            "score": self.score,
            "children": list(map(lambda child: child.to_dict(), self.children))
        }
        
    