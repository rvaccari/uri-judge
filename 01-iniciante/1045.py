"""
Tipos de Triângulos

Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que
o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes
três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B)
e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

--
p1,p2,p3 = map(float, input().strip().split())
c = p3
if p1 > p2:
    a = p1
    b = p2
else:
    a = p2
    b = p1

if a < p3:
    a = p3
    b = p2
    c = p1

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2 + c**2):
        print('TRIANGULO RETANGULO')
    if a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if a**2 == b**2 == c**2:
        print('TRIANGULO EQUILATERO')
    elif (a**2 == b**2) or (b**2 == c**2) or (a**2 == c**2):
        print('TRIANGULO ISOSCELES')

--

>>> resolve(7.0, 5.0, 7.0)
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES

>>> resolve(6.0, 6.0, 10.0)
TRIANGULO OBTUSANGULO
TRIANGULO ISOSCELES

>>> resolve(6.0, 6.0, 6.0)
TRIANGULO ACUTANGULO
TRIANGULO EQUILATERO

>>> resolve(5.0, 7.0, 2.0)
NAO FORMA TRIANGULO

>>> resolve(6.0, 8.0, 10.0)
TRIANGULO RETANGULO

"""


def resolve(p1, p2, p3):
    c = p3
    if p1 > p2:
        a = p1
        b = p2
    else:
        a = p2
        b = p1

    if a < p3:
        a = p3
        b = p2
        c = p1

    if a >= (b + c):
        print('NAO FORMA TRIANGULO')
    else:
        if a ** 2 == (b ** 2 + c ** 2):
            print('TRIANGULO RETANGULO')
        if a ** 2 > (b ** 2 + c ** 2):
            print('TRIANGULO OBTUSANGULO')
        if a ** 2 < (b ** 2 + c ** 2):
            print('TRIANGULO ACUTANGULO')
        if a ** 2 == b ** 2 == c ** 2:
            print('TRIANGULO EQUILATERO')
        elif (a ** 2 == b ** 2) or (b ** 2 == c ** 2) or (a ** 2 == c ** 2):
            print('TRIANGULO ISOSCELES')
