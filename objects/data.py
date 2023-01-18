class Pattern:
    def __init__(self):
        self._internal = []
    
    def set(self, new):
        self._internal = list(new)

    def add(self, item):
        self._internal.append(item)
        self._internal.pop(0)
    
    def raw(self):
        return ''.join(self._internal)

class Data:
    def __init__(self):
        self._internal = {}
        self.pattern = Pattern()
    
    def __setitem__(self, key, value):
        self._internal[key] = value
    
    def __getitem__(self, key):
        return self._internal.get(key)
