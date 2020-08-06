import pytest

from linked_lists.singly_linked_lists import SinglyLinkedList

"""
Given a linked list,
return true if the list is circular or false if not.
"""


def check_circular_first_option(linked_list):
    """
    Given a linked list, must check if it's circular or not.
    :param linked_list:
    :return bool: True or False
    """
    if linked_list.head is None:
        return False
    marker = linked_list.head.next_node
    while marker:
        marker = marker.next_node
        if marker == linked_list.head:
            return True
    return False


def check_circular_second_option(linked_list):
    """
    Given a linked list, must check if it's circular or not.
    :param linked_list:
    :return bool: True or False
    """
    if linked_list.head is None:
        return False
    rabbit = linked_list.head
    turtle = linked_list.head
    while rabbit.next_node and rabbit.next_node.next_node:
        rabbit = rabbit.next_node.next_node
        turtle = turtle.next_node
        if turtle == rabbit:
            return True
    return False


@pytest.fixture(scope="function")
def linked_list():
    linked_list = SinglyLinkedList()
    return linked_list


class TestCircularFirstOptionCheck(object):
    def test_circular_when_list_is_not_circular(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        assert check_circular_first_option(linked_list) is False

    def test_circular_when_list_is_circular(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        linked_list.get_tail_node().next_node = linked_list.head
        assert check_circular_first_option(linked_list) is True

    def test_circular_when_list_has_one_node(self, linked_list):
        linked_list.insert_first(1)
        assert check_circular_first_option(linked_list) is False

    def test_circular_when_list_has_no_nodes(self, linked_list):
        assert check_circular_first_option(linked_list) is False


class TestCircularSecondOptionCheck(object):
    def test_circular_when_list_is_not_circular(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        assert check_circular_second_option(linked_list) is False

    def test_circular_when_list_is_circular(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        linked_list.get_tail_node().next_node = linked_list.head
        assert check_circular_second_option(linked_list) is True

    def test_circular_when_list_has_one_node(self, linked_list):
        linked_list.insert_first(1)
        assert check_circular_second_option(linked_list) is False

    def test_circular_when_list_has_no_nodes(self, linked_list):
        assert check_circular_second_option(linked_list) is False