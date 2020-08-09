import pytest

from linked_lists.singly_linked_lists import SinglyLinkedList, Node


def remove_dups(linked_list):
    """
    Remove duplicates from a given linked list without a buffer.
    """
    current = linked_list.head
    while current:
        runner = current
        while runner.next_node:
            if runner.next_node.value == current.value:
                runner.next_node = runner.next_node.next_node
            else:
                runner = runner.next_node
        current = current.next_node


def helper_sum_lists(marker):
    number = ""
    while marker:
        number += str(marker.value)
        marker = marker.next_node
    return int(number[::-1])


def sum_lists(linked_list1, linked_list2):
    """
    Given two lists representing numbers with digits stored in a REVERSED ORDER,
    sum the two numbers and return the sum as a linked list
    """
    number1 = helper_sum_lists(linked_list1.head)
    number2 = helper_sum_lists(linked_list2.head)
    summed_number = [int(n) for n in str(number1 + number2)]
    summed_linked_list = SinglyLinkedList(Node(summed_number[0]))
    for digit in summed_number[1:]:
        summed_linked_list.insert_last(digit)
    return summed_linked_list


def palindrome(linked_list):
    """
    Given a word separated in the values of a linked list, check if palindrome, returning True otherwise False.
    """
    current = linked_list.head
    word = ""
    while current:
        word += current.value.lower()
        current = current.next_node
    if word == word[::-1]:
        return True
    return False


def get_size(linked_list):
    current = linked_list.head
    list_size = 0
    while current:
        current = current.next_node
        list_size += 1
    return list_size


def find_intersection_helper(number_of_asymmetrical_nodes, marker1, marker2):
    trim_index = 0
    while trim_index < number_of_asymmetrical_nodes:
        marker1 = marker1.next_node
        trim_index += 1
    # Now both markers are at the same distance from the intersection point
    while marker1:
        if marker1 == marker2:
            return marker1.value
        else:
            marker1 = marker1.next_node
            marker2 = marker2.next_node


def find_intersection(linked_list1, linked_list2):
    """
    Given two intersecting linked lists, return the intersecting node value.
    """
    size1, size2 = get_size(linked_list1), get_size(linked_list2)
    marker1, marker2 = linked_list1.head, linked_list2.head
    number_of_asymmetrical_nodes = size1 - size2
    if number_of_asymmetrical_nodes > 0:  # ll1 > ll2
        intersecting_node_value = find_intersection_helper(number_of_asymmetrical_nodes, marker1, marker2)
        return intersecting_node_value
    elif number_of_asymmetrical_nodes < 0: # ll1 < ll2
        intersecting_node_value = find_intersection_helper(abs(number_of_asymmetrical_nodes), marker2, marker1)
        return intersecting_node_value


@pytest.fixture(scope="function")
def linked_list():
    linked_list = SinglyLinkedList(Node(1))
    linked_list.insert_last(2)
    linked_list.insert_last(2)
    linked_list.insert_last(3)
    return linked_list


@pytest.fixture(scope="function")
def linked_list1():
    linked_list = SinglyLinkedList(Node(1))
    linked_list.insert_last(2)
    linked_list.insert_last(3)
    linked_list.insert_last(4)
    linked_list.insert_last(5)
    linked_list.insert_last(6)
    return linked_list


@pytest.fixture(scope="function")
def linked_list2():
    linked_list2 = SinglyLinkedList(Node(10))
    linked_list2.insert_last(11)
    linked_list2.insert_last(12)
    return linked_list2


class TestExercises(object):

    def test_remove_dups(self, linked_list):
        remove_dups(linked_list)
        assert linked_list.size() == 3

    def test_sum_lists(self, linked_list):
        linked_list1 = linked_list
        linked_list2 = linked_list
        summed_list = sum_lists(linked_list1, linked_list2)
        assert summed_list.size() == 4

    def test_palindrome(self):
        linked_list = SinglyLinkedList(Node("a"))
        linked_list.insert_last("b")
        linked_list.insert_last("b")
        linked_list.insert_last("a")
        assert palindrome(linked_list) is True

    def test_palindrome_must_return_false(self):
        linked_list = SinglyLinkedList(Node("a"))
        linked_list.insert_last("b")
        linked_list.insert_last("b")
        linked_list.insert_last("c")
        assert palindrome(linked_list) is False

    def test_find_intersection_when_ll1_is_bigger_than_ll2(self, linked_list1, linked_list2):
        linked_list2.get_tail_node().next_node = linked_list1.get_node(3)
        assert find_intersection(linked_list1, linked_list2) == 5

    def test_find_intersection_when_ll1_is_smaller_than_ll2(self, linked_list1, linked_list2):
        linked_list2.get_tail_node().next_node = linked_list1.get_node(3)
        assert find_intersection(linked_list2, linked_list1) == 5
