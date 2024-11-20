import java.util.*;
public class PotenciaRecursiva {

    public int exponeciar(int base , int expoente){
        if(expoente == 0){
            return 1;
        }
        return base * exponeciar(base, expoente-1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int base = sc.nextInt();
        int expoente = sc.nextInt();
        PotenciaRecursiva alg = new PotenciaRecursiva();
        System.out.println(alg.exponeciar(base, expoente));
    }
}
