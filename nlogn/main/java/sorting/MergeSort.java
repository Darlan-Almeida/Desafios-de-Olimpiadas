 package sorting;
import java.util.*;
public class MergeSort implements SortingStrategy {

    /**
    * Implemente o método abaixo, que recebe dois arrays ordenados em forma crescente
    * e retorna um novo array também ordenado em forma crescente.
    */
    public int[] mergeOrdenadosCrescente(int[] a, int[] b) {
        int tam = a.length + b.length;
        int[] aux = new int[tam];
                
        int i = 0;
        int j = 0;
        int k = 0;

        while(i < a.length && j < b.length){
            if(a[i] <= b[j])
                aux[k++] = a[i++];
            else
                aux[k++] = b[j++];
        }
        
        while(i < a.length){
            aux[k++] = a[i++];
        }

        while(j < b.length){
            aux[k++] = b[j++];
        }


        return aux;
    }
    
    // TODO: implementar
    
    /**
    * Implemente o método abaixo, que recebe dois arrays ordenados em forma decrescente
    * e retorna um novo array ordenado em forma crescente.
    */
    public int[] mergeOrdenadosDecrescente(int[] a, int[] b) {
        int tam = a.length + b.length;

        int[] aux = new int[tam];
        
        int i = a.length - 1;
        int j = b.length - 1;
        int k = 0;

        while(i > 0 && j > 0){
            if(a[i] <= b[j])
                aux[k++] = a[i--];
            else
                aux[k++] = b[j--];
        }


        while(i > 0){
            aux[k++] = a[i--];
        }

        while(j > 0){
            aux[k++] = b[j--];
        }

        return aux;
    }
   
    /**
    * Implemente o método abaixo, que recebe dois arrays: a, ordenado em forma crescente e b, ordenado
    * em forma descrescente. Seu método deve retornar um array ordenado em forma crescente.
    */
    public int[] mergeOrdenadosDistintos(int[] a, int[] b) {
        int tam = a.length + b.length;
        int[] aux = new int[tam];

        int i = 0;
        int j = b.length-1;
        int k = 0;

        while(i < a.length && j > 0){
            if(a[i] < b[j])
                aux[k++] = a[i++];
            else
                aux[k++] = b[j--];
        }

        while(i < a.length){
            aux[k++] = a[i++];
        }

        while(j > 0){
            aux[k++] = b[j--];
        }

        return aux;
    }
   
    /**
    * Implemente a versão clássica do merge sort que vimos em sala de aula. Você pode
    * criar métodos auxiliares se precisar.
    */
    @Override
    public void sort(int[] v, int ini, int fim) {


        if(ini < fim){

            int meio = (ini + fim) / 2;

            sort(v , ini , meio);
            sort(v , meio+1 , fim);

            merge(v, ini, meio ,fim);
        }
    }

    void merge(int[] v , int ini , int meio , int fim){
        int tam = fim - ini + 1;
        int[] aux = new int[tam];

        int i = ini;
        int j = meio+1;
        int k = 0;


        while(i <= meio && j <= fim){
            if(v[i] <= v[j])
                aux[k++] = v[i++];
            else
                aux[k++] = v[j++];
        }

        while(i <= meio){
            aux[k++] = v[i++];
        }

        while(j <= fim){
            aux[k++] = v[j++];
        }
        


        for(int l = 0 ; l < tam ; l++){
            v[ini+l] = aux[l];
        }
    }

}
