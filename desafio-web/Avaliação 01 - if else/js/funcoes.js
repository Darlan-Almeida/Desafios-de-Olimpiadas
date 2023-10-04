
// Função para resolução da QUESTÃO 01 
function q_01(){

    let nr_01 = parseInt(document.getElementById('q1_nr_01').value);
    let nr_02 = parseInt(document.getElementById('q1_nr_02').value);
    let nr_03 = parseInt(document.getElementById('q1_nr_03').value);

    if(nr_01 < nr_02 && nr_01 < nr_03 && nr_02 < nr_03){
        alert("Resultado da questão 01 - Números: " + 
        nr_03 + ' : ' + 
        nr_02 + ' : ' + 
        nr_01
        );
    }else if (nr_01 < nr_02 && nr_01 < nr_03 && nr_02 > nr_03){
        alert("Resultado da questão 01 - Números: " + 
        nr_02 + ' : ' + 
        nr_03 + ' : ' + 
        nr_01
        );

    }else if (nr_01 < nr_02 && nr_01 > nr_03 && nr_02 > nr_03){
        alert("Resultado da questão 01 - Números: " + 
        nr_02 + ' : ' + 
        nr_01 + ' : ' + 
        nr_03
        );

    }else if(nr_01 > nr_02 && nr_01 > nr_03 && nr_02 < nr_03){
        alert("Resultado da questão 01 - Números: " + 
        nr_01 + ' : ' + 
        nr_03 + ' : ' + 
        nr_02
        );

    }else if(nr_01 > nr_02 && nr_01 < nr_03 && nr_03 > nr_02){
        alert("Resultado da questão 01 - Números: " + 
        nr_03 + ' : ' + 
        nr_02 + ' : ' + 
        nr_01
        );

    }
    else{
        alert("Resultado da questão 01 - Números: " + 
        nr_01 + ' : ' + 
        nr_02 + ' : ' + 
        nr_03
        );

    }


}



// Função para resolução da QUESTÃO 02
function q_02(){
    
    let nr_01 = parseInt(document.getElementById('q2_nr_01').value);
    let nr_02 = parseInt(document.getElementById('q2_nr_02').value);
    let nr_03 = parseInt(document.getElementById('q2_nr_03').value);
    let nr_04 = parseInt(document.getElementById('q2_nr_04').value);
    let nr_05 = parseInt(document.getElementById('q2_nr_05').value);
    let nr_06 = parseInt(document.getElementById('q2_nr_06').value);
    var iguais = 0

    if(nr_01 == nr_02 || nr_01 == nr_03 || nr_01 == nr_04 ||nr_01 == nr_05 ||nr_01 == nr_06){
        iguais += 1
    }if(nr_02 == nr_01 || nr_01 == nr_03 || nr_02 == nr_04 ||nr_02 == nr_05 ||nr_02 == nr_06){
        iguais += 1
    }if(nr_03 == nr_01 || nr_03 == nr_02 || nr_03 == nr_04 ||nr_03 == nr_05 ||nr_03 == nr_06){
        iguais += 1
    }if(nr_04 == nr_01 || nr_04 == nr_02 || nr_04 == nr_03 ||nr_04 == nr_05 ||nr_04 == nr_06){
        iguais += 1
    }if(nr_05 == nr_01 || nr_05 == nr_02 || nr_05 == nr_03 ||nr_05 == nr_04 ||nr_05 == nr_06){
        iguais += 1
    }if(nr_06 == nr_01 || nr_06 == nr_02 || nr_06 == nr_03 ||nr_06 == nr_04 ||nr_06 == nr_05){
        iguais += 1
    }


    /*

        Digite seu código aqui!!!!

    */
   

    alert("Resultado da questão 02 - Números Iguais: " + 
    iguais
    );

}


// Função para resolução da QUESTÃO 03
function q_03(){

    let valor = parseFloat(document.getElementById('valor').value);
    let forma = document.getElementById('forma').value;


    if(forma === "C"){
        valor = valor -(valor * 10/100)
        forma = "Cartão"

    }else if(forma === "P"){
        valor = valor -(valor * 20/100)
        forma = "PIX"
    }else if(forma === "D"){
        valor = valor -(valor * 30/100)
        forma = "DINHEIRO"

    }

    alert("Resultado da questão 03 - Valor: " + 
    valor + " : " +
    "forma: " +
    forma
    );
}


// Função para resolução da QUESTÃO 04
function q_04(){
    
    let nome = document.getElementById('nome').value;
    let idade = parseInt(document.getElementById('idade').value);
    

    if(idade == 5 && idade <= 7){
        condicao = "Infantil A"
        
    }else if(idade >= 8 && idade <= 10){
        condicao = "Infantil B"
    }
    else if(idade >= 11 && idade <= 13){
        condicao = "juvenil A"
    }
    else if(idade >= 14 && idade <= 17){
        condicao = "Juvenil B"
    }
    else if(idade > 18){
        //levo em consideração o enunciado, porém deveria ser maior igual a 18
        condicao = "Adulto"
    }

    alert("Resultado da questão 04 - Nome: " + 
    nome + " : " +
    "Condição: " +
    condicao
    );

}