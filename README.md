# Programação-Estruturada-Exercícios-01

## Questão 1:
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.


## Questão 2:
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

## Questão 3:
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha

## Questão 4:
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    
## Questão 5:

    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno

## Questão 6:

Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.

Veja abaixo os exemplos de entrada e saída esperadas.

[Referência](https://www.thehuxley.com/problem/699?quizId=4536)

### Formato de entrada

O usuário deve digitar um inteiro N.
O usuário deve digitar um inteiro M.

### Formato de saída

O programa deve exibir V, X, Y, Z


### Exemplo 1:

Entrada:

- 2016
- 4

Saída:

- 2020 2024 2028 2032

### Exemplo 2:

Entrada:

- 1999
- 1

Saída:

- 2000 2001 2002 2003

## Questão 7:

Faça um programa que leia uma sequencia de números e indique se eles são primos ou não.  Você deve parar ao ler o número -1.

[Referência](https://www.thehuxley.com/problem/972?quizId=4457)

### Formato de entrada

Você irá receber uma sequência de números. A entrada termina quando o número lido for -1.

### Formato de saída

Para cada número lido você deve imprimir Não caso o número não seja primo ou Primo caso seja.

### Exemplo 1:

Entrada:

- 5
- 4
- 6
- -1

Saída:

- Primo
- Não
- Não

## Questão 8:

Valquíria trabalha em uma padaria e foi roubada ontem. Seus clientes ficaram com pena e resolveram organizar uma vaquinha para comprar um novo celular para ela. Escreva um programa que receba como entrada o valor doado por cada cliente, até que seja informado um valor negativo, e exiba o total arrecadado e o valor médio doado por eles.

[Referência](https://www.thehuxley.com/problem/465?quizId=4457)

### Formato de entrada

Vários valores reais, até que seja informado um negativo


### Formato de saída

Dois valores reais, com duas casas decimais cada um

Atenção para a sequência indicada na descrição

### Exemplo 1:

Entrada:

- 2.5
- 5.0
- 3.2
- -4

Saída:

- 10.70
- 3.57

## Questão 9:

A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.

[Referência](https://www.thehuxley.com/problem/445?quizId=4276)

### Formato de entrada

Dois valores inteiros, separados por uma quebra de linha



### Formato de saída

Um valor real com duas casas decimais



### Exemplo 1:

Entrada:

- 1
- 80

Saída:

- 90.00

### Exemplo 2:

Entrada:

- 0
- 80

Saída:

- Valor inválido

### Exemplo 3:

Entrada:

- 1
- 0

Saída:

- 90.00

## Questão 10:

Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius

[Referência](https://www.thehuxley.com/problem/1080?quizId=4225)

### Formato de entrada

Uma escala de medida de temperatura ("C", "F" ou "K")

Um valor de temperatura a ser convertido

Esse valor deve obedecer os seguintes valores mínimos (float):
Celsius: t >= -273.15
Fahrenheit: t >= -459,67
Kelvin: t >= 0.0
Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
"Valor de temperatura abaixo do minimo"
Não há limite máximo de temperatura


### Formato de saída

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
"Valor de temperatura abaixo do minimo"

![Tabela de Conversão](https://www.infoescola.com/wp-content/uploads/2010/01/conversao-de-escalas-termometricas-tabela-600x250.jpg)

### Exemplo 1:

Entrada:

- F
- 34.0

Saída:

- 1.11 C
- 274.26 K

### Exemplo 2:

Entrada:

- K
- -8.0

Saída:

- Valor de temperatura abaixo do minimo


### Exemplo 3:

Entrada:

- K
- 29.0

Saída:

- -244.15 C
- -407.47 F

### Exemplo 3:

Entrada:

- C
- -237.0

Saída:

- -394.60 F
- 36.15 K
   

