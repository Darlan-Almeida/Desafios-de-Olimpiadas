public class Fibonacci {

    public int coelhos(int n){
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }

        return coelhos(n-1) + coelhos(n-2);
    }
    public static void main(String[] args) {
        Fibonacci alg = new Fibonacci();
        System.out.println(alg.coelhos(10));
    }
    
}