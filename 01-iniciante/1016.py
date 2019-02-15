"""
Distância

Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante
de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou
seja, consegue se afastar um quilômetro a cada 2 minutos.

Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar
essa distância do outro carro.

Entrada
O arquivo de entrada contém um número inteiro.

Saída
Imprima o tempo necessário seguido da mensagem "minutos".

https://www.urionlinejudge.com.br/judge/pt/problems/view/1016

--
x = int(input())
print('%i minutos' % (x * 2))
--

>>> resolve(30)
60 minutos

>>> resolve(110)
220 minutos

>>> resolve(7)
14 minutos

"""


def resolve(x):
    print('%i minutos' % (x * 2))

