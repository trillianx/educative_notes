from linked_list_class import LinkedList
from node_class import Node

def deletion_at_head(lst):
    if lst.head_node is None:
        return 'Empty linked list'
    lst.head_node = lst.head_node.next
    return

def deletion_at_tail(lst):
    if lst.isEmpty():
        return None
    
def deletion_at_value(lst, value):
    if lst.isEmpty():
        return 'Empyt Linked list'
    
    if lst.get_head().data == value:
        return deletion_at_head(lst)
    
    cur = lst.head_node
    pre = cur
    while cur is not None:
        if cur.data == value:
            pre.next = cur.next
            cur.next = None
            return True
        pre = cur
        cur = cur.next
    return False

    


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(1)
    ll.insert_at_head(2)
    ll.insert_at_head(3)
    ll.insert_at_head(4)
    #ll.insert_at_tail(5)
    ll.show()
    print(deletion_at_value(ll, 3))
    print("-" * 10)
    ll.show()