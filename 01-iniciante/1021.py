"""
Notas e Moedas


Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor
monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor
pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas
possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas
necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial,
conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

--
val = input().split('.')
note = int(val[0])
coins = int(val[1])
print('NOTAS:')
print('%i nota(s) de R$ 100.00' % (note // 100))
note = note % 100
print('%i nota(s) de R$ 50.00' % (note // 50))
note = note % 50
print('%i nota(s) de R$ 20.00' % (note // 20))
note = note % 20
print('%i nota(s) de R$ 10.00' % (note // 10))
note = note % 10
print('%i nota(s) de R$ 5.00' % (note // 5))
note = note % 5
print('%i nota(s) de R$ 2.00' % (note // 2))
note = note % 2
print('MOEDAS:')
print('%i moeda(s) de R$ 1.00' % (note // 1))
print('%i moeda(s) de R$ 0.50' % (coins // 50))
coins = coins % 50
print('%i moeda(s) de R$ 0.25' % (coins // 25))
coins = coins % 25
print('%i moeda(s) de R$ 0.10' % (coins // 10))
coins = coins % 10
print('%i moeda(s) de R$ 0.05' % (coins // 5))
coins = coins % 5
print('%i moeda(s) de R$ 0.01' % (coins // 1))
--

>>> resolve('576.73')
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01

>>> resolve('4.00')
NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
2 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01

>>> resolve('91.01')
NOTAS:
0 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
2 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
1 moeda(s) de R$ 0.01

"""


def resolve(value):
    val = value.split('.')
    note = int(val[0])
    coins = int(val[1])
    print('NOTAS:')
    print('%i nota(s) de R$ 100.00' % (note // 100))
    note = note % 100
    print('%i nota(s) de R$ 50.00' % (note // 50))
    note = note % 50
    print('%i nota(s) de R$ 20.00' % (note // 20))
    note = note % 20
    print('%i nota(s) de R$ 10.00' % (note // 10))
    note = note % 10
    print('%i nota(s) de R$ 5.00' % (note // 5))
    note = note % 5
    print('%i nota(s) de R$ 2.00' % (note // 2))
    note = note % 2
    print('MOEDAS:')
    print('%i moeda(s) de R$ 1.00' % (note // 1))
    print('%i moeda(s) de R$ 0.50' % (coins // 50))
    coins = coins % 50
    print('%i moeda(s) de R$ 0.25' % (coins // 25))
    coins = coins % 25
    print('%i moeda(s) de R$ 0.10' % (coins // 10))
    coins = coins % 10
    print('%i moeda(s) de R$ 0.05' % (coins // 5))
    coins = coins % 5
    print('%i moeda(s) de R$ 0.01' % (coins // 1))
