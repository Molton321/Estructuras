/**
 * Jeve
 */
public class Jeve {
    public static int LIMITE = 1000000;
    

    public static void main(String[] args) {
        
    }

    static double obtenerPIv1() {
        double s = 0;
        int sign = 1;
        for (int i = 1; i <= LIMITE; i += 2) {
            s += ((1. / i) * sign); // OJO si cambia 1. por 1 falla
            sign *= -1;
        }
        s *= 4;
        return s;
    }

    static double obtenerPIv2() {
        double s = 0;
        for (int i = 1; i <= LIMITE; i += 2) {
            s += ((24. /Math.pow(i,2))); // OJO si cambia 1. por 1 falla
        }
        s = Math.sqrt(s);
        s *= 1/2;
        return s;
    }

    static double obtenerPIv3(){
        // usando la misma logica de v1 y v2 pero ahora el resultado se multiplica por 4 y los numeradores se 
        double s = 0;
        for (int i = 1; i <= LIMITE; i += 2) {
            s += ((1. /Math.pow(i,2))); // OJO si cambia 1. por 1 falla
        }
        
        s = Math.sqrt(s);
        return s;
    }
}