# In this file, I will be implementing linked list and its basic operations.

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insertAtBeginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def getLastNode(self):
        if self.head is None:
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def printList(self):
        if self.head is None:
            print("List is empty.")
        itr = self.head
        llstr = ""
        while(itr):
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insertValues(self, data_values):
        self.head = None
        for i in data_values:
            self.insertAtEnd(i)

    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def removeAt(self, index):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Input")
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insertAt(self, data, index):
        if index<0 or index>self.getLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertAtBeginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insertAfterValue(self, dataAfter, dataToInsert):
        if self.head is None:
            return
        if self.head.data == dataAfter:
            self.head.next = Node(dataAfter, self.head.next)
        itr = self.head
        while itr:
            if dataAfter == itr.data:
                itr.next = Node(dataToInsert, itr.next)
                break
            itr = itr.next

    def removeByValue(self, data):
        if self.head is None:
            return
        if self.head == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def removeMiddleElement(self):
        if self.head is None:
            return
        itr = self.head
        n = 0
        while itr:
            itr = itr.next
            n += 1
        itr = self.head
        count = 0
        # n = self.getLength()
        middle = n//2
        while itr.next:
            if count == middle:
                itr.next = itr.next.next
            itr = itr.next
            count += 1



l = LinkedList()
l.insertAtBeginning(12)
l.insertAtBeginning(63)
l.insertAtEnd(85)
l.insertAtBeginning(19)
l.insertAtEnd(7)
l.printList()
l.insertAfterValue(12,45)
l.printList()
l.removeByValue(63)
l.printList()
l.removeMiddleElement()
l.printList()
# l.print_backward()
# l.printReverseList()
# l.insertValues([1, 2, 3, 4])
# l.printList()
# print(l.getLength())
# l.removeAt(2)
# l.printList()
# l.getLength()
# l.insertAt(2000, 1)
# l.printList()
