"""
Distância Entre Dois Pontos

Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a
vírgula, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de
ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o
ponto decimal.

--
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())
distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
print('%.4f' % distance)
--

>>> resolve([1.0, 7.0], [5.0, 9.0])
4.4721

>>> resolve([-2.5, 0.4], [12.1, 7.3])
16.1484

>>> resolve([2.5, -0.4], [-12.2, 7.0])
16.4575

"""


def resolve(x, y):
    x1, y1 = map(float, x)
    x2, y2 = map(float, y)

    distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    print('%.4f' % distance)
