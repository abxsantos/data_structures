import pytest

from stacks.stacks import ArrayStack


@pytest.fixture
def stack():
    stack = ArrayStack()
    return stack


class TestStack(object):
    def test_push(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.data == [2, 1]

    def test_pop(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
    
    def test_peek(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
