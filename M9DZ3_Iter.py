class EvenNumbers:
    def __init__(self, a, b):
        self.start = a
        self.end = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 2
            return self.start
en = EvenNumbers
for i in en(10, 25):
    print(i-2)
