"""
Cálculo Simples

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário
de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada
peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores,
respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar
um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com
2 casas após o ponto.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

--
line1 = input().split(' ')
line2 = input().split(' ')
id_1, qtd_1, value_1 = int(line1[0]), float(line1[1]), float(line1[2])
id_2, qtd_2, value_2 = int(line2[0]), float(line2[1]), float(line2[2])
total = (qtd_1 * value_1) + (qtd_2 * value_2)
print('VALOR A PAGAR: R$ %.2f' % total)
--

>>> resolve([12, 1, 5.30], [16, 2, 5.10])
VALOR A PAGAR: R$ 15.50

>>> resolve([13, 2, 15.30], [161, 4, 5.20])
VALOR A PAGAR: R$ 51.40

>>> resolve([1, 1, 15.10], [2, 1, 15.10])
VALOR A PAGAR: R$ 30.20

"""


def resolve(line1, line2):
    id_1, qtd_1, value_1 = line1
    id_2, qtd_2, value_2 = line2
    total = (qtd_1 * value_1) + (qtd_2 * value_2)
    print('VALOR A PAGAR: R$ %.2f' % total)
