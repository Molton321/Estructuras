/**
 * Jeve
 */
public class Jeve {
    public static int LIMITE = 1000000;

    public static void main(String[] args) {
        // obtenerPIv3();
        System.out.println(obtenerPIv3());
        System.out.println(obtenerCociente(13, 3));
        System.out.println(fx(0.84));

    }

    // 35
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
            s += ((24. / Math.pow(i, 2))); // OJO si cambia 1. por 1 falla
        }
        s = Math.sqrt(s);
        s *= 1 / 2;
        return s;
    }

    static double obtenerPIv3() {
        // usando la misma logica de v1 y v2 pero ahora el resultado se multiplica por 4
        // y los numeradores se
        double s = 1., i = 4;
        int sign = 1;

        while (i <= LIMITE) {

            s *= ((i / (i + sign)) * ((i / (i - sign))));
            i += 2;

        }
        System.out.println(s);
        s *= (4. * (2. / 3.));
        return s;
    }

    // 36

    /*
     * static void divisionEntera() {
     * int dividendo = Keyboard.readInt("Dividendo: ");
     * int divisor = Keyboard.readInt("Divisor: ");
     * String resultado = obtenerCociente(dividendo, divisor);
     * System.out.println(resultado);
     * Keyboard.readString("Pulse Intro para volver al menú...");
     * }
     */

    static String obtenerCociente(int dividendo, int divisor) {
        int cociente = 0;
        int resto = dividendo;
        String resultado = "";

        while (resto >= divisor) {
            resto -= divisor;
            cociente++;

        }
        resto = dividendo;

        resultado = dividendo + " / " + divisor + " = " + cociente + " y sobra " + resto;
        return resultado;

    }

    static double fx(double x) {
        if (x >= 20) {
            return ((obtenerPIv1() / 2.) + (4 * x));
        } else if (x >= 0 && x < 20) {
            return (Math.pow(x, 3) - 1 / (2 * x));
        } else {
            return (Math.pow(x, 2) - Math.pow(x, 3));
        }
    }

}