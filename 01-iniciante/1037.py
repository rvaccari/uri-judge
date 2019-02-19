"""
Intervalo

Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo
em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se
encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser
impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

--
value = float(input())
if 0 <= value <= 25:
    print('Intervalo [0,25]')
elif 25 < value <= 50:
    print('Intervalo (25,50]')
elif 50 < value <= 75:
    print('Intervalo (50,75]')
elif 75 < value <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
--

>>> resolve(25.01)
Intervalo (25,50]

>>> resolve(25.00)
Intervalo [0,25]

>>> resolve(100.00)
Intervalo (75,100]

>>> resolve(-25.02)
Fora de intervalo

"""


def resolve(value):
    if 0 <= value <= 25:
        print('Intervalo [0,25]')
    elif 25 < value <= 50:
        print('Intervalo (25,50]')
    elif 50 < value <= 75:
        print('Intervalo (50,75]')
    elif 75 < value <= 100:
        print('Intervalo (75,100]')
    else:
        print('Fora de intervalo')
