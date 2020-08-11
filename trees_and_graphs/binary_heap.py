class BinaryHeap(object):
    def __init__(self):
        self.data = []
        self.size = 0

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.data[index] < self.data[index//2]:
                temp = self.data[index//2]
                self.data[index // 2] = self.data[index]
                self.data[index] = temp
            index = index // 2

    def insert(self, item):
        self.data.append(item)
        self.size += 1
        self.percolate_up(self.size)
