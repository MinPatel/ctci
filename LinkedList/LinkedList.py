class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None

    def set_node(self, newdata):
        self.data = newdata

    def set_next_node(self, newnext):
        self.next_node = newnext

    def get_node(self):
        return self.data

    def get_next_node(self):
        return self.next_node


class UnorderedList:
    def __init__(self):
        #self.head = Node(data)
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_node(self, newdata):
        temp = self.head
        #self.head = newdata
        self.head = Node(newdata)
        #Node.set_next_node(temp)
        self.head.set_next_node(temp)
        #return self.head

    def search_node(self, data):
        isNodeFound = False
        current = self.head
        while not isNodeFound and current != None:
            if current.get_node() == data:
                isNodeFound = True
            else:
                current.get_next_node()
                print(current.get_next_node())
        return isNodeFound

    # def delete(self, data):
    #     isNodeFound = UnorderedList.search_node(data)
    #     if isNodeFound:
    #         Node.data = Node.set_next_node(data)
    #     else:
    #         print("Node Not Found")##

    # def size_of_list(self):
    #     count = 0
    #     for each_node in Node:
    #         count += 1
    #     return count

# temp = Node(93)
# print(temp.get_node())

mylist = UnorderedList()
mylist.add_node(93)
mylist.add_node(37)
mylist.add_node(54)
mylist.add_node(76)
mylist.add_node(67)

result = mylist.search_node(54)




