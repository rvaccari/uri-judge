"""
Coordenadas de um Ponto

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um
ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se
está sobre um dos eixos cartesianos ou na origem (x = y = 0).

       Y
    Q2 | Q1
    ------- X
    Q3 | Q4

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a
situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

--
x, y = map(float, input().strip().split())

if x == y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif (x > 0) and (y > 0):
    print('Q1')
elif (x > 0) and (y < 0):
    print('Q4')
elif (x < 0) and (y < 0):
    print('Q3')
else:
    print('Q2')
--

>>> resolve(4.5, -2.2)
Q4

>>> resolve(0.1, 0.1)
Q1

>>> resolve(0.0, 0.0)
Origem

>>> resolve(0, 0)
Origem

>>> resolve(0.0, 1.0)
Eixo Y

>>> resolve(0.1, 0)
Eixo X

>>> resolve(-0.1, 1)
Q2

>>> resolve(-0.3, -5)
Q3

"""


def resolve(x, y):
    if x == y == 0:
        print('Origem')
    elif x == 0:
        print('Eixo Y')
    elif y == 0:
        print('Eixo X')
    elif (x > 0) and (y > 0):
        print('Q1')
    elif (x > 0) and (y < 0):
        print('Q4')
    elif (x < 0) and (y < 0):
        print('Q3')
    else:
        print('Q2')
