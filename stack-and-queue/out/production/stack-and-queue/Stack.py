#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):         
        if self.isEmpty():
            raise Exception("Empty Stack. Cannot pop.")
        return self.items.pop()
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):      
        if self.isEmpty():
            raise Exception("Empty Stack. Cannot peek.")
        return self.items[len(self.items)-1] 
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += str(item) + ' '
        return stackAsString
    
    def clear(self):
        self.items = []