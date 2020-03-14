class ThreeStack1:
    def __init__(self, l1, l2, l3):
        self.stack = [l1, l2, l3]

class ThreeStack2:
    def __init__(self, l1, l2, l3)
        self.stack = [0] * (10 ** 8)
        self.l1_st = 0
        self.l2_st = len(self.stack) // 3
        self.l3_st = len(self.stack) // 3 * 2
        for l, st in zip([l1, l2, l3], [self.l1_st, self.l2_st, self.l3_st]):
            for i in range(l):
                self.stack[st+i] = l[i]

# TODO movable version
                



