import csv
from game2dboard import Board


import csv

class Utilities:
    """
    A class that provides utility functions for solving mazes.

    Attributes:
    - maze: a list representing the maze
    - caminos: a list of paths taken to solve the maze
    - valY: a list of y-coordinates of visited cells
    - valX: a list of x-coordinates of visited cells
    """

    maze = []
    caminos = []
    valY = []
    valX = []

    def LoadCsv(self, filename):
        """
        Loads a CSV file containing a maze and returns it as a list.

        Args:
        - filename: a string representing the path to the CSV file

        Returns:
        - A list representing the maze
        """
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            data = list(reader)
            self.Maze = [[int(col) for col in row] for row in data]

        return (self.Maze)

    def solve(self, maze, startX, startY, endX, endY):
        """
        Solves a maze using recursive backtracking.

        Args:
        - maze: a list representing the maze
        - startX: an integer representing the starting x-coordinate
        - startY: an integer representing the starting y-coordinate
        - endX: an integer representing the ending x-coordinate
        - endY: an integer representing the ending y-coordinate

        Returns:
        - True if the maze is solvable, False otherwise
        """
        rows = len(maze)
        cols = len(maze[0])

        # Verificar si estamos fuera de los limites o en una celda bloqueada
        if startX < 0 or startX >= cols or startY < 0 or startY >= rows or maze[startY][startX] == 1:
            return False

        # Verifica si hemos llegado a la salida
        if startX == endX and startY == endY:
            return True

        # Marcar la celda como visitada
        maze[startY][startX] = 1

        print(f"Marcar la posición {startY}, {startX}")

        self.valY.append(startY)
        self.valX.append(startX)

        # Explorar las cuatro direcciones posibles
        if (self.solve(maze, startX+1, startY, endX, endY) or
            self.solve(maze, startX-1, startY, endX, endY) or
            self.solve(maze, startX, startY+1, endX, endY) or
            self.solve(maze, startX, startY-1, endX, endY)):

            return True
        # Si ninguna direccion lleva a la solución, desmarcar la celda
        maze[startY][startX] = 0

        self.valY.pop
        self.valX.pop

        return False
