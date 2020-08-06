"""
Given a linked list and a n value,
return the nth element counting from the last node.
*Do not call the size method of linked list*
*Do not call the tail method of linked list*
"""
import pytest

from linked_lists.singly_linked_lists import SinglyLinkedList


def get_nth_node_value_from_tail(linked_list, n):
    if linked_list.head is None:
        return None
    rabbit = linked_list.head
    turtle = linked_list.head
    index = 0
    while index <= n:
        if rabbit:
            rabbit = rabbit.next_node
            index += 1
        else:
            return None
    while rabbit:
        rabbit = rabbit.next_node
        turtle = turtle.next_node
    return turtle.value


@pytest.fixture
def linked_list():
    linked_list = SinglyLinkedList()
    return linked_list


class TestGetNthElementFromTail(object):

    def test_get_nth_node_value_from_tail(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        n = 1
        assert get_nth_node_value_from_tail(linked_list, n) == 2

    def test_get_nth_node_value_from_tail_if_list_is_none(self, linked_list):
        n = 1
        assert get_nth_node_value_from_tail(linked_list, n) is None

    def test_get_nth_node_value_from_tail_if_n_is_greater_than_list_size(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        n = 10
        assert get_nth_node_value_from_tail(linked_list, n) is None
