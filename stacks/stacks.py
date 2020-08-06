class Node (object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = None

    def insert_first(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.first
            self.first = new_node
            self.first.next_node = temp
        self.size += 1
        return self.size

    def remove_last(self):
        if self.first is None:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next_node
        self.size -= 1
        return temp


class ArrayStack(object):
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        if self.data:
            return self.data[0]
        else:
            return None
