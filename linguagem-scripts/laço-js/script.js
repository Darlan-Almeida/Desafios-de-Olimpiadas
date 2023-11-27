array =  [2, 5, 7, 9, 3, 4, 5, 6, 8, 9, 2, 4, 1, 1, 5]
valor = 0


for( x of array){
    console.log(x)
}


for(x of array){
    if(x % 2 !== 0){
        console.log("numeros impares: " + x)
    }
}


for( x of array){
    valor += x
}

console.log("a soma dos valores: " + valor)


for(let index = 0 ; index < array.length; index++){
    if(array[index] == 9){
        array.splice(index , 1)
    }

}

console.log("lista com todos os numeros 9 removido" , array)