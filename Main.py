"""
    Andrea Abril Palencia Gutierrez, 18198
    Diseño de Lenguajes de Programacion
    23 de febrero del 2023

    Main: programa principal que manda a llamar las funciones
    de los otros archivos.
"""

from Arbol import *
from Infix_a_Postfix import *
from To_afn import *
import sys

abiertos = 0
cerrados = 0

# EXPRESION REGULAR
expresion_regular = input("Ingrese la expresion regular: ")
for caracter in expresion_regular:
    if caracter == "(":
        abiertos += 1
    elif caracter == ")":
        cerrados += 1
if (abiertos > cerrados) or (abiertos < cerrados):
    print("\nERROR: Verifique los paréntesis, ya que hay", abiertos,  "paréntesis abiertos y", cerrados, "paréntesis cerrados.")
    sys.exit()
else:
    expresion_regular_nuevo = expresion_regular.replace(".", "$")

    # POSTFIX
    expresion_postfix = Infix_Postfix(expresion_regular_nuevo)

    # ARBOL SINTACTICO
    tree = construir_arbol(expresion_postfix)
    imprimir_arbol(tree, "arbol_sintactico")

    # AFN
    afn = construir_AFN_desde_arbol(tree)
    print(afn)
    g = generar_grafo_AFN(afn)
