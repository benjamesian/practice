# https://leetcode.com/problems/design-linked-list/
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None
        self.prev = None
        self.tail = self
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        elif index == self.length - 1:
            return self.tail.val

        if index < self.length / 2:
            p = self
            while index:
                p = p.next
                index -= 1
        else:
            p = self.tail
            i = self.length - 1
            while i > index:
                p = p.prev
                i -= 1

        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val is None:
            self.val = val
            self.tail = self
        else:
            p = MyLinkedList()
            p.val = self.val
            p.next = self.next
            p.prev = self

            self.val = val
            self.next = p
            if self is self.tail:
                self.tail = p
            else:
                p.next.prev = p
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val is None:
            self.val = val
            self.tail = self
        else:
            new = MyLinkedList()
            new.val = val
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            new = MyLinkedList()
            new.val = val
            if index < self.length / 2:
                p = self
                while index - 1:
                    p = p.next
                    index -= 1
            else:
                p = self.tail
                i = self.length - 1
                while i >= index:
                    p = p.prev
                    i -= 1
            new.next = p.next
            new.next.prev = new
            p.next = new
            new.prev = p

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        elif index == 0:
            if self.next:
                self.val = self.next.val
                self.next = self.next.next
                self.next.prev = self
            else:
                self.val = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            if index < self.length / 2:
                p = self
                while index:
                    p = p.next
                    index -= 1
            else:
                p = self.tail
                i = self.length - 1
                while i > index:
                    p = p.prev
                    i -= 1
            p.next.prev = p.prev
            p.prev.next = p.next

        self.length -= 1
