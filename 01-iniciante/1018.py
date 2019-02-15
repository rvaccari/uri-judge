"""
Cédulas

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no
qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso
contrário seu programa apresentará a mensagem: “Presentation Error”.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

--
value = int(input())
print(value)
print('%i nota(s) de R$ 100,00' % (value // 100))
value = value % 100
print('%i nota(s) de R$ 50,00' % (value // 50))
value = value % 50
print('%i nota(s) de R$ 20,00' % (value // 20))
value = value % 20
print('%i nota(s) de R$ 10,00' % (value // 10))
value = value % 10
print('%i nota(s) de R$ 5,00' % (value // 5))
value = value % 5
print('%i nota(s) de R$ 2,00' % (value // 2))
value = value % 2
print('%i nota(s) de R$ 1,00' % (value // 1))
--

>>> resolve(576)
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

>>> resolve(11257)
11257
112 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
0 nota(s) de R$ 1,00

>>> resolve(503)
503
5 nota(s) de R$ 100,00
0 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
0 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

"""


def resolve(value):
    print(value)

    print('%i nota(s) de R$ 100,00' % (value // 100))
    value = value % 100
    print('%i nota(s) de R$ 50,00' % (value // 50))
    value = value % 50
    print('%i nota(s) de R$ 20,00' % (value // 20))
    value = value % 20
    print('%i nota(s) de R$ 10,00' % (value // 10))
    value = value % 10
    print('%i nota(s) de R$ 5,00' % (value // 5))
    value = value % 5
    print('%i nota(s) de R$ 2,00' % (value // 2))
    value = value % 2
    print('%i nota(s) de R$ 1,00' % (value // 1))
