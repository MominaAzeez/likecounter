class UpCounter(UpDownCounter):
    def __init__(self, start=0, step=1):
        super().__init__(start)
        self.step = step

    def advance(self):
        self.current += self.step
        return self.current
