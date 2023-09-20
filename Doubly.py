class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    def __init__(self):
        self._head = None

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

    def is_empty(self):
        return self._head is None

    # Display the list
    def display(self):
        cur = self._head
        while cur:
            print(cur.item, end=" <-> ")
            cur = cur.next
        print("None")

if __name__ == "__main__":
    ll = DLinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Original Doubly Linked List:")
    ll.display()

    ll.remove(2)

    # Display the list after deletion
    print("\nDoubly Linked List after deleting node with value 2:")
    ll.display()
