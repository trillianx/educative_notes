from linked_list_practice import Node, LinkedList


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(25)
    ll.insert_at_head(35)
    ll.insert_at_tail(100)
    print(ll.head.data)
    print(ll.head.next.data)
    print(ll.head.next.next.data)