"""
Triângulo

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso
positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura,
mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

--
a, b, c = map(float, input().strip().split())
p = (a + b + c) / 2
area = p * (p - a) * (p - b) * (p - c)
if area > 0:
    print('Perimetro = %.1f' % (a + b + c))
else:
    t = ((a + b) / 2) * c
    print('Area = %.1f' % t)
--

>>> resolve(6.0, 4.0, 2.0)
Area = 10.0

>>> resolve(6.0, 4.0, 2.1)
Perimetro = 12.1

"""


def resolve(a, b, c):
    p = (a + b + c) / 2
    area = p * (p - a) * (p - b) * (p - c)
    if area > 0:
        print('Perimetro = %.1f' % (a + b + c))
    else:
        t = ((a + b) / 2) * c
        print('Area = %.1f' % t)
