#   WRITE VALUES

#valores_celulares = [100, 100, 100]
#with open('valores_celulares.txt', 'w+') as arquivo:
#     for valor in valores_celulares:
#         arquivo.write(str(valor) + '\n')
#---------------------------------------------------


#   READ VALUES

#valores_celulares = [1000, 2100, 123100]
#with open('valores_celulares.txt', 'r') as arquivo:
#     for valor in valores_celulares:
#         print(valor)
#---------------------------------------------------


#   READ AND WRITE VALUES

#valores_celulares = [1000, 2100, 123100]
#with open('valores_celulares.txt', 'r+') as arquivo:
#     for valor in valores_celulares:
#         print(valor)
#     arquivo.write('9000') 
#     for valor in valores_celulares:
#        print(valor)
#---------------------------------------------------
with open('credito.csv', 'r+') as arquivo:
    for pessoas in arquivo:
        print(pessoas)

