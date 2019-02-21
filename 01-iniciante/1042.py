"""
Sort Simples

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em
ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram
lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

--
inp = input().split()
order = [int(x) for x in inp]
order.sort()

print(*order, sep='\n')
print('')
print(*inp, sep='\n')

--

>>> resolve(7, 21, -14)
-14
7
21
<BLANKLINE>
7
21
-14

>>> resolve(-14, 21, 7)
-14
7
21
<BLANKLINE>
-14
21
7

"""


def resolve(a, b, c):
    inp = [a, b, c]
    order = [int(x) for x in inp]
    order.sort()

    print(*order, sep='\n')
    print('')
    print(*inp, sep='\n')
