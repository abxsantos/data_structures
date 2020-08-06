import pytest
from linked_lists.singly_linked_lists import SinglyLinkedList


@pytest.fixture(scope='function')
def linked_list():
    linked_list = SinglyLinkedList()
    return linked_list


class TestSinglyLinkedList:
    def test_insert_node_must_insert_a_new_node(self, linked_list):
        linked_list.insert_first(1)
        assert linked_list.head.value == 1

    def test_insert_node_must_link_with_previous_head(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        assert linked_list.head.value == 2
        assert linked_list.head.next_node.value == 1

    def test_size_must_count_correct_number_of_nodes(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        linked_list.insert_first(1)

        assert linked_list.size() == 3

    def test_get_head_node_must_return_the_head(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        head = linked_list.get_head_node()
        assert head.value == 2

    def test_get_tail_node_must_return_the_last_node(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        tail = linked_list.get_tail_node()
        assert tail.value == 1

    def test_get_tail_node_must_return_None_when_list_is_empty(self, linked_list):
        tail = linked_list.get_tail_node()
        assert tail is None

    def test_clear_must_clear_all_nodes(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.clear()
        assert linked_list.head is None

    def test_remove_head_node(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.remove_head()
        assert linked_list.head.value == 1

    def test_remove_head_node_must_return_None_if_only_head(self, linked_list):
        linked_list.insert_first(2)
        linked_list.remove_head()
        assert linked_list.head is None

    def test_remove_tail(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.remove_tail()
        assert linked_list.get_tail_node().value == 2

    def test_insert_last(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_last(4)
        assert linked_list.get_tail_node().value == 4

    def test_get_node(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        assert linked_list.get_node(1).value == 2

    def test_insert_at(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        linked_list.insert_at(10, 2)
        assert linked_list.get_node(2).value == 10

    def test_remove_at(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        linked_list.remove_at(1)
        assert linked_list.get_node(1).value == 1
