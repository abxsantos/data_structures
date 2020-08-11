import pytest


class BinaryTree(object):

    def __init__(self, root=None):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, node):
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, value):
        new_root = BinaryTree(value)
        new_root.left_child = self.left_child
        new_root.right_child = self.right_child
        self.key = new_root

    def get_root_value(self):
        return self.key


@pytest.fixture(scope="function")
def tree():
    tree = BinaryTree(1)
    return tree


@pytest.fixture(scope="function")
def tree_with_leaves():
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    return tree


class TestBinaryTree(object):

    def test_root(self, tree):
        assert tree.key == 1

    def test_insert_left(self, tree):
        tree.insert_left(2)
        assert tree.left_child.key == 2
        assert tree.right_child is None

    def test_insert_right(self, tree):
        tree.insert_right(3)
        assert tree.right_child.key == 3
        assert tree.left_child is None

    def test_get_right_child(self, tree_with_leaves):
        assert tree_with_leaves.get_right_child().key == 3

    def test_get_left_child(self, tree_with_leaves):
        assert tree_with_leaves.get_left_child().key == 2
