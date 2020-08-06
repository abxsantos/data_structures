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
        >>> priority_queue = PriorityQueue()
        >>> priority_queue.add([['Human', 2], ['dog', 2], ['rabbit', 2]])
        >>> priority_queue.data = [['Human', 2], ['dog', 2], ['rabbit', 2]]

        >>> priority_queue.add(["Cat", 1])
        >>> priority_queue.data = [["Cat", 1]['Human', 2], ['dog', 2], ['rabbit', 2]]
        """
        self.data = []

    def enqueue(self):
        """
        Add an item with priority to the queue
        """
        pass

    def dequeue(self):
        """
        Remove an item based on priority
        """
        pass

    def size(self):
        """
        Return number of items in the queue
        """
        pass

    def peek(self):
        """
        Return the first element in the queue
        """
        pass

    def check_if_empty(self):
        """
        Check if the queue is empty or not
        """
        pass

