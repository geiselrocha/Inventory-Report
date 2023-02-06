from collections.abc import Iterator


class InventoryIterator(Iterator):

    def __init__(self, list):
        self.list = list
        self.index = 0

    def __next__(self):
        result = self.list[self.index]
        if not result:
            raise StopIteration()

        self.index += 1
        return result
