"""
Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, 
calcular a sua soma. Por exemplo, para a sequência:

Os números inteiros são os números positivos e negativos. Estes números formam o conjunto dos números inteiros, 
indicado por ℤ

o seu programa deve escrever o número 35.

"""

def  main():
    
    x = int(input('Informe um número inteiro'))
    sum = 0

    while x != 0:
        sum = sum + x
        x = int(input('Informe um número inteiro'))
        
        


    print(sum)

main()