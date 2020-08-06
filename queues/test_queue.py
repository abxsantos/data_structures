import pytest

from queues.queues import ArrayQueue


@pytest.fixture
def queue():
    queue = ArrayQueue()
    return queue


class TestQueue(object):
    def test_add_queue(self, queue):
        queue.add(1)
        assert len(queue.data) == 1

    def test_remove_queue(self, queue):
        queue.add(1)
        queue.add(2)
        assert queue.remove() == 1
        assert len(queue.data) == 1

    def test_peek(self, queue):
        """
        Given a queue, when peek is called
        should return the last element
        without altering the array
        """
        queue.add(1)
        queue.add(2)
        assert queue.peek() == 1