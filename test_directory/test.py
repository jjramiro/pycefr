class my_range:
    def __init__(self, start, stop=None, step=1, /):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step
        if step < 0:
            lo, hi, step = stop, start, -step
        else:
            lo, hi = start, stop
        self.length = 0 if lo > hi else ((hi - lo - 1) // step) + 1

    def __iter__(self):
        current = self.start
        if self.step < 0:
            while current > self.stop:
                yield current
                current += self.step
        else:
            while current < self.stop:
                yield current
                current += self.step

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if i < 0:
            i += self.length
        if 0 <= i < self.length:
            return self.start + i * self.step
        raise IndexError('my_range object index out of range')

    def __contains__(self, num):
        if self.step < 0:
            if not (self.stop < num <= self.start):
                return False
        else:
            if not (self.start <= num < self.stop):
                return False
        return (num - self.start) % self.step == 0