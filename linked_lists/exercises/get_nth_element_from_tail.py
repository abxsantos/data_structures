"""
Given a linked list and a n value,
return the nth element counting from the last node.
*Do not call the size method of linked list*
"""
import pytest
from linked_lists.singly_linked_lists import SinglyLinkedList


def get_nth_element_from_tail(linked_list, n):
    pass


@pytest.fixture
def linked_list():
    linked_list = SinglyLinkedList()
    return linked_list


class TestGetNthElementFromTail(object):

    def test_get_nth_element_from_tail(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        n = 1
        assert get_nth_element_from_tail(linked_list, n) == 2

    def test_get_nth_element_from_tail_if_list_is_None(self, linked_list):
        n = 1
        assert get_nth_element_from_tail(linked_list, n) == None

    def test_get_nth_element_from_tail_if_n_is_greater_than_list_size(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        n = 10
        assert get_nth_element_from_tail(linked_list, n) == None