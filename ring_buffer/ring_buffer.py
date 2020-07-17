class RingBuffer:
    def __init__(self, capacity, data=[]):
        self.capacity = capacity
        self.index = 0
        self.array = list(data)[-capacity:]

    def append(self, item):
        if (len(self.array) == self.capacity):
            self.array[self.index] = item
        else:
            self.array.append(item)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.array
