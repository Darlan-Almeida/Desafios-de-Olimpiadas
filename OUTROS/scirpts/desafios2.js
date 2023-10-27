/*
Utilize a relação dos index para relacionar os arrays.

1)Imprima o preço da jaca.
2)Imprima uma lista de todas as frutas e seus preços.
3)Adicione a fruta maçã com seu preço: R$9,90.
4)Aplique 10% de desconto em todas as frutas.
5)Remova a fruta uva.
6)Imprima o nome da fruta mais barata.
7)Altere o valor da fruta banana para R$ 3,85.
8)Deixe o array de preços em ordem crescente e repita a questão 2.
9)Desenvolva um interface para que o usuário digite o nome da fruta e receba como
Resposta o seu preço.
*/
const frutas = [
    'laranja',
    'uva',
    'goiaba',
    'jaca',
    'banana'
]

const preco =[
    '2,50' ,
    '8,40' ,
    '6,99' ,
    '1,99' ,
    '4,99'
]

for( [ index , fruta] of frutas.entries()){
    if(fruta == "jaca"){
        var index_fruta = index
    }
}

console.log(preco[index_fruta]) // 1)Imprima o preço da jaca.


for([ index , fruta] of frutas.entries()){
    console.log("Fruta: " + fruta + " valor: " + preco[index])
}

frutas.push("maça")
preco.push("9,90")


for([ index , price] of preco.entries()){
    preco.splice(index , 1)
    parseFloat(price.replace("," , "."))
    preco.push(price)
    
}

console.log(preco)