import java.util.*;
class PrimeiroNegativo {
    public String buscar(String sequencia){
            String[] sequenciaArray = sequencia.split( " ");
            if( sequenciaArray.length == 1){
                    int num = Integer.parseInt(sequenciaArray[0]);
                    if(num < 0){
                            return sequencia;
                    }else{
                            return "-";
                    }
            }

            int numComparar = Integer.parseInt(sequenciaArray[0]);

            if (numComparar < 0){
                    return sequenciaArray[0];
            }

            String novaSequencia = String.join(" " , java.util.Arrays.copyOfRange( sequenciaArray, 1 , sequenciaArray.length));

            return buscar(novaSequencia);
    }
    public static void main(String[] args){
            String seq = "5 7 -8 9 -4 2 3";
            PrimeiroNegativo pn = new PrimeiroNegativo();
            System.out.println(pn.buscar(seq));
    }
}