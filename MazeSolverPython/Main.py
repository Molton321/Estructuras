from Utilities import Utilities
from game2dboard import Board
import time


class Main:
    def main():
        """
        This program loads a maze from a CSV file, solves it using the Utilities class, and displays the solution on a board.
        """
        visited, block = "body.png", "block.png"

        # se crean los objetos Utils y utilities para realizar el proceso con clases
        utils = Utilities()

        # De la clase utilities se toma la funcion que convierte el archivo Csv a una matriz de 0 y 1 que es el laberinto
        maze = utils.LoadCsv('MazeSolverPython\DataCSV\Lab1.csv')
        b = Board(len(maze), len(maze[0]))
        b.title = "Lab 1"
        b.cell_size = "60"
        b.cell_color = "white"
        b.grid_color = "black"

        # Se le pide al objeto utils llamar a la funcion solve que soluciona el laberinto y dependiendo de esta desicion
        # se sabe si el laberinto tiene solucion o no
        start = time.time()
        
        for row in range(len(maze)):
                for col in range(len(maze[row])):
                    print(row, col)
                    if maze[row][col] == 1:
                        b[row][col] = block
                    
        if utils.solve(maze, 0, 1, 9, 8):
            print("Se encontro una solución")

            
        else:
            print("No se encontro una solución")

        end = time.time()
        b.show()
    
        print(end - start)



if __name__ == '__main__':
    Main.main()
