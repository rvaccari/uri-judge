"""
Conversão de Tempo

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em
uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:
segundos, conforme exemplo fornecido.

https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

--
time = int(input())
seconds = time % 60
minutes = time // 60
hours = 0
if minutes > 60:
    hours = minutes // 60
    minutes = minutes % 60

print('%i:%i:%i' % (hours, minutes, seconds))

--

>>> resolve(556)
0:9:16

>>> resolve(1)
0:0:1

>>> resolve(140153)
38:55:53


"""


def resolve(time):
    seconds = time % 60
    minutes = time // 60
    hours = 0
    if minutes > 60:
        hours = minutes // 60
        minutes = minutes % 60

    print('%i:%i:%i' % (hours, minutes, seconds))
