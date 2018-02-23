class Node:
    def __init__(self, initdata, position = 0):
        self.data = initdata
        self.next_node = None
        self.position = position

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
        self.set_index_Node(self.head, 0)

    def set_index_Node(self, node_value, position):
        current = node_value
        while current.next_node != None:
            current.position = position
            position += 1
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

    def insert_node_atindex(self, newdata, nodeindex):
        previous = None
        current = self.head
        indexfound = False
        while not indexfound:
            if current.position == nodeindex: #adding the node at any index
                #self.add_node(newdata)
                temp = current
                current = Node(newdata)
                current.set_next_node(temp)
                self.set_index_Node(current,nodeindex)
                previous.set_next_node(current)
                indexfound = True
            elif current.position == (nodeindex - 1): #appending the node
                lastnode = Node(newdata)
                current.set_next_node(lastnode)
                lastnode.position = current.position + 1
                indexfound = True
            elif current.position != nodeindex:
                previous = current
                current = current.get_next_node()


    def append_node(self,newdata):
        size_of_list = self.size_of_list()
        self.insert_node_atindex(newdata,size_of_list)

# temp = Node(93)
# temp = Node(36)
# temp = Node(45)
# print(temp.get_node())

mylist = UnorderedList()
mylist.add_node(93)
mylist.add_node(37)
mylist.add_node(66)
mylist.add_node(90)
mylist.append_node(45)

# mylist.add_node(31)
# mylist.add_node(77)
# mylist.add_node(17)
# mylist.add_node(93)
# mylist.add_node(26)
# mylist.add_node(54)
#
# print(mylist.size_of_list())
# print(mylist.search_node(93))
# print(mylist.search_node(100))
#
# mylist.add_node(100)
# print(mylist.search_node(100))
# print(mylist.size_of_list())
#
# mylist.delete(54)
# print(mylist.size_of_list())
# mylist.delete(93)
# print(mylist.size_of_list())
# mylist.delete(31)
# print(mylist.size_of_list())
# print(mylist.search_node(93))






