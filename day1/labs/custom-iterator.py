class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

iterator = MyIterator(1, 5)

for value in iterator:
    print(value)  # Output: 1, 2, 3, 4, 5
