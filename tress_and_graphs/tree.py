import pytest


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add(self, value):
        self.children.append(Node(value))

    def remove(self, value):
        self.children = list(filter(lambda node: node.value != value, self.children))


class Tree(object):
    def __init__(self):
        self.root = None

    def traverse_breadth_first(self):
        pass

    def traverse_depth_first(self):
        pass


@pytest.fixture(scope="function")
def node():
    new_node = Node(1)
    return new_node


@pytest.fixture(scope="function")
def tree():
    new_tree = Tree()
    new_tree.root = Node("a")
    return new_tree


class TestTree(object):
    def test_add_node(self, node):
        node.add(2)
        assert len(node.children) == 1

    def test_remove_node(self, node):
        node.add(2)
        node.remove(2)
        assert node.children == []

    def test_traverse_breadth_first(self, tree):
        tree.root.add("b")
        tree.root.add("d")
        tree.root.children[0].add("c")
        assert tree.traverse_breadth_first() == ["a", "b", "c", "d"]