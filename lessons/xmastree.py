class xmastree:

    plots: list[int]

    def __init__ (self, plots: int, initalplanting: int):
        self.plots = []
        a: int = 0
        while a < plots:
            if a <= initalplanting:
                self.plots.append(1)
            else:
                self.plots.append(0)
    

    def plant (self, index: int):
        self.plots[index] = 1
    
    def growth(self):
        for index in self.plots:
            if self.plots[index] != 0:
                self.plots[index] += 1

    def harvest (self, replant: bool):
        totat: int
        for index in self.plots:
            if self.plots[index] == 5:
                if replant:
                    self.plots[index] = 1
                else:
                    self.plots[index] = 0