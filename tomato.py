class Tomato:
    states={'small':1, 'normal':2, 'big':3}
    def __init__(self, index,states):
        self._index=index
        self._state=states['small']
    def grow(self):
        self.gr=self._state+1
    def is_ripe(self):
        if self.gr==3:
            print("Томат вырос")







