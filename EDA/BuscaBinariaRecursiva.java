import java.util.Scanner;

public class BuscaBinariaRecursiva {
    
    public int buscar( int[] v, int ini , int fim, int elemento){
        
        int meio = (ini + fim) / 2;
        
        
        if(v[meio] == elemento){
            return meio;
        }
        System.out.println(meio);

        if(ini == fim){
            return -1;
        }

        if(v[meio] < elemento){
            return buscar(v, meio+1, fim, elemento);
        }

        return buscar(v, ini, meio-1, elemento);
        
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

        BuscaBinariaRecursiva lin = new BuscaBinariaRecursiva();
        System.out.println(lin.buscar(v , 0 , v.length-1 , elementoBuscar));
    }
}

