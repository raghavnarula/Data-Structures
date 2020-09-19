###########################################################################
#               Circular linked Lists Basic Functions                     #
#               # Deletion at specific position                           #
#               # Insertion at specific position                          #
#               # Updating at specific position                           #
###########################################################################

import circular_linked_lists,insertion

class List(circular_linked_lists.List):
    def insertion_postion_circular(self,data,position):
        print("Enter the number according to the ")
        new  = insertion.Node(data)

        #position starts from self.headval

