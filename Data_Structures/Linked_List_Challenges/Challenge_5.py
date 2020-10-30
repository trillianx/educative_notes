from linked_list_class import LinkedList

def reverse(lst):
    if lst.isEmpty():
        return None
    next_node = None
    cur_node = lst.get_head()
    prev_node = None

    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
        
    lst.head_node = prev_node
    return lst




if __name__ == "__main__":
    lst = LinkedList()
    lst.insert_at_head(6)
    lst.insert_at_head(4)
    lst.insert_at_head(5)
    lst.insert_at_head(2)
    lst.show()
    reverse(lst)
    print("")
    lst.show()
