"""
    Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo, dados os números 3 e 4 o seu 
    programa deve escrever o número 81.
"""


def main():
    n = int(input('Informe um número inteiro'))
    k = int(input('Informe um número inteiro maior ou igual a 0'))

    if k < 0:
        print("K deve ser maior ou igual a 0")
        return False

    result = n**k

    print('O resultado de', n, 'elevado a ', k, 'é ', result)

main()