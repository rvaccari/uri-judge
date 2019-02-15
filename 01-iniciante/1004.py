"""
Produto Simples

Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e
atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem
correspondente.

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois
da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu
programa apresentará a mensagem: “Presentation Error”.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1004

--
a = int(input())
b = int(input())
prod = a * b
print('PROD = %i' % prod)
--

>>> resolve(3, 9)
PROD = 27

>>> resolve(-30, 10)
PROD = -300

>>> resolve(0, 9)
PROD = 0

"""


def resolve(a, b):
    prod = a * b
    print('PROD = %i' % prod)
