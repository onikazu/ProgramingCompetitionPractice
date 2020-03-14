# don't think too difficult!!

class MinStack:
    def __init__(self, l):
        self.data = l
        self.min_data = []
        self.min = float("inf")
        for v in self.data:
            if v < self.min:
                self.min_data.append(v)
                self.min = v
            else:
                self.min_data.append(self.min)

    def push(self, v):
        if v < self.min_data[-1]:
            self.min_data.append(v)
        else:
            self.min_data.append(self.min_data[-1])
        self.data.append(v)

    def pop(self):
        self.data.pop()
        self.min_data.pop()

    def get_min(self):
        return self.min_data[-1]


if __name__ == "__main__":
    min_stack = MinStack([1, 2, 3, 4, 5, -10, 15])
    print(min_stack.get_min())
    print(min_stack.pop())
    print(min_stack.pop())
    print(min_stack.get_min())
