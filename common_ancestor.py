def main():
    while True:
        print("Find the first common ancestor of two nodes in a binary tree")
        i = input("Enter integers to make a tree, separated by spaces: ").split(" ")
        vals = [int(x) for x in i]

def contains(root, node):
    if root is None or node is None: return False
    if root == node: return True
    return contains(root.left, node) or contains(root.right, node)

def fca_h(root, node1, node2):
    if root is None: return None
    if root == node1 or root == node2: return root
    node1_left = contains(root.left, node1)
    node2_left = contains(root.left, node2)

    if node1_left != node2_left: return root
    child_side = node1_left ? root.left : root.right
    fca_h(child_side, node1, node2)

def fca(T, node1, node2):
    if not (contains(T.root, n1) or contains(T.root, n2)): return None
    return fca_h(T.root, node1, node2)

# Not a bst, and not balanced
class Tree(object):
    def __init__(self, root=None):
        self.root = root

    # Start at the root. If it's missing a child, insert there.
    # Otherwise, call insert randomly on its left or right child
    def insert(self, val):
        child = Node(val)
        if self.root is None:
            self.root =
        else:

    def insert_h(self, subroot, val):


class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




























if __name__ == "__main__": main()