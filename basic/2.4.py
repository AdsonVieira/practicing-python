




def main():
    
    
    fat = int(input('Informe um valor para calcular o fatorial'))
    result = 1

    while fat >= 2:

        if(result != 1):
            fatTemp = result
        else:
            fatTemp = fat
                
        result = fatTemp * (fat -1)
        fat =  fat - 1

    print(result)


main()