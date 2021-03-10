from stack import Stack

new_stack = Stack()

# CHECK IF STACK IS EMPTY
print(new_stack.isEmpty())

# ADD NEW ITEMS TO STACK
new_stack.push(4)

# SEE stack items
print(new_stack.items)
new_stack.push('dog')
print(new_stack.items)

# SEE the item AT THE TOP of the stack
print(new_stack.peek())

# REMOVE ITEMS
new_stack.pop()
print(new_stack.items)
new_stack.push(['8.4', 'burgers'])
print(new_stack.items)

# SIZE OF STACK
print(new_stack.size())