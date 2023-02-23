from collections import deque

class State:
    def __init__(self, id):
        print(id)
        self.id = id
        self.transitions = {}

    def add_transition(self, label, state):
        print(label, " label ", state)
        if label in self.transitions:
            self.transitions[label].append(state)
        else:
            self.transitions[label] = [state]
    
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

class NFA:
    def __init__(self, start_state, states, final_states, alphabet):
        self.start_state = start_state
        self.states = states
        self.final_states = final_states
        self.alphabet = alphabet

def construir_AFN(root):
    # Generar identificadores únicos para los estados
    state_id = 0
    def generate_id():
        nonlocal state_id
        state_id += 1
        return state_id

    # Recorrer el árbol y crear los estados correspondientes
    def build_states(node):
        if node is None:
            return None
        state = State(generate_id())
        if node.value in ['*', '+', '?']:
            child = build_states(node.left)
            state.add_transition("ε", child)
            if node.value in ['*', '+']:
                state.add_transition("ε", State(generate_id()))
        elif node.value == '.':
            left = build_states(node.left)
            right = build_states(node.right)
            left.add_transition("ε", right)
            state = left
        elif node.value == '|':
            left = build_states(node.left)
            right = build_states(node.right)
            start = State(generate_id())
            start.add_transition("ε", left)
            start.add_transition("ε", right)
            state = start
        else:
            state.add_transition(node.value, State(generate_id()))
        if node.left is None and node.right is None:
            state.is_final = True
        return state

    # Llamar a la función para construir los estados
    start = State(generate_id())
    final = build_states(root)
    states = {start}
    queue = deque([start])
    while queue:
        current_state = queue.popleft()
        for label in current_state.transitions:
            for state in current_state.transitions[label]:
                if state not in states:
                    states.add(state)
                    queue.append(state)

    # Obtener el alfabeto del AFN
    alphabet = set()
    for state in states:
        for label in state.transitions:
            if label is not None:
                alphabet.add(label)

    # Crear el objeto NFA y retornarlo
    return NFA(start, states, {final}, alphabet)
