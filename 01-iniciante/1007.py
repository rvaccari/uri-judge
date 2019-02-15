"""
Diferença

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do
produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo,
com um espaço em branco antes e depois da igualdade.


https://www.urionlinejudge.com.br/judge/pt/problems/view/1007

--
a = int(input())
b = int(input())
c = int(input())
d = int(input())
diferenca = a * b - c * d
print('DIFERENCA = %i' % diferenca)
--

>>> resolve(5, 6, 7, 8)
DIFERENCA = -26

>>> resolve(0, 0, 7, 8)
DIFERENCA = -56

>>> resolve(5, 6, -7, 8)
DIFERENCA = 86

"""


def resolve(a, b, c, d):
    diferenca = a * b - c * d
    print('DIFERENCA = %i' % diferenca)
