class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_syntax_tree(postfix):
    stack = []
    for symbol in postfix:
        if symbol in '|?+*^':
            right = stack.pop()
            left = stack.pop()
            node = Node(symbol, left, right)
            stack.append(node)
        else:
            node = Node(symbol)
            stack.append(node)
    return stack.pop()

def print_syntax_tree(node, indent=0):
    if node is None:
        return
    print(' ' * indent + str(node.value))
    if node.left:
        print_syntax_tree(node.left, indent+4)
    if node.right:
        print_syntax_tree(node.right, indent+4)

# Ejemplo de uso
postfix = '0?1??0*.'
root = build_syntax_tree(postfix)
print_syntax_tree(root)
