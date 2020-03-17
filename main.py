import sys
import os.path
import re


def main():
    # Expresiones regulares para cada columna
    col1 = r'[A-Z]\d{7}'
    col2 = r'[A-Z]{3}'
    col3 = r'[A-Z]'
    col5 = r'[A-Z]{2}'
    col7 = r'[^\t\n\r\f\v]+'
    col8 = r'\d'

    # Expresión regular
    pattern = r'^{}\|{}\|{}\|{}\|{}\|{}\|{}\|{}\|$'.format(
        col1, col2, col3, col1, col5, col1, col7, col8)
    # pattern2 = r'{}\|{}\|{}\|{}\|{}\|{}\|'.format( col1, col2, col3, col1, col5, col1)

    # Abrimos el archivo que contiene la cadena de entrada
    lines = OpenFile('file.txt')

    # Comparamos cada linea con la expresión regular
    for line in lines:
        if (not re.match(pattern, line)):
            error = 'ERROR: Archivo invalido. Formato invalido en la linea:\n\n>> {}\nSaliendo...'.format(
                line)
            sys.exit(error)

    # Si no hubo errores el programa termina con exito
    print('¡Formato correcto! Archivo valido. Saliendo...')


def OpenFile(filename):
    if not os.path.isfile(filename):
        error = 'Archivo {} no existe. Saliendo...'.format(filename)
        sys.exit(error)
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    main()
