import java.util.Arrays;

public class SelectionSort<T extends Comparable<T>> implements Sorting<T>{
    
    @Override
    public  void sort(T[] elements) {

        for(int j = 0 ; j < elements.length; j++){
            int idx_menor = j;
            for(int i = idx_menor ; i < elements.length; i++){
                if(elements[i].compareTo(elements[idx_menor]) < 0){
                    idx_menor = i;
                }
            }
            T aux = elements[j];
            elements[j] = elements[idx_menor];
            elements[idx_menor] = aux;            
        }
    }

}