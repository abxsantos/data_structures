class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, data):
        """
        creates a new Node from data
        and assigns the Node to the
        head property.
        :param data: Object
        :return new_head: New head node
        """
        self.head = Node(data, self.head)

    def size(self):
        list_size = 0
        current = self.head
        while current:
            current = current.next_node
            list_size += 1
        return list_size

    def get_head_node(self):
        return self.head

    def get_tail_node(self):
        if self.head is None:
            return None
        current = self.head
        while current.next_node:
            current = current.next_node
        return current

    def clear(self):
        self.head = None

    def remove_head(self):
        if self.head.next_node:
            self.head = self.head.next_node
        else:
            self.head = None

    def remove_tail(self):
        previous = self.head
        current = self.head.next_node
        while current.next_node:
            previous = current
            current = current.next_node
        previous.next_node = None

    def insert_last(self, data):
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

    def get_node(self, index):
        i = 0
        current = self.head
        while i <= index:
            current = current.next_node
            i += 1
        return current

    def insert_at(self,data,index):
        previous = self.get_node(index - 1)
        node = Node(data, previous.next_node)
        previous.next_node = node

    def remove_at(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next_node
            return
        previous = self.get_node(index - 1)
        if previous.next_node:
            previous.next_node = previous.next_node.next_node
        else:
            return
