"""
Fórmula de Bhaskara

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente
“Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel
calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha
após cada mensagem.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
f(x)=2x2−6x−20
--
a, b, c = map(float, input().strip().split())
try:
    r1 = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)
except:
    print('Impossivel calcular')

--

>>> resolve(10.0, 20.1, 5.1)
R1 = -0.29788
R2 = -1.71212

>>> resolve(0.0, 20.0, 5.0)
Impossivel calcular

>>> resolve(10.3, 203.0, 5.0)
R1 = -0.02466
R2 = -19.68408

>>> resolve(10.0, 3.0, 5.0)
Impossivel calcular

"""


def resolve(a, b, c):
    try:
        delta = ((b ** 2) - 4 * a * c) ** 0.5
        r1 = (-b + delta) / (2 * a)
        r2 = (-b - delta) / (2 * a)
        print('R1 = %.5f' % r1)
        print('R2 = %.5f' % r2)
    except:
        print('Impossivel calcular')
