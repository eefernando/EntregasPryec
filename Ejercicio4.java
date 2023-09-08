import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa la edad de Juan: ");


        int edadAna;
        int edadJuan = scanner.nextInt();
        int edadAlberto;
        int edadMama;


        edadAlberto = 2 * edadJuan / 3;
        edadAna = 4 * edadJuan / 3;
        edadMama = edadAlberto + edadAna + edadJuan;




        System.out.println("La edad de Juan es: " + edadJuan);
        System.out.println("La edad de Alberto es: " + edadAlberto);
        System.out.println("La edad de Ana es: " + edadAna);
        System.out.println("La edad total de la mamá, Juan, Alberto y Ana es: " + edadMama);
    }
}
