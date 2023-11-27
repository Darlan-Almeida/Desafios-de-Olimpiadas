/* 1)Imprima o primeiro elemento.
2)Imprima o terceiro elemento.
3)Imprima o ultimo elemento.
4)Imprima o tamanho do array.
5)Imprima todos os elementos.
6)Busque e imprima o maior elemento. Utilize for of
7)Busque e imprima o menor elemento. Utilize for of
8)Busque e imprima os elementos pares. Utilize for of
9)Remova o ultimo elemento.
10)Remova o elemento de index = 3.
11)Adicione o numero 32 ao final do array.
12)Imprima os números que ocorrem mais de uma vez.
*/

const aposta = [1 , 59 , 32 , 45 , 20 , 25 ,60 , 95 , 31]

console.log(aposta[0])// 1)Imprima o primeiro elemento
console.log(aposta[4])// 2)Imprima o terceiro elemento.

for([ index , element] of aposta.entries() ){
    last = aposta.length - 1
    if(index == last){
        console.log(element)// 3)Imprima o ultimo elemento.

    }

}

var quantityElements = 0
for(element of aposta){
    quantityElements += 1 
}

console.log(quantityElements) // 4)Imprima o tamanho do array.


for(elements of aposta){
    console.log()// 5)Imprima todos os elementos.
 
}

let min= aposta[0]
let max= aposta[0]
for(elements of aposta){
    if(elements < min){
        min = elements
    }
    if(elements > max){
        max = elements
    }
    if(elements % 2 == 0){
        console.log(elements) // 8)Busque e imprima os elementos pares. Utilize for of

    }

}
console.log(min) // 7)Busque e imprima o menor elemento. Utilize for of

console.log(max) // 6)Busque e imprima o maior elemento. Utilize for of


for([ index , element] of aposta.entries() ){
    last = aposta.length - 1
    if(index == last){
        aposta.splice(last) // 9)Remova o ultimo elemento.
        console.log(aposta)
    }

}


aposta.splice(3) // 10)Remova o elemento de index = 3.

aposta.push(32)

for(elements of aposta){
    elements1 = elements
    for(elements of aposta){
        elements2 = elements
    }
    if(elements1 == elements2){
        console.log(elements)// 12)Imprima os números que ocorrem mais de uma vez.

    }
}



for([ index1 , elements1] of aposta.entries()){
    for([ index2 , elements2] of aposta.entries()){
        if(elements1 == elements2 && index1 !== index2){
            console.log(elements1)
        }
    }
}
