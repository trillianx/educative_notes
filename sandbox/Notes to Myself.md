# Linked List Notes
* For the case of insert at head, it is important to have `return self.head`. This allows the `self.head` to reset. 
* For the `insert_at_tail` you should end with `cur_node.next = new_node`. This seems counter-intuitive as `cur_node = cur_node.next`, but still we need to state that clearly.
* For checking the length of linked lists, you want to use `cur_node != None` rather than `cur_node.next != None`. The latter will result in one less count. 
* 

