from linked_list_practice import Node, LinkedList


if __name__ == "__main__":
    ll = LinkedList()
    data = [55, 45, 25, 15, 5]
    for d in data:
        ll.insert_at_head(d)
    ll.insert_at_tail(65)
    print(ll.get_length())
    print("")
    ll.insert_at_index(3, 35)
    ll.print_ll()