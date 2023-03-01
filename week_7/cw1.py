class Queue:
    def __init__(self):
        self.elms = []

    def append(self, x):
        self.elms.append(x)

    def pop_front(self):
        if self.is_empty():
            return -1
        return self.elms.pop(0)
    
    def size(self):
        return len(self.elms)

    def peek(self):
        if self.is_empty():
            return -1
        return self.elms[0]

    def is_empty(self):
        if self.elms == []:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.elms}"
    