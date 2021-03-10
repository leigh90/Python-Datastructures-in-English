class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # def push(self, item):
    #     self.items.append(item)

    # def pop(self):
    #     return self.items.pop()

    # def peek(self):
    #     return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



    # if you want to change the top of the stack instead of being at the end of the list to being the start then you have to explicitly define it  
    def push(self,item):
        self.items.insert(0,item)
        # note that the python .insert() method adds elements to a list at the specified index it takes as arguments the index to add the element at and the element to add

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

# PERSONAL NOTES
# 

# Please note that the two implementations do have significant differences in performance since append() and pop() operations are both O(1) ie constant time since its always one operation regardless of the 
# number of items in the stack Since all you're ever doing is adding or removing from the end of the list
# In the second implementation performance is slower since append() and pop() require O(n) depending on the size of the stack which is n. since at worst the item is at the start of the list so you have to 
# go through the entire list to get to end of the list