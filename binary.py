# Definition of a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Function to calculate height of the tree
def height(root):
    if root is None:
        return -1  # Height of empty tree

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


# Main program
if __name__ == "__main__":
    # Creating the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder Traversal:")
    inorder(root)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nPostorder Traversal:")
    postorder(root)

    print("\nHeight of the tree:", height(root))
