from tree import drawTree


class TreeItem:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, root, item):
        if root is None:
            return
        elif root.value > item.value:
            if root.left is None:
                root.left = item
            else:
                self.insert(root.left, item)
        elif root.value < item.value:
            if root.right is None:
                root.right = item
            else:
                self.insert(root.right, item)

    def is_simetric(self, root):
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        else:
            if self.is_simetric(root.left) == self.is_simetric(root.right):
                return True
            else:
                return False


tree_1 = TreeItem(10)
tree_2 = TreeItem(10)

for tree_key in [20, 5, 3, 8, 18, 30, 40, 9]:
    item_tree = TreeItem(value=tree_key)
    tree_1.insert(tree_1, item_tree)


for tree_key in [20, 40, 30, 60, 50]:
    item_tree = TreeItem(value=tree_key)
    tree_2.insert(tree_2, item_tree)


def is_identical(tree1, tree2) -> bool:
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is not None and tree2 is not None:
        if tree1.value == tree2.value:
            left_equal = is_identical(tree1.left, tree2.left)
            right_equal = is_identical(tree1.right, tree2.right)
            return left_equal and right_equal
        else:
            return False
    else:
        return False


drawTree(tree_1)

if is_identical(tree_1, tree_2):
    print(f'são iguais')
else:
    print(f'não são iguais')

if tree_1.is_simetric(tree_1):
    print(f"é simetrico")
else:
    print(f"não é")
