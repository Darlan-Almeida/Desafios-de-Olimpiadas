import java.util.*;

public class SelectionSort {
    void ordenar( int [] v){
        for(int i = 0 ; i < v.length ; i++){
            int pos_menor = i;
            for(int j = i+1 ; j < v.length ; j++){
                if(v[j] < v[pos_menor]){
                    pos_menor = j;
                }
            }
            int aux = v[i];
            v[i] = v[pos_menor];
            v[pos_menor] = aux;
            System.out.println(Arrays.toString(v));

        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nums = sc.nextLine();
        String[] nums_v = nums.split(" ");
        
        int[] v = new int[nums_v.length];
        for(int i = 0; i < nums_v.length; i++){
            int numero = Integer.parseInt(nums_v[i]);
            v[i] = numero;
        }

        SelectionSort alg = new SelectionSort();
        alg.ordenar(v);
    }
}

