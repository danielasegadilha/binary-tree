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

    def is_simetric(self, root_left, root_right):
        if root_left is not None and root_right is not None:
            left_side = self.is_simetric(root_left.left, root_right.left)
            right_side = self.is_simetric(root_left.right, root_right.right)
            return left_side and right_side
        elif root_left is None and root_right is None:
            return True
        else:
            return False

    def get_height(self, root):
        if root.left is not None or root.right is not None:
            if root.left is not None and root.right is not None:
                left_height = 1 + self.get_height(root.left)
                right_height = 1 + self.get_height(root.right)
            elif root.left is None:
                right_height = 1 + self.get_height(root.right)
                left_height = 0
            else:
                left_height = 1 + self.get_height(root.left)
                right_height = 0
            if left_height > right_height:
                return left_height
            else:
                return right_height
        else:
            return 0

    def is_balanced(self, root):
        if root.left is not None and root.right is not None:
            if abs(self.get_height(root.left) - self.get_height(root.right)) <= 1:
                left_side = self.is_balanced(root.left)
                right_side = self.is_balanced(root.right)
                return left_side and right_side
            else:
                return False
        elif root.left is None and root.right is None:
            return True
        elif root.left is None:
            if self.get_height(root.right) - 0 <= 1:
                return True
            else:
                return False
        elif root.right is None:
            if self.get_height(root.left) - 0 <= 1:
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
