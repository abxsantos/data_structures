"""
tree = [
["a"],        # root
[[], []],     # child1
[[], [], []]  # child 2
]
"""


def binary_tree(root):
    return [root, [], []]


def insert_left(root, new_branch):
    tree = root.pop(1)
    if len(tree) > 1:
        root.insert(1, [new_branch, tree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    tree = root.pop(2)
    if len(tree) > 1:
        root.insert(2, [new_branch, [], tree])
    else:
        root.insert(2,[new_branch, [], []])
    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root(1)


def get_right_child(root):
    return root[2]


"""
root = binary_tree(3)
insert_left(root, 4)
insert_left(root, 5)
insert_right(root, 6)
insert_right(root, 7)
left = get_left_child(root)
set_root_value(left, 9)
"""