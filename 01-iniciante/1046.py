"""
Tempo de Jogo

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo
que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora
e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do
jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

--
start, end = map(int, input().strip().split())
if start >= end:
    end = end + 24
period = end - start

print('O JOGO DUROU %i HORA(S)' % period)
--

>>> resolve(16, 2)
O JOGO DUROU 10 HORA(S)

>>> resolve(0, 0)
O JOGO DUROU 24 HORA(S)

>>> resolve(2, 16)
O JOGO DUROU 14 HORA(S)

"""


def resolve(start, end):
    if start >= end:
        end = end + 24
    period = end - start

    print('O JOGO DUROU %i HORA(S)' % period)
