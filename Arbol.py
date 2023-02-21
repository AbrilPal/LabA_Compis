"""
    Andrea Abril Palencia Gutierrez, 18198
    Diseño de Lenguajes de Programacion
    23 de febrero del 2023

    Arbol: crea el arbol sintactico a partir de la expresion POSTFIX
    para luego este ser utilizado para la creacion del AFN.
"""

from binarytree import build
from Stack import *
from Infix_a_Postfix import Infix_Postfix

def Arbol_sintactico(expresion_reg):
    operadoresPar = ['|', '.']
    operadoresIndividual = ['+', '|', '*']
    
    return None

    # if (cadenaAl.peek() in operadoresPar) or (cadenaAl.peek() in operadoresIndividual):
    #     root = Node(cadenaAl.pop())
    #     if (cadenaAl.peek() )

    
expresion_postfix = Infix_Postfix("(a*|b*)c")
print(Arbol_sintactico(expresion_postfix))