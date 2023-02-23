from Nodo import *
from Infix_a_Postfix import Infix_Postfix
import graphviz

class Estado:
    contador_ids = 0
    def __init__(self):
        self.id = Estado.contador_ids
        Estado.contador_ids += 1
        self.transiciones = {}
        self.epsilon_transiciones = set()

    def add_transition(self, simbolo, estado):
        if simbolo in self.transiciones:
            self.transiciones[simbolo].add(estado)
        else:
            self.transiciones[simbolo] = {estado}

    def add_epsilon_transition(self, estado):
        self.epsilon_transiciones.add(estado)

    def get_transitions(self, simbolo):
        return self.transiciones.get(simbolo, set())

    def get_epsilon_transitions(self):
        return self.epsilon_transiciones

    def __str__(self):
        return f"{self.id}"

class AFN:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def match(self, cadena):
        estados_actuales = {self.inicial}
        for simbolo in cadena:
            nuevos_estados = set()
            for estado in estados_actuales:
                nuevos_estados |= estado.get_transitions(simbolo)
                nuevos_estados |= estado.get_epsilon_transitions()
            estados_actuales = nuevos_estados
        return self.final in estados_actuales

    def __str__(self):
        visitados = set()
        nodos = [self.inicial]
        nodos_finales = {self.final}
        transiciones = []

        print("transiciones:\n")
        
        while nodos:
            nodo = nodos.pop()
            visitados.add(nodo)
            
            if nodo in nodos_finales:
                marca = '*'
            else:
                marca = ''
            
            for simbolo, estados_destino in nodo.transiciones.items():
                for estado_destino in estados_destino:
                    transiciones.append((nodo, estado_destino, simbolo))
                    if estado_destino not in visitados:
                        nodos.append(estado_destino)
            
            for estado_destino in nodo.epsilon_transiciones:
                transiciones.append((nodo, estado_destino, 'ε'))
                if estado_destino not in visitados:
                    nodos.append(estado_destino)
        
        estados_str = [f'{str(e)}{marca}' for e in visitados]
        transiciones_str = [f'{str(e1)} --{s}--> {str(e2)}' for e1, e2, s in transiciones]
        
        return '\n'.join(transiciones_str)

def construir_AFN_desde_arbol(nodo):
    if nodo.value == '.':
        afn1 = construir_AFN_desde_arbol(nodo.left)
        afn2 = construir_AFN_desde_arbol(nodo.right)
        afn1.final.add_epsilon_transition(afn2.inicial)
        afn1.final = afn2.final
        return afn1
    elif nodo.value == '|':
        afn1 = construir_AFN_desde_arbol(nodo.left)
        afn2 = construir_AFN_desde_arbol(nodo.right)
        inicial = Estado()
        inicial.add_epsilon_transition(afn1.inicial)
        inicial.add_epsilon_transition(afn2.inicial)
        final = Estado()
        afn1.final.add_epsilon_transition(final)
        afn2.final.add_epsilon_transition(final)
        return AFN(inicial, final)
    elif nodo.value == '*':
        afn = construir_AFN_desde_arbol(nodo.left)
        inicial = Estado()
        final = Estado()
        inicial.add_epsilon_transition(afn.inicial)
        inicial.add_epsilon_transition(final)
        afn.final.add_epsilon_transition(afn.inicial)
        afn.final.add_epsilon_transition(final)
        return AFN(inicial, final)
    elif nodo.value == '+':
        afn = construir_AFN_desde_arbol(nodo.left)
        inicial = Estado()
        final = Estado()
        inicial.add_epsilon_transition(afn.inicial)
        afn.final.add_epsilon_transition(afn.inicial)
        afn.final.add_epsilon_transition(final)
        return AFN(inicial, final)
    elif nodo.value == '?':
        afn = construir_AFN_desde_arbol(nodo.left)
        inicial = Estado()
        final = Estado()
        inicial.add_epsilon_transition(afn.inicial)
        inicial.add_epsilon_transition(final)
        afn.final.add_epsilon_transition(final)
        return AFN(inicial, final)
    else:
        estado_inicial = Estado()
        estado_final = Estado()
        estado_inicial.add_transition(nodo.value, estado_final)
        return AFN(estado_inicial, estado_final)