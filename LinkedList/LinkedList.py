class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None

    def set_node(self, newdata):
        self.data = newdata

    def set_next_node(self, newnext):
        self.next = newnext

    def get_node(self):
        return self.data

    def get_next_node(self):
        return self.next


class UnorderedList:
    def __init__(self, data):
        self.head = Node(data)

    def add_node(self, newdata):
        temp = self.head
        self.head = newdata
        Node.set_next_node(temp)
        return self.head

    def search_node(self, data):
        isNodeFound = False
        for each_node in Node:
            if data == Node.get_node():
                isNodeFound = True
        return isNodeFound

    def delete(self, data):
        isNodeFound = Unorderedlist.search_node(data)
        if isNodeFound:
            Node.data = Node.set_next_node(data)
        else:
            return print("Node Not Found")

    def size_of_list(self):
        count = 0
        for each_node in Node:
            count += 1
        return count


