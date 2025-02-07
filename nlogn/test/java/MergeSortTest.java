import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import sorting.MergeSort;

public class MergeSortTest {

    MergeSort sorting = new MergeSort(); 
    int[] v;

    @Test
    public void testSort() {
        v = new int[]{8, 1, 78, 45, 3, 2, 103};
        sorting.sort(v, 0, v.length - 1);
        assertArrayEquals(new int[]{1, 2, 3, 8, 45, 78, 103}, v);	

        v = new int[]{2};
        sorting.sort(v, 0, v.length - 1);
        assertArrayEquals(new int[]{2}, v); 

        v = new int[]{1, 2, 3, -4};
        sorting.sort(v, 0, v.length - 1);
        assertArrayEquals(new int[]{-4, 1, 2, 3}, v); 

        v = new int[]{10, 2, 3, 4};
        sorting.sort(v, 0, v.length - 1);
        assertArrayEquals(new int[]{2, 3, 4, 10}, v); 
    }	

}




