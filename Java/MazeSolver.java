public class MazeSolver { // 37

    public boolean solve (int [][] maze, int startx, int starty , int endx, int endy) {
        int rows = maze.length; 
        int cols = maze[0].length;
        
        //verificar su esta fuera de los limites o en una celda bloqueada
        if (startx <0 || startx >= cols || starty < 0 || starty >= rows || maze[starty][startx] ==1) {
            return false;
        }
        //verificar si esta en la celda de salida
        if (startx == endx && starty == endy) {
            return true;
        }

        //marcar la celda como visitada
        maze[starty][startx] = 1;
        System.out.println("Marcar la posicion" + starty + "," + startx);
    }
}
