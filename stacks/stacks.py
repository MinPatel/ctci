class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, newitem):
        self.items.append(newitem)

    def get_item(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)


class FIFOStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def peek(self):
        return self.items[0]

    def pop(self):
        return self.items.pop(0)

class LIFOStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.LIFOStack = Stack()

    def peek(self):
        return self.items[(self.size() - 1)]

    def pop(self):
        return self.items.pop()


# LIFOStack = LIFOStack()
# LIFOStack.push(2)
# LIFOStack.push(5)
# LIFOStack.push(78)
# LIFOStack.push(4)
# LIFOStack.push(79)
# LIFOStack.pop()
#
#
# for items in LIFOStack.items:
#     print(items)
#
# print(" ")
# print(LIFOStack.peek())
# print (LIFOStack.get_item(3))

FIFOStack = FIFOStack()
FIFOStack.push(2)
FIFOStack.push(5)
FIFOStack.push(78)
FIFOStack.push(4)
FIFOStack.push(79)
FIFOStack.pop()

for items in FIFOStack.items:
    print(items)

print(" ")
print(FIFOStack.peek())
print (FIFOStack.get_item(3))




