from linked_list_class import LinkedList
from node_class import Node

def search(lst, value):
    if lst.head_node is None:
        return 'Empty List'
    
    cur = lst.head_node
    while cur is not None:
        data = cur.data
        if value == data:
            return True
        cur = cur.next
    return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(25)
    ll.insert_at_head(35)
    ll.insert_at_head(45)
    ll.insert_at_head(55)
    ll.insert_at_tail(15)
    print(search(ll, 1))