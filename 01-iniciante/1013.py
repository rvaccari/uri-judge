"""
O Maior

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido
da mensagem “eh o maior”. Utilize a fórmula:


Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

--
a, b, c = map(int, input().strip().split())

maior = (a + b + abs(a - b)) / 2
maior = (maior + c + abs(maior - c)) / 2

print('%i eh o maior' % maior)
--

>>> resolve(7, 14, 106)
106 eh o maior

>>> resolve(217, 14, 6)
217 eh o maior


"""


def resolve(a, b, c):
    maior = (a + b + abs(a - b)) / 2
    maior = (maior + c + abs(maior - c)) / 2

    print('%i eh o maior' % maior)
