class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append_list(self, l):
        n = self
        while n.next:
            n = n.next
        for num in l:
            n.next = Node(num)
            n = n.next

def delete_k(head, k):
    node = head
    node_length = 0
    while node:
        node_length += 1
        node = node.next
    delete_idx = node_length - (k - 1)

    dummy = Node(None)
    dummy_head = dummy
    cur = head
    cur_length = 0
    while cur:
        cur_length += 1
        if cur_length == delete_idx:
            dummy.next = None
            cur = cur.next
        else:
            dummy.next = cur
            cur = cur.next
            dummy = dummy.next
    return dummy_head.next

def double_pointer(head, k):
    pass

def print_linkedlist(node):
    while node:
        print(node.data, " ", end="")
        node = node.next
    print()
            
if __name__ == "__main__":
    node = Node(0)
    node.append_list([1, 2, 3, 4, 5, 6])
    print_linkedlist(node)
    node = delete_k(node, 3)
    print_linkedlist(node)






