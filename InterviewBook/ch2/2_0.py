class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append_tail(self, data):
        end = Node(data)
        n = self
        while n.next != None:
            n = n.next
        n.next = end


if __name__ == "__main__":
    head = Node(0)
    head.next = Node(1)
    head.append_tail(2)
    cur = head

    while cur:
        print(cur.data)
        cur = cur.next
    print("end")



