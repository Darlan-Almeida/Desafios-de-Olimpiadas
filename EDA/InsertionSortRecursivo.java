import java.util.*;

public class InsertionSortRecursivo {
    int[] ordenar(int [] v , int ini , int fim){
        
        if(ini == fim - 1){
            return v;
        }

        for( int i = ini + 1 ; i > 0 ; i--){
            if(v[i] < v[i-1]){
                int aux = v[i];
                v[i] = v[i-1];
                v[i-1] = aux;
            }

        }
        return ordenar(v , ini + 1 , v.length);
    }
    public static void main(String[] args) {
        int[] v = {0, 90, 1, 3, 70, 100, 2};
        InsertionSortRecursivo alg = new InsertionSortRecursivo() ;
        int ini = 0;
        int fim = v.length;
        alg.ordenar(v , ini , fim);
        System.out.println(Arrays.toString(v));
    }
}
