"""
Teste de Seleção 1

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior
do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem
positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever
"Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

--
a, b, c, d = map(int, input().strip().split())

if (b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0) and (d > 0) and (a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
--

>>> resolve(5, 6, 7, 8)
Valores nao aceitos

>>> resolve(2, 3, 2, 6)
Valores aceitos

"""


def resolve(a, b, c, d):
    if (b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0) and (d > 0) and (
            a % 2 == 0):
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')
