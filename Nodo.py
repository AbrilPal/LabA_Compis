class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.transitions = {}

    def add_transition(self, value, node):
        if value in self.transitions:
            self.transitions[value].append(node)
        else:
            self.transitions[value] = [node]

    def add_epsilon_transition(self, node):
        self.add_transition('', node)

    def connect_to(self, value, node):
        for child in self.transitions.get(value, []):
            child.add_epsilon_transition(node)

    def connect_to_all(self, node):
        for transition in self.transitions:
            self.connect_to(transition, node)

    def is_leaf(self):
        return self.left is None and self.right is None
