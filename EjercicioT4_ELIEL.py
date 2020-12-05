import re

opcion = 0
while opcion != 6:
    print('----------------------------- Eliel Novelo ------------------------------')
    print('\nSelecciona una Opción')
    print('1.- Variables válidas\n2.- Enteros y decimales')
    print('3.- Operadores aritméticos  \n4.- Operadores relacionales. \n5.- Palabras reservadas.\n6.- Salir')
    opcion = int(input("Opción a realizar: "))

    if opcion == 1:
        print('Variables Válidas : suma, resta, contador, acumulador ')
        filename = 'Datos.txt'
        textfile = open(filename, "r")
        regexsuma = "\d+\s?\+\s?\d+"
        regexresta = "\d+\s?\-\s?\d+"
        regexconta = "[i]+\+[\+]?"
        regexacumu = "\w+\s?\+?\=\s?\w+\s?\+?\s?\w+"
        regsuma = re.compile(regexsuma)
        regresta = re.compile(regexresta)
        regconta = re.compile(regexconta)
        regacumu = re.compile(regexacumu)
        for line in textfile:
            lista = regsuma.findall(line)
            print(lista)
            lista = regresta.findall(line)
            print(lista)
            lista = regconta.findall(line)
            print(lista)
            lista = regacumu.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 2:
        print('Enteros y decimales')
        filename = 'Datos.txt'
        textfile = open(filename, "r")
        regex = "\d+\.?\d+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 3:
        print('Operadores aritméticos')
        filename = 'Datos.txt'
        textfile = open(filename, "r")
        regex = "[\+\-\*\/\%]"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        print('Operadores relacionales')
        filename = 'Datos.txt'
        textfile = open(filename, "r")
        regex = "\=[\=]|\![\=]|\<\=?|\>\=?"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 5:
        print('Operadores relacionales')
        filename = 'Datos.txt'
        textfile = open(filename, "r")
        regex = "assert|pass|and|as|break|class|continue|def|del|elif|else"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print('Ingresa valores dentro de las opciones')