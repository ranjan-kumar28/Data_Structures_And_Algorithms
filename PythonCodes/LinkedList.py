class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.count = 0
        self.head = None

    def insert_at_start(self,data):
        self.count += 1
        newNode = Node(data)
        if not self.head: self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def size(self):
        return self.count

    def insert_at_end(self,data):
        self.count += 1
        newNode = Node(data)
        current = self.head
        while(current):
            current = current.next
        current = newNode

    def remove(self,data):
        self.count -= 1
        temp = Node(0)
        temp.next = self.head
        if self.head.data == data:self.head = self.head.next
        else:
            while(temp.next):
                if temp.next.data == data:
                    a=temp.next
                    temp.next = temp.next.next
                    del a.data
                    del a.next
                    del a
                temp = temp.next

    def traverse(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
