## reverse a linked list ######
# 1->2->3->4->5               #
# to                          #
# 5->4->3->2->1               #
###############################
# = just copies the reference of the object so any changes made to the any one of those effect the other as well
import insertion,product_linked_list

class List(product_linked_list.List):
    def reverse(self):
        # iterate over the linked list and then make a backwards pointer to node
        prev = None
        current = self.headval
        while (current is not None):
            # the current must move to next node also
            # we create a copy of node we want so we can access it later
            temp = current
            current = current.nextval
            temp.nextval = prev
            prev = temp

list = List()
list.insert(10)
list.insert(20)
list.insert(30)
list.reverse()











