class Node:
    def __init__(self, initdata, position = 0):
        self.data = initdata
        self.next_node = None
        self.position = position

    def set_node(self, newdata):
        self.data = newdata

    def set_next_node(self, newnext):
        self.next_node = newnext

    # def set_index(self):
    #     self.index_of_node += 1

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
        self.set_index_Node(self.head)

    def set_index_Node(self, node_value):
        position = 0
        current = node_value
        while current.next_node != None:
            current.position = position
            position+=1
            current.get_next_node().position = position
            current = current.get_next_node()


    def search_node(self, data):
        is_node_found = False
        current = self.head
        while not is_node_found and current != None:
            if current.get_node() == data:
                is_node_found = True
            else:
                current = current.get_next_node()
        return is_node_found

    def delete(self, data):
        previous = None
        current = self.head
        is_node_found = False
        while not is_node_found and current != None:
            if self.head.data == data:
                self.head = current.get_next_node()
                is_node_found = True
            elif current.get_node() == data:
                previous.set_next_node(current.get_next_node())
                is_node_found = True
            else:
                previous = current
                current = current.get_next_node()

    def size_of_list(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next_node()
        return count

    #def append_node(self):


    # def index_of_node(self):
    #     current = self.head
    #     current.index_of_data = 0
    #     while current != None:
    #         current = current.get_next_node()
    #         current.index_of_data += 1


# temp = Node(93)
# temp = Node(36)
# temp = Node(45)
# print(temp.get_node())

mylist = UnorderedList()
mylist.add_node(93)
mylist.add_node(37)
mylist.add_node(54)
mylist.add_node(76)
mylist.add_node(67)
mylist.delete(67)
mylist.add_node(57)
mylist.add_node(66)
mylist.add_node(90)

print(mylist.size_of_list())






