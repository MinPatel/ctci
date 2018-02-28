class Stacks():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, newitem):
        self.items.append(newitem)

    def peek(self):
        return self.items[(self.size()-1)]

    def get_item(self, index):
        return self.items[index]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

LIFOStack = Stacks()
LIFOStack.push(2)
LIFOStack.push(5)
LIFOStack.push(78)
LIFOStack.push(4)
LIFOStack.push(79)


for items in LIFOStack.items:
    print(items)

print(" ")
print(LIFOStack.peek())
print (LIFOStack.get_item(3))


