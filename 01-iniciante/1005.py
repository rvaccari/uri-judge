"""
Média 1

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de
um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota
B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até
10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída
Calcule e imprima a variável MEDIA conforme exemplo abaixo, com 5 dígitos após o ponto
decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla
precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após
o resultado, caso contrário, você receberá "Presentation Error".

https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

--
a = float(input())
b = float(input())
p1 = 3.5
p2 = 7.5
media = (a * p1 + b * p2) / (p1 + p2)
print('MEDIA = %.5f' % media)
--

>>> resolve(5.0, 7.1)
MEDIA = 6.43182

>>> resolve(0.0, 7.1)
MEDIA = 4.84091

>>> resolve(10.0, 10.0)
MEDIA = 10.00000

"""


def resolve(a, b):
    p1 = 3.5
    p2 = 7.5
    media = (a * p1 + b * p2) / (p1 + p2)
    print('MEDIA = %.5f' % media)
