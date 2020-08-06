"""
Based on
https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-set-class
"""
import pytest


class Set(object):
    """
    A set is like an array, but it cannot contain duplicate values.
    The typical use for a set is to simply check for the presence of an item.
    """
    def __init__(self):
        self.data = []

    def add(self, value):
        """
        Check if the given value exists in the set. If it does, return False
        otherwise add the value to the set and return True.
        """
        if not self.data:
            self.data.append(value)
            return True
        for element in self.data:
            if element == value:
                return False
        self.data.append(value)
        return True

    def remove(self, value):
        """
        Check if the given value exists in the set.
        If it does remove it and return True. Otherwise return False
        """
        if not self.data:
            return False
        for element in self.data:
            if element == value:
                self.data.remove(value)
                return True
        return False

    def size(self):
        if not self.data:
            return 0
        return len(self.data)


@pytest.fixture
def set_fixture():
    created_set = Set()
    created_set.add(1)
    return created_set


class TestSet(object):
    def test_add(self, set_fixture):
        """
        Given a value,
        when add is called,
        must return True and add the
        value to the set if it doesn't already exists
        """
        assert set_fixture.add(1) is False
        assert set_fixture.add(2) is True

    def test_remove(self, set_fixture):
        """
        Given a value,
        when remove is called,
        must return True and remove if the value is in the set data, otherwise False
        """
        assert set_fixture.remove(2) is False
        assert set_fixture.remove(1) is True

    def test_size(self, set_fixture):
        """
        Given a set,
        when size is called,
        must return the size of the set
        """
        assert set_fixture.size() == 1
        set_fixture.add(2)
        assert set_fixture.size() == 2
        set_fixture.remove(1)
        assert set_fixture.size() == 1
