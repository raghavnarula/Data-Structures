# Revision for Trees

1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer:

```bash
file system
-----------
     /    <-- root
  /      \
...       home
      /          \
   ugrad        course
    /       /      |     \
  ...      cs101  cs112  cs113  
```
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays).

3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists).

4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.

## Binary Tree


A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

Full Binary Tree -> A Binary Tree is a full binary tree if every node has 0 or 2 children.

Complete Binary Tree -> Every level is filled to fullest except the last level. 

Perfect Binary Tree -> All levels filled completely.

Balanced Binary Tree -> A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes.

## Enumeration in Binary Trees

Number of possible unordered binary tree woth n nodes -> Sum(T(i-1)*T(n-i)) From i=1 to n.

Number of BST with n nodes is also same as unordered trees.

Labeled Binary trees with N nodes = Number of unlabeled * n! (all labels are different)


