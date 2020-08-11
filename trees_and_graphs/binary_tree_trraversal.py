import pytest

from trees_and_graphs.binary_tree import BinaryTree


def pre_order_traversal(tree):
    if tree:
        print(tree.get_root_value())
        pre_order_traversal(tree.get_left_child())
        pre_order_traversal(tree.get_right_child())


def post_order_traversal(tree):
    if tree:
        post_order_traversal(tree.get_left_child())
        post_order_traversal(tree.get_right_child())
        print(tree.get_root_value())


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)

pre_order_traversal(tree)
post_order_traversal(tree)