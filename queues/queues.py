class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self.size

    def dequeue(self):
        if self.first is None:
            return None
        if self.first == self.last:
            self.first = None
        else:
            self.first = self.first.next
            self.last -= 1
        return self.first


class ArrayQueue(object):
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.insert(0, value)

    def remove(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
