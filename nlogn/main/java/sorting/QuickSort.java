package sorting;

public class QuickSort implements SortingStrategy {

  
    /*
       A mediana de uma sequência de tamanho ímpar é o valor que divide uma sequência ao meio, isto é, 
       metado dos valores são menores que ela, enquanto metade são maiores. Implemente o método abaixo
       que recebe uma sequência de tamanho ímpar e retorna a mediana dessa sequência.
    */
    public int mediana(int[] v) {
        sort(v, 0, v.length-1);
        return v[(v.length - 1)/2];
    }

    /**
    * Implemente a versão do quick sort usando o particionamento Hoare, que está descrito
    * neste material: https://joaoarthurbm.github.io/eda/posts/particionamento-hoare/
    */
    public void sort(int[] v, int ini, int fim) {
        
        if(ini < fim){

            int pivo = particiona(v , ini , fim);

            sort(v , ini , pivo-1);
            sort(v, pivo+1 ,fim);
        }
    }

    int particiona(int[] v , int ini , int fim){

        int pivo = v[ini];
        
        int i = ini+1;
        int j = fim;

        while( i <= j){
            while(pivo <= v[i]){
                i++;
            }
    
            while(pivo >= v[j]){
                j--;
            }
            
            int aux = v[i];
            v[i] = v[j];
            v[j] = aux;
        }

        int aux = v[ini];
        v[ini] = v[j];
        v[j] = aux;

        return j;
    }


    /**
    * Nós discutimos em sala de aula que uma tentativa para melhorar a escolha do pivot é
    * decidir usar o valores mediano (não média, cuidado) entre o primeiro elemento do array,
    * o elemento central e o último.

    * Implemente o método abaixo que retorna o valor que seria escolhido como pivot seguindo
    * a abordagem acima.
    * 
    * Interprete os testes para saber qual valor usar como elemento central para calcular a mediana de três.
    */
    public int medianaDeTres(int[] v) {
        return -1;
    }

}
