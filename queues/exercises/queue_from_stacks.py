import pytest

from stacks.stacks import ArrayStack


class QueueFromStack(object):
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def add(self, value):
        self.stack1.push(value)

    def remove(self):
        while self.stack1.peek():
            self.stack2.push(self.stack1.pop())
        value = self.stack2.pop()
        while self.stack2.peek():
            self.stack1.push(self.stack2.pop())
        return value

    def peek(self):
        while self.stack1.peek():
            self.stack2.push(self.stack1.pop())
        peek_value = self.stack2.peek()
        while self.stack2.peek():
            self.stack1.push(self.stack2.pop())
        return peek_value


@pytest.fixture
def queue():
    queue = QueueFromStack()
    return queue


class TestQueue(object):

    def test_add(self, queue):
        queue.add(1)
        queue.add(2)
        assert queue.stack1.data == [2, 1]

    def test_remove(self, queue):
        queue.add(1)
        queue.add(2)
        assert queue.remove() == 1
        assert queue.stack1.data == [2]

    def test_peek(self, queue):
        queue.add(1)
        queue.add(2)
        assert queue.peek() == 1
