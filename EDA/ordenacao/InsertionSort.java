public class InsertionSort<T extends Comparable<T>> implements Sorting<T> {
    @Override
    public void sort(T[] elements){
        
        int tam = elements.length;
        
        for(int i = 1; i < tam; i++){
            int j = i;
            while(j > 0 && elements[j].compareTo(elements[j-1]) < 0){
                T aux = elements[j-1];
                elements[j-1] = elements[j];
                elements[j] = aux;
                j--;
            }
        }
    }
}

    

    
    
