class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Node[{self.value:^5}]'

class Tree:
    def __init__(self):
        self.root = None

    def new_node(self, value):
        return Node("красный", None, None)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1

t = Tree()
t.root = t.new_node("черный")
t.root.left = t.new_node("красный")
t.root.right = t.new_node("черный")
t.root.left.left = t.new_node("черный")
t.root.left.right = t.new_node("черный")
t.print_level_order(t.root)
print(f'глубина: {t.height(t.root)}')