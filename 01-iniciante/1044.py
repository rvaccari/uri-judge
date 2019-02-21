"""
Múltiplos

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao
Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

--
a, b = map(int, input().strip().split())
if ((b % a) == 0) or ((a % b) == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
--

>>> resolve(6, 24)
Sao Multiplos

>>> resolve(6, 25)
Nao sao Multiplos

"""


def resolve(a, b):
    if ((b % a) == 0) or ((a % b) == 0):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
