"""
    Andrea Abril Palencia Gutierrez, 18198
    Diseño de Lenguajes de Programacion
    23 de febrero del 2023

    Convertir de INFIX a POSTFIX: usa como parametro una cadena ya
    formateada y devolver una cadena POSTFIX para luego contruir el
    arbol.
"""
from Stack import *
from Formatear_Expresion import Formatear

def getPrecedence(caracter):
    if(caracter == '(' or caracter == ')'):
        return 1
    elif(caracter == '|'):
        return 2
    elif(caracter == '.'):
        return 3
    elif(caracter == '?' or caracter == '*' or caracter == '+'):
        return 4
    elif(caracter == '^'):
        return 5
    else:
        return 6

def Infix_Postfix(expresion_re):
    postfix = []
    stack = Stack()
    expresion_form = Formatear(expresion_re)

    for c in expresion_form:
        # print(c, " esta es c\n")
        if c == '(':
            stack.push(c)
            break
        if c == ')':
            while stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
            break

        while stack.is_empty() != True:
            peekedChar = stack.peek()
            peekedCharPrece = getPrecedence(peekedChar)
            currentCharPrece = getPrecedence(c)

            if peekedCharPrece >= currentCharPrece:
                postfix.append(stack.pop())
            else:
                break
        
        stack.push(c)
    
    while stack.is_empty() != True:
        postfix.append(stack.pop())

    postfixFinal = ''.join(postfix)
    print("La expresion POSTFIX es: ", postfixFinal, "\n")
    return postfixFinal

Infix_Postfix("ab*ab*")
