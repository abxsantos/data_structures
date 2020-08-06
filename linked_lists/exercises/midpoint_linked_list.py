import pytest

from linked_lists.singly_linked_lists import SinglyLinkedList

"""
Return the middle node of a linked list.
If the list has a even number of nodes, 
return the node at the end of the first half of the list.
*Do not use a counter variable*
*Do not retrieve the size of the list*
*Iterate only one time through the list* 
"""


def find_midpoint(linked_list):
    turtle = linked_list.head
    rabbit = linked_list.head
    while rabbit.next_node and rabbit.next_node.next_node is not None:
        rabbit = rabbit.next_node.next_node
        turtle = turtle.next_node
    return turtle.value


@pytest.fixture
def linked_list():
    linked_list = SinglyLinkedList()
    return linked_list


class TestMidpoint(object):
    def test_find_midpoint_odd_list(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        assert find_midpoint(linked_list) == 2

    def test_find_midpoint_even_list(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        assert find_midpoint(linked_list) == 3

