from linked_list_practice import Node, LinkedList


if __name__ == "__main__":
    ll = LinkedList()
    data = [6, 5, 4, 3, 2, 1]
    for d in data:
        ll.insert_at_head(d)
    # ll.insert_at_tail(65)
    print(ll.get_length())
    print("")
    # ll.insert_at_index(3, 35)
    ll.print_ll()
    #print(ll.find_middle())