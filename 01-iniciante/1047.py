"""
Tempo de Jogo com Minutos

Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir
calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

https://www.urionlinejudge.com.br/judge/pt/problems/view/1047

--
h1, m1, h2, m2 = map(int, input().strip().split())
hour = 0
minutes = (m2 + 60) - m1
if minutes >= 60:
    hour = h2 - h1
    minutes = minutes - 60
if hour < 0:
    hour = 24 - (hour * -1)
if (hour == 0) and (minutes == 0):
    hour = 24
    minutes = 0

print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % (hour, minutes))
--

>>> resp(7, 7, 7, 6)
O JOGO DUROU 23 HORA(S) E 59 MINUTO(S)

>>> resp(7, 8, 9, 10)
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

>>> resp(7, 7, 7, 7)
O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

>>> resp(7, 10, 8, 9)
O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)

>>> resp(15, 10, 8, 10)
O JOGO DUROU 17 HORA(S) E 0 MINUTO(S)


"""


def to_minutes(hour, minute):
    return 60 * hour + minute


def resolve(start_hour, start_minute, end_hour, end_minute):
    if (start_hour, start_minute) == (end_hour, end_minute):
        return str('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

    start_total_minutes = to_minutes(start_hour, start_minute)
    end_total_minutes = to_minutes(end_hour, end_minute)

    delta = end_total_minutes - start_total_minutes
    if delta < 0:
        delta += 24 * 60  # adding a day in minutes
    hour_minute_tpl = divmod(delta, 60)
    return 'O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % hour_minute_tpl


# print(resolve(*map(int, input().strip().split())))


def resp(start_hour, start_minute, end_hour, end_minute):
    print(resolve(start_hour, start_minute, end_hour, end_minute))
