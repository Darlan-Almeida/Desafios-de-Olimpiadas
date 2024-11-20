import java.util.*;

public class BuscaLinearRecursiva {

    public int buscar(int[] v , int ini , int fim , int elemento){
        if(v[ini] == elemento){
            return ini;
        }
        if(ini == fim){
            return -1;
        }
        return buscar( v , ini+1 , fim , elemento);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nums = sc.nextLine();
        int elementoBuscar = sc.nextInt();
        String[] nums_v = nums.split(" ");
        
        int[] v = new int[nums_v.length];
        for(int i = 0; i < nums_v.length; i++){
            int numero = Integer.parseInt(nums_v[i]);
            v[i] = numero;
        }

        BuscaLinearRecursiva lin = new BuscaLinearRecursiva();
        System.out.println(lin.buscar(v , 0 , v.length-1 , elementoBuscar));
    }
}
