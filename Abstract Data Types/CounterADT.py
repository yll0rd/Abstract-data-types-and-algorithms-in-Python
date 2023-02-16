class Counter:
    def __init__(self,num):
        self.num = num

    def inc(self):
        return self.num + 1

    def dec(self):
        return self.num - 1

    def reset(self):
        self.num = 0