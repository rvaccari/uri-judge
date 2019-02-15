"""
Consumo

Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida
(em Km) e o total de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância
total percorrida (em Km), e um valor real Y representando o total de combustível gasto,
com um dígito após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula,
seguido da mensagem "km/l".

https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

--
distance = int(input())
liters = float(input())
consumption = distance / liters
print('%0.3f km/l' % consumption)
--

>>> resolve(500, 35.0)
14.286 km/l

>>> resolve(2254, 124.4)
18.119 km/l

>>> resolve(4554, 464.6)
9.802 km/l

"""


def resolve(distance, liters):
    consumption = distance / liters
    print('%0.3f km/l' % consumption)
