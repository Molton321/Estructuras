//import java.util.Scanner;

public class Ejercicios {

    public static void main(String[] args) {
       // System.out.println(CalculoPotencia(3, 7));
        Factorial(68);
    }

    public static long CalculoPotencia(int base, int exponente) {
        int resultado = base;
        for (int i = 1; i < exponente; i++) {
            resultado = resultado * base;
        }
        return resultado;

    }

    // public static long Sum(){

    // return long ;
    // }

    public static void Factorial(int Factorial) {
        System.out.print("El numero " + Factorial +" se puede descomponer en: ");
        while (Factorial != 1) {
            if (Factorial % 2 == 0) {
                Factorial = Factorial / 2;
                System.out.print("2, ");
            } else if (Factorial % 3 == 0) {
                Factorial = Factorial / 3;
                System.out.print("3, ");
            } else if (Factorial % 5 == 0){
                Factorial = Factorial / 5;
                System.out.print("5, ");
            } else if (Factorial % 7 == 0){
                Factorial = Factorial/7;
                System.out.print("7");
            } else if ( Factorial % Factorial == 0 && Factorial % 1 == 0){
                System.out.print(Factorial);
                break;
            }

        }
    }

    
}
