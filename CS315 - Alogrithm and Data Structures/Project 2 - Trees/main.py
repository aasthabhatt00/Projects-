# Author: Aastha Bhatt
# CS315 - Programming Assignment 2

# Class for BST nodes representation
class newNode:
    def __init__(self, item):
        self.parent = None
        self.left = None
        self.right = None
        self.key = item


# Creates array from a given file with 1 column of data
def CREATE_ARRAY(filename):
    file = open(filename, "r")
    lines = file.readlines()
    power_list = []

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        lines[i] = int(lines[i])
        power_list.append(lines[i])
    return power_list


# Inserts a new node into the BST
def TREE_INSERT(node, key):
    if node is None:
        return newNode(key)

    if node.key > key:
        left_child = TREE_INSERT(node.left, key)
        node.left = left_child
        left_child.parent = node

    elif node.key < key:
        right_child = TREE_INSERT(node.right, key)
        node.right = right_child
        right_child.parent = node

    return node


# Searches for value in BST's node's keys and returns the node if found else returns None
def TREE_SEARCH(root, value):
    if root is None or root.key == value:
        return root

    if root.key < value:
        return TREE_SEARCH(root.right, value)

    return TREE_SEARCH(root.left, value)


# Returns node with the minimum value in the BST
def TREE_MINIMUM(root):
    while root.left is not None:
        root = root.left
    return root


# Returns node with the maximum value in the BST
def TREE_MAXIMUM(root):
    while root.right is not None:
        root = root.right
    return root


# Overwrites BST 'u' with BST 'v'
def TRANSPLANT(root, u, v):
    if u.parent is None:
        root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent


# Deletes a node holding a given value as key if found (return True if successful, false otherwise)
def TREE_DELETE(root, value):
    node = TREE_SEARCH(root, value)
    if node is None:
        return False
    else:
        if node.left is None:
            TRANSPLANT(root, node, node.right)
        elif node.right is None:
            TRANSPLANT(root, node, node.left)
        else:
            y = TREE_MINIMUM(node.right)
            if y.parent is not node:
                TRANSPLANT(root, y, y.right)
                y.right = node.right
                y.right.parent = y
            TRANSPLANT(root, node, y)
            y.left = node.left
            y.left.parent = y
        return True


# Function that prints the tree in preorder traversal
def PREORDER_TREE_WALK(root):
    if root:
        print(root.key, end=" ")
        PREORDER_TREE_WALK(root.left)
        PREORDER_TREE_WALK(root.right)


# Function that prints the tree in postorder traversal
def POSTORDER_TREE_WALK(root):
    if root:
        POSTORDER_TREE_WALK(root.left)
        POSTORDER_TREE_WALK(root.right)
        print(root.key, end=" ")


# Function that prints the tree in inorder traversal
def INORDER_TREE_WALK(root):
    if root:
        INORDER_TREE_WALK(root.left)
        print(root.key, end=" ")
        INORDER_TREE_WALK(root.right)


# Function that makes a corresponding BST for a given array
def CREATE_BST(array):
    root = newNode(array[0])
    for j in range(1, len(array)):
        root = TREE_INSERT(root, array[j])
    return root


# Convert the csv into arrays and then into BSTs
BST1 = CREATE_BST(CREATE_ARRAY("test1.csv"))
BST2 = CREATE_BST(CREATE_ARRAY("test2.csv"))
BST3 = CREATE_BST(CREATE_ARRAY("test3.csv"))

print("Testing TREE_INSERT() by printing preorder traversal of BST1, BST2, and BST3:")
PREORDER_TREE_WALK(BST1)
print()
PREORDER_TREE_WALK(BST2)
print()
PREORDER_TREE_WALK(BST3)
print()

print("\nTesting, TREE_SEARCH(), TREE_MAXIMUM(), and TREE_MINIMUM() methods:")
print(f"When searching for '128' in the tree resulting from 'test3.csv' the node {TREE_SEARCH(BST1, 0)} is returned"
      f" and when searching for -1 and 129 (values that do not exist) {TREE_SEARCH(BST1, -1)} and"
      f" {TREE_SEARCH(BST3, 129)} is returned respectively.")
print(f"The value of key for nodes that hold the maximum in 'test1.csv', 'test2.csv', and 'test3.csv' are {TREE_MAXIMUM(BST1).key}, {TREE_MAXIMUM(BST2).key}, "
      f"and {TREE_MAXIMUM(BST3).key} respectively.")
print(f"The value of key for nodes that hold the minimum in 'test1.csv', 'test2.csv', and 'test3.csv' are {TREE_MINIMUM(BST1).key}, {TREE_MINIMUM(BST2).key}, "
      f"and {TREE_MINIMUM(BST3).key} respectively.")
print()



# Preorder, postorder, and inorder traversals of BST3
print("\nTesting tree traversal methods:")
print("PREORDER traversal of BST3:", end=" ")
PREORDER_TREE_WALK(BST3)
print()

print("POSTORDER traversal of BST3:", end=" ")
POSTORDER_TREE_WALK(BST3)
print()

print("INORDER traversal of BST3:", end=" ")
INORDER_TREE_WALK(BST3)
print()


# Testing TREE_DELETE() method on BST3
print("\nTesting TREE_DELETE() method on BST3:")
print("Original BST3:", end=" ")
PREORDER_TREE_WALK(BST3)
print()

print("Preorder Traversal of BST3 after deleting 6:", end=" ")
TREE_DELETE(BST3, 6)
PREORDER_TREE_WALK(BST3)
print()

print("Preorder Traversal of BST3 after deleting 37:", end=" ")
TREE_DELETE(BST3, 37)
PREORDER_TREE_WALK(BST3)
print()

print("Preorder Traversal of BST3 after deleting 77:", end=" ")
TREE_DELETE(BST3, 77)
PREORDER_TREE_WALK(BST3)
print()
