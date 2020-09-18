###########################################################################
#               Circular linked Lists Basic Functions                     #
#               # Deletion at specific position                           #
#               # Insertion at specific position                          #
#               # Updating at specific position                           #
###########################################################################

import circular_linked_lists,insertion

class List(circular_linked_lists.List):
    def insertion_postion_circular(self):
        new  = insertion.Node()
        #position starts from self.headval

