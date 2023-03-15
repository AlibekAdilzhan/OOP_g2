class Stack:
    def __init__(self):
        self.__elms = []

    def push(self, x):
        self.__elms.append(x)

    def pop(self):
        if self.is_empty():
            raise Exception("there are no elements")
        return self.__elms.pop()
    
    def is_empty(self):
        if self.__elms == []:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        return self.__elms[-1]
    
    def size(self):
        return len(self.__elms)
    
    def __str__(self):
        return f"{self.__elms}"
    

s = Stack()
s.push(1)
s.push(2)
s.pop()
s.pop()
s.pop()
print(s)