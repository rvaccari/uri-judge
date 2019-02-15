"""
Média 2

Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir,
calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C
tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a variável MEDIA conforme exemplo abaixo, com 1 dígito após o ponto decimal e com
um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não
esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá
"Presentation Error".

https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

--
a = float(input()) * 2
b = float(input()) * 3
c = float(input()) * 5
media = (a + b + c) / 10
print('MEDIA = %.1f' % media)
--

>>> resolve(5.0, 6.0, 7.0)
MEDIA = 6.3

>>> resolve(5.0, 10.0, 10.0)
MEDIA = 9.0

>>> resolve(10.0, 10.0, 5.0)
MEDIA = 7.5

"""


def resolve(a, b, c):
    p1 = 2
    p2 = 3
    p3 = 5
    media = ((a * p1) + (b * p2) + (c * p3)) / (p1 + p2 + p3)
    print('MEDIA = %.1f' % media)
