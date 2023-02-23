"""
    Andrea Abril Palencia Gutierrez, 18198
    Diseño de Lenguajes de Programacion
    23 de febrero del 2023

    Main:
"""

from Arbol import *
from Infix_a_Postfix import *
from To_afn import *

expresion_regular = input("Ingrese la expresion regular: ")

expresion_postfix = Infix_Postfix(expresion_regular)
tree = construir_arbol(expresion_postfix)
imprimir_arbol(tree, "arbol_sintactico")
afn = construir_AFN_desde_arbol(tree)
print(afn)

g = generar_grafo_AFN(afn)
