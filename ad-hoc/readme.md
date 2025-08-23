# AD-hoc

## Questão: Make Them Narrow

### Enunciado
Você recebe uma sequência `A` de comprimento `N`.  
Escolha exatamente `K` elementos de `A` e remova-os.  
Concatenando os elementos restantes na ordem original, obtemos uma nova sequência `B`.  

Seu objetivo é **minimizar**:

> `max(B) - min(B)`

**Restrições:**
- `1 ≤ K < N ≤ 2 × 10^5`
- `1 ≤ Ai ≤ 10^9`

**Entrada:**
N K
A1​ A2​ … AN​

**Saída:**  
Um inteiro representando o menor valor possível de `(max(B) - min(B))`.


---

### Resposta

**Código em Python:**

```python
n , k = input().split()
entrada = [int(i) for i in input().split()]
entrada.sort()
menor = entrada[len(entrada) - 1] - entrada[0]

for i in range(int(k)+1):
    x = entrada[len(entrada) - 1 - int(k) + i] - entrada[i]
    print(x)
    if x < menor:
        menor = x

print(menor)
```

### Explicação da Técnica (Sliding Window)

A ideia central é:

1. **Ordenar o array `A`:**  
   Quando os elementos estão ordenados, os valores mais próximos ficam juntos.  
   A menor diferença entre o maior e o menor de um subconjunto estará sempre em uma **faixa consecutiva**.

2. **Escolher uma janela de tamanho `N-K`:**  
   Precisamos manter `N-K` elementos.  
   Assim, percorremos todas as janelas consecutivas de tamanho `N-K` no array ordenado e calculamos:
   ```
   diferença = A[i + (N-K) - 1] - A[i]
   ```
   Pegamos o mínimo entre todas essas diferenças.

3. **Complexidade:**  
   - Ordenação: `O(N log N)`
   - Sliding Window: `O(N)`

Essa técnica é um exemplo clássico de **"AD-hoc" + Sliding Window após ordenação**, usada sempre que precisamos **minimizar o intervalo (max-min)** de um subconjunto de tamanho fixo.


## Questão: Count ABC Again

### Enunciado
Você recebe uma string `S` de comprimento `N`.  
Você também recebe `Q` consultas. Cada consulta é do formato:

- Dado um inteiro `X` e um caractere `C`, substitua o caractere `S[X]` por `C` (índice 1-based).  
- Após cada substituição, imprima o número de vezes que a substring `"ABC"` aparece em `S`.

**Definição:** Uma substring é uma sequência de caracteres consecutivos de `S`.

**Restrições:**
- `3 ≤ N ≤ 2 × 10^5`
- `1 ≤ Q ≤ 2 × 10^5`
- `S` contém apenas letras maiúsculas do alfabeto inglês.
- `1 ≤ X ≤ N`
- `C` é uma letra maiúscula.

**Entrada:**
```
N Q
S
X1 C1
X2 C2
...
XQ CQ
```

**Saída:**  
Para cada consulta, imprimir o número de ocorrências de `"ABC"` após a atualização.

---

### Resposta

**Código em Python:**

```python

N, Q = map(int, input().split())
S = list(input().strip())

# Contagem inicial de "ABC"
count = 0
for i in range(N - 2):
    if S[i:i+3] == ['A', 'B', 'C']:
        count += 1

for _ in range(Q):
    x, c = input().split()
    x = int(x) - 1  # converter para índice 0-based

    # Remover ocorrências afetadas pela posição alterada
    for i in range(x - 2, x + 1):
        if 0 <= i <= N - 3 and S[i:i+3] == ['A', 'B', 'C']:
            count -= 1

    # Atualizar caractere
    S[x] = c

    # Adicionar novas ocorrências (se houver)
    for i in range(x - 2, x + 1):
        if 0 <= i <= N - 3 and S[i:i+3] == ['A', 'B', 'C']:
            count += 1

    print(count)
```

---

### Explicação da Técnica (Sliding Window Local)

- **Observação-chave:** A substring `"ABC"` tem tamanho 3.  
  Uma atualização em `S[x]` só pode afetar **três substrings**:  
  aquelas começando em `x-2`, `x-1` e `x`.

- **Abordagem:**
  1. Contamos inicialmente todas as ocorrências de `"ABC"` na string.
  2. Para cada atualização, removemos do contador as ocorrências de `"ABC"` que estavam nas janelas afetadas.
  3. Alteramos o caractere.
  4. Recontamos as ocorrências de `"ABC"` nas janelas afetadas e adicionamos ao contador.

- **Complexidade:**  
  - Contagem inicial: `O(N)`  
  - Cada query: `O(1)` (verifica no máximo 3 posições)  
  - Total: `O(N + Q)`, eficiente para os limites dados.

Essa técnica é um exemplo de **atualização local com janela deslizante de tamanho fixo (Sliding Window)**, típica em problemas **AD-hoc**.

## Questão: K-th Largest Value

### Enunciado
Você recebe um array `a` de comprimento `n`, onde cada elemento é `0` ou `1`.  
Você precisa processar `q` consultas de dois tipos:

1. `1 x` : Inverte o valor de `a[x]` → `a[x] = 1 - a[x]`  
2. `2 k` : Imprime o k-ésimo maior valor do array.

**Nota:** O k-ésimo maior valor de um array `b` é definido como o k-ésimo elemento após ordenar `b` em ordem não crescente.

**Restrições:**
- `1 ≤ n, q ≤ 10^5`
- `0 ≤ ai ≤ 1`
- Pelo menos uma query do tipo 2 será fornecida.

**Entrada:**
```
n q
a1 a2 ... an
t1 x1
t2 x2
...
tq xq
```

**Saída:**  
Para cada query do tipo 2, imprima o valor correspondente.

**Exemplo:**

Entrada:
```
5 5
1 1 0 1 0
2 3
1 2
2 3
2 1
2 5
```

Saída:
```
1
0
1
0
```

---

### Resposta

```python
qtd = input().split()
elementos = input().split()

z = 0
u = 0

for i in elementos:
    if i == '0':
        z += 1
    elif i == '1':
        u += 1

contador = 0
results = []
while contador < int(qtd[1]):
    comand = input().split()
    pos = int(comand[1])
    if comand[0] == '2':
        if pos <= u:
            results.append(1)
        else:
            results.append(0)
    else:
        if elementos[pos-1] == '1':
            elementos[pos-1] = '0'
            u -= 1
            z += 1
        else:
            elementos[pos-1] = '1'
            u += 1
            z -= 1
    contador += 1

for i in results:
    print(i)

```

---

### Explicação da Técnica

- **Observação chave:**  
  Todos os elementos são `0` ou `1`. Portanto, o k-ésimo maior valor depende apenas do número de `1`s no array.

- **Contagem incremental:**  
  1. Inicializamos `count_1s = sum(a)`  
  2. Para cada operação de inversão (`1 x`), atualizamos `count_1s` em O(1)  
  3. Para cada operação de consulta (`2 k`):
     - Se `count_1s ≥ k`, o k-ésimo maior é `1`
     - Caso contrário, é `0`

- **Complexidade:**  
  - Inicialização: O(n)  
  - Cada query: O(1)  
  - Total: O(n + q), eficiente para n, q ≤ 10^5

- **Categoria:**  
  - **AD-hoc + Contagem Incremental / Counting**  
  - Explora a propriedade de que o array tem **apenas 0s e 1s**, evitando ordenações ou buscas caras.


## Tópico Importante: Crivo de Eratóstenes (Sieve of Eratosthenes)

### Descrição
O **Crivo de Eratóstenes** é o algoritmo mais eficiente para encontrar **todos os números primos até um limite `n`**, com complexidade **O(n log log n)**.  
É extremamente útil em problemas AD-hoc que exigem verificação de primalidade de múltiplos números ou contagem de primos em intervalos grandes.

---

### **Ideia do Algoritmo**
1. Criar um array `is_prime` de tamanho `n+1`, inicializado com `True` (exceto 0 e 1).
2. Iterar de `p = 2` até `√n`:
   - Se `p` for primo (`is_prime[p] == True`), marcar todos os múltiplos de `p` (a partir de `p*p`) como não primos.
3. Ao final, todos os números `i` com `is_prime[i] == True` são primos.

---

### **Implementação em Python**

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Exemplo: todos os primos até 100
primes_up_to_100 = sieve(100)
print(primes_up_to_100)
```

**Saída:**
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

---

### **Otimizações**
- Marcar apenas números ímpares após o 2, economizando espaço e tempo.
- Usar **bitarrays** para grandes `n` (≥ 10^8), reduzindo memória.

---

### **Complexidade**
- **Tempo:** O(n log log n)
- **Espaço:** O(n)

---

### **Aplicação em Problemas AD-hoc**
- Contar primos em intervalos grandes.
- Verificar primalidade repetidamente sem recalcular cada número.
- Problemas de combinações, somas e propriedades de números primos.