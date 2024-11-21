import java.util.*;

public class InsertionSort {

    void ordenar(int []  v){

        int ini = 0;
        int fim = v.length;

        while( ini < fim - 1){
            for( int i = ini + 1 ; i > 0 ; i--){
                if(v[i] < v[i - 1]){
                    int aux = v[i];
                    v[i] = v[i-1];
                    v[i-1] = aux;
                }
            }
            ini++;
            System.out.println(Arrays.toString(v));
        }

    }

    public static void main(String[] args) {
        int[] v = {0, 90, 1, 3, 70, 100, 2};
        InsertionSort alg = new InsertionSort() ;
        alg.ordenar(v);
     
    }
}
