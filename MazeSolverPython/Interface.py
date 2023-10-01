from game2dboard import Board
import Utilities
import threading

block = "block.png"


utils = Utilities()
maze = utils.LoadCsv('MazeSolverPython\DataCSV\Lab1.csv')

b = Board(len(maze), len(maze[0]))
b.title = "Lab 1"
b.cell_size = "60"
b.cell_color = "white"
b.grid_color = "black"

for row in range(len(maze)):
    for col in range(len(maze[row])):

        if maze[row][col] == 1:
            b[row][col] = block
            b.start_timer(20)

b.show()
