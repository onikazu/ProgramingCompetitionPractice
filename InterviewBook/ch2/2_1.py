class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append_tail(self, data):
        n = self
        while n.next:
            n = n.next
        n.next = Node(data)

    def append_list(self, nums):
        n = self
        while n.next:
            n = n.next
        for num in nums:
            n.next = Node(num)
            n = n.next


def delete_dup(head):
    if not head:
        return None
    dummy = Node(None)
    dummy_head = dummy
    num_set = set()
    while head:
        if head.data in num_set:
            head = head.next
            dummy.next = None
        else:
            num_set.add(head.data)
            dummy.next = head 
            head = head.next
            dummy = dummy.next
    return dummy_head.next


def without_buffer(head):
    pass

    
def print_linked_list(node):
    head = node
    while head:
        print(f"{head.data}, ", end="")
        head = head.next
    print()


if __name__ == "__main__":
    node = Node(0)
    l = [1, 2, 2, 3, 4, 5, 5]
    node.append_list(l)
    print_linked_list(node)
    node = delete_dup(node)
    print_linked_list(node)

