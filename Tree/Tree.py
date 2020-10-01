# #
# A tree data structure can be defined recursively as a collection of nodes (starting at a root node).
# where each node is a data structure consisting of a value, together with a list of references to nodes
# (the "children"), with the constraints that no reference is duplicated, and none points to the root.
# Ref.: https://en.wikipedia.org/wiki/Tree_(data_structure)
#
# Traversal is a process to visit all the nodes of a tree and may print their values too.
# Because, all nodes are connected via edges (links) we always start from the root (head) node.
# That is, we cannot randomly access a node in a tree.
# There are three ways which we use to traverse a tree − In-order Traversal; Pre-order Traversal ;Post-order Traversal
# Ref.: https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
# #

def main():
    tree = Tree()

    tree.add(27)
    tree.add(14)
    tree.add(35)
    tree.add(10)
    tree.add(19)
    tree.add(31)
    tree.add(42)

    print("INORDER:", end=' ')
    tree.show_inorder(tree.root)
    print()

    print("PREORDER:", end=' ')
    tree.show_preorder(tree.root)
    print()

    print("POSTORDER:", end=' ')
    tree.show_postorder(tree.root)
    print()

    for valeu in [10, 1, 27, 2, 35, 31, 42, 14, 15]:
        print(f'SEARCH: {valeu} ->', end=' ')
        print(f'NOT FOUND!' if tree.search(valeu) is None else 'FOUND!')


class Node:

    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def insert_child(self, value):
        if(value <= self.value):
            if(self.left is None):
                self.left = Node(value)
            else:
                self.left.insert_child(value)
        else:
            if(self.right is None):
                self.right = Node(value)
            else:
                self.right.insert_child(value)

    def find_value(self, value):
        if(value == self.value):
            return self.value

        if(value <= self.value):
            if(not(self.left is None)):
                return self.left.find_value(value)
        else:
            if(not(self.right is None)):
                return self.right.find_value(value)

        return None


class Tree:

    def __init__(self):
        self.root = None

    def add(self, value):
        if(self.root is None):
            self.root = Node(value)
        else:
            self.root.insert_child(value)

    def search(self, value):
        return self.root.find_value(value)

    def show_inorder(self, origin):
        if(origin is None):
            return

        self.show_inorder(origin.left)
        print(origin.value, end=' ')
        self.show_inorder(origin.right)

    def show_postorder(self, origin):
        if(origin is None):
            return

        self.show_postorder(origin.left)
        self.show_postorder(origin.right)
        print(origin.value, end=' ')

    def show_preorder(self, origin):
        if(origin is None):
            return

        print(origin.value, end=' ')
        self.show_preorder(origin.left)
        self.show_preorder(origin.right)


main()
