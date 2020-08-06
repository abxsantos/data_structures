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
        """
        Return the size of a collection
        """
        if not self.data:
            return 0
        return len(self.data)

    def unite(self, collection):
        """
        Unite the given collection to the existing
        set without any duplicated values
        """
        if not self.data:
            return collection

        united_collection = self.create_temporary_set(self.data)

        values_to_unite = []
        if isinstance(collection, Set):
            values_to_unite = collection.data
        elif isinstance(collection, list):
            values_to_unite = collection
        for item in values_to_unite:
            united_collection.add(item)

        return united_collection

    def create_temporary_set(self, collection):
        temp_collection = Set()
        for value in collection:
            temp_collection.add(value)
        return temp_collection

    def intersection(self, collection):
        """
        Return the intersection of two sets or of a set and a list.
        """
        if not self.data:
            return None

        temp_collection = self.create_temporary_set(self.data)
        intersected_elements = []
        values_to_intersect = []
        if isinstance(collection, Set):
            values_to_intersect = collection.data
        elif isinstance(collection, list):
            values_to_intersect = collection

        for element in values_to_intersect:
            if not temp_collection.add(element):
                intersected_elements.append(element)

        intersected_collection = self.create_temporary_set(intersected_elements)

        return intersected_collection


@pytest.fixture
def set_fixture():
    created_set = Set()
    created_set.add(1)
    return created_set


@pytest.fixture
def second_set_fixture():
    created_set = Set()
    created_set.add(1)
    created_set.add(2)
    created_set.add(3)
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

    def test_unite_with_another_set(self, set_fixture, second_set_fixture):
        """
        Given a set,
        when the unite method
        is called with another set as argument
        it must unite the two collections excluding any duplicates
        """
        assert set_fixture.unite(second_set_fixture).data == [1, 2, 3]

    def test_unite_with_list(self, set_fixture):
        """
        Given a set,
        when the unite method
        is called with a list as argument
        it must unite the two datas excluding any duplicates
        """
        list_to_unite = [1, 2, 3]
        assert set_fixture.unite(list_to_unite).data == [1, 2, 3]

    def test_intersection_with_set(self, set_fixture, second_set_fixture):
        """
        Given a set,
        when the intersection method is called with another set as argument
        it must return a set with the duplicated values.
        """
        assert set_fixture.intersection(second_set_fixture).data == [1]

    def test_intersection_with_list(self, set_fixture):
        """
        Given a set,
        when the intersection method is called with a liist as argument
        it must return a set with the duplicated values.
        """
        list_to_intersect = [1, 2, 3]
        assert set_fixture.intersection(list_to_intersect).data == [1]
