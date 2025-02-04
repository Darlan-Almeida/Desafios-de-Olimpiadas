import java.util.*;


public class Main {

    public static void main(String[] args) {
        Integer [] v = {32 , 1 , 0 , 4 , 2, 1 , 9 , 5};

        Sorting<Integer> sorter = new InsertionSort<>();
        sorter.sort(v);
        System.out.println(Arrays.toString(v));
        
    }
    
}