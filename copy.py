
with open('credito.csv', 'r+') as arquivo:
    for pessoas in arquivo:
        arquivo2 = open('credito3.csv', 'w+')
        for pessoas in arquivo:
            arquivo2.write(pessoas)