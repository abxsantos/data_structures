"""
Based on https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-priority-queue-class
"""
import pytest


class PriorityQueue(object):
    def __init__(self):
        """
        A Priority Queue is a special type of Queue in
        which items may have additional information which
        specifies their priority.

        Item priority will override placement order in
        determining the sequence items are dequeued.
        If an item with a higher priority is enqueued after
        items with lower priority, the higher priority item
        will be dequeued before all the others.

        ex.:
        # >>> priority_queue = PriorityQueue()
        # >>> priority_queue.enqueue([['Human', 2], ['dog', 2], ['rabbit', 2]])
        # >>> priority_queue.data = [['Human', 2], ['dog', 2], ['rabbit', 2]]

        # >>> priority_queue.enqueue(["Cat", 1])
        # >>> priority_queue.data = [["Cat", 1]['Human', 2], ['dog', 2], ['rabbit', 2]]
        """
        self.data = []

    def enqueue(self, item):
        """
        Add an item with priority to the queue
        """
        if not self.data:
            self.data.append(item)
        else:
            position = 0
            for element in self.data:
                if element[1] <= item[1]:
                    position += 1
            self.data.insert(position, item)

    def dequeue(self):
        """
        Remove an item based on priority and first in first out principles.
        """
        if not self.data:
            return None
        else:
            return self.data.pop(0)

    def size(self):
        """
        Return number of items in the queue
        """
        return len(self.data)

    def peek(self):
        """
        Return the first element in the queue
        """
        return self.data[0]

    def check_if_empty(self):
        """
        Check if the queue is empty or not
        """
        if not self.data:
            return True
        return False


@pytest.fixture
def priority_queue():
    priority_queue = PriorityQueue()
    priority_queue.enqueue(['item1', 1])
    priority_queue.enqueue(['item2', 1])
    priority_queue.enqueue(['item3', 2])
    priority_queue.enqueue(['item4', 1])
    priority_queue.enqueue(['item5', 3])
    return priority_queue


class TestPriorityQueue(object):
    def test_enqueue(self, priority_queue):
        """
        Given an item with priority,
        when enqueued is called,
        must add the item in the correct position based on priority
        """
        assert priority_queue.data == [['item1', 1], ['item2', 1], ['item4', 1], ['item3', 2], ['item5', 3]]

    def test_size(self, priority_queue):
        """
        Given a priority queue,
        when size is called,
        must return the number of items in the queue.
        """
        assert len(priority_queue.data) == 5

    def test_dequeue(self, priority_queue):
        """
        Given a priority queue,
        when dequeue is called,
        must return the first added item with highest priority.
        """
        assert priority_queue.dequeue() == ['item1', 1]

    def test_peek(self, priority_queue):
        """
        Given a priority queue,
        when peek is called,
        must return the first item in the queue
        """
        assert priority_queue.peek() == ['item1', 1]

    def test_peek_after_dequeue(self, priority_queue):
        """
        Given a priority queue,
        when peek is called,
        must return the first item in the queue
        """
        priority_queue.dequeue()
        assert priority_queue.peek() == ['item2', 1]

    def test_check_if_empty(self):
        """
        Given a priority queue,
        when check_if_empty is called
        must return False if the queue is not empty otherwise True
        """
        priority_queue = PriorityQueue()
        assert priority_queue.check_if_empty() == True
        priority_queue.enqueue(['item', 1])
        assert priority_queue.check_if_empty() == False