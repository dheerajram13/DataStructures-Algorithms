from linked.Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0
     #O(N)
    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
              print("%d" % actualNode.data)
              actualNode = actualNode.nextNode

        #insert at Start O(1)
    def insertAtStart(self,data):
        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

     #O(1)
    def size(self):
        return self.counter

          #O(N)
    def insertAtEnd(self,data):
        if self.head is None:
            self.insertAtStart(data)
            return
        newNode = Node(data)
        actualNode = self.head

        self.counter += 1

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def remove(self,data):
        self.counter -= 1
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data,self.head)
