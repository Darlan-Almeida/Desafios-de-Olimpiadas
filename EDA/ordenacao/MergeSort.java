import java.util.*;

public class MergeSort{
    
    
    public static void sort(int[] v) {
        mergeSort(v, 0, v.length-1);
    }

    static void mergeSort(int[] v, int ini , int fim){
            
        if(ini < fim){
            int meio = (ini + fim) / 2;

            mergeSort(v , ini , meio);
            mergeSort(v , meio+1 , fim);

            merge(v, ini, meio , fim);

            

        }
    }

    static void merge(int[] v , int ini , int meio, int fim){
        int[] helper = new int[v.length];

        for(int i = ini; i <= fim ; i++){
            helper[i] = v[i];
        }
        System.out.println(Arrays.toString(helper));
        
        int i = ini;
        int j = meio+1;
        int k = ini;
        
        while(i <= meio && j <= fim){

            if(helper[i] <= helper[j])
                v[k++] = helper[i++];
            else
                v[k++] = helper[j++];
                
            
        }

        while(i <= meio)
            v[k++] = helper[i++];
    }

    public static void main(String[] args) {
        int[] v = { 2, 9 , 5 ,4 , 6 ,7 ,3 , 2};

        MergeSort.sort(v);

        System.out.println(Arrays.toString(v));

    }
}
