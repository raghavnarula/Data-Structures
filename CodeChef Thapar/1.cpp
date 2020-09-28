#include <bits/stdc++.h>

using namespace std;
// Approach for U op:
// basically we need to keep the track of how many links a node is connected to.
// we count the number of links which connect _to_ it.
//
// if an example list is: 1 -> 2 -> 3 -> 4
// then 1 has 0 links, and the rest of the elements have 1 link each.
//
// using this approach, we can easily differentiate when a node gets a change in
// number of links. We have to perform this subroutine whenever either a new
// node is added or when U op is called:
// - when the first node is added, it has 0 links, subsequent nodes will have 1
//   link each. This corresponds to the I 0 op.
// - when the I 1 op is summoned, we have to check whether the element is added
//   from at the start or not. if it is, we will increment `head`'s links and
//   initialise the newly added value's link to 0.
// - if the list is upgraded to circular, head's links get incremented by 1.
// - when a link is added in between or at the end of the list, always initiate
//   their links by 1.
// - when U op is called perform the updates to the link accordingly, the
//   comments under `move_next` should help.

struct Node {
    int val;
    Node *next;
};

class LinkedList {
public:
    Node *head, *tail;
    map<int,int> links;
    int circular = 0;
    int size = 0;

    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    void print() {
        Node *temp = this->head;
        while(temp) {
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }
    // spits the position of the element, starting from 0.
    // if it doesn't exist, returns -1
    int position(int val) {
        Node *temp = new Node;
        temp = this->head;

        int cnt = 0;
        while(temp) {
            if (temp->val == val) {
#if CP_DEBUG
                cout << val <<  " pos: " << cnt << endl;
#endif
                return cnt;
            } else {
                cnt++;
            }
            temp = temp->next;
        }
        // should not reach here 
        return -1;
    }

    void insert(int val) {
        Node* temp = new Node;
        temp->val = val;
        temp->next = NULL;


        if (!this->head) {
            // update link count: first node has no links
            links[val] = 0;
            this->head = temp;
            this->tail = temp;
        } else {
            // update link count
            links[val] = 1;
            this->tail->next = temp;
            this->tail = this->tail->next;
        }

        this->size++;
    }

    // inserts the element _before_ the given position.
    // ex: inserting at 0 adds the element at the 0th position
    //     and shifts all the nodes towards right.
    // this works till `size`.
    void insert_at_pos(int pos, int val) {
        Node* temp = this->head;
        Node* entry_node = new Node;
        entry_node->val = val;

        if (pos == this->size) {
            // if we are inserting the element at the very end of the list.
            insert(val);
            this->size--; // size will get incremented at insert.
        } else { 
            if (pos) { // anywhere after the first element.
                
                // update link count;
                // starting with one because we are adding in the middle.
                links[val] = 1;

                for (int i = 0; i < pos - 1; i++) {
                    temp = temp->next;
                }
                entry_node->next = temp->next;
                temp->next = entry_node;
            } else { // add at position 0.  

                // update link count
                links[this->head->val]++;
                links[val] = 0;

                entry_node->next = this->head;
                this->head = entry_node;
            }
        }

#if CP_DEBUG 
        cout << "inserted " << val << " at pos " << pos << " : ";
#endif

        this->size++;
    }

    void middle_insert(int bef, int aft, int val) {

        int start = position(bef);
        int end = position(aft);

        // logic is unclear, so i am adding elements after the
        // mid-element if the list has odd nodes.
        insert_at_pos((start + end)/2 + 1, val);
    }

    // insert element as given.
    // give it 7, 0 and it will fucking insert 7 or 0, whatever's missing
    // into the list in the exact fucking order.
    void lookalike_insert(int one, int two) {
        if (position(one) >= 0) {
            insert_at_pos(position(one) + 1, two);
        } else {
            insert_at_pos(position(two), one);
        }
    }

    // U op
    void move_next(int val, int pos) {
        Node *moving_node = this->head, *pos_ptr = this->head;

        // bring moving_node to val
        for (int i = 0; i < position(val); i++) {
           moving_node = moving_node->next; 
           pos_ptr = pos_ptr->next;
        }

        // update: original link to val is now broken.
        links[pos_ptr->next->val]--;
        
        // traverse pos_ptr to pos
        for (int i = 0; i < pos; i++) {
            if (pos_ptr->next) {
                pos_ptr = pos_ptr->next;
            } else {
                // boi we went circular
                // once we go circular, we never go back.
                this->circular = 1;
                this->tail->next = this->head;
                pos_ptr = pos_ptr->next;

                // circular also means that head gets a link.
                links[head->val]++;
            }
        }

        // update because a new link is made.
        links[pos_ptr->val]++;
        moving_node->next = pos_ptr;
    }
};

int main() 
{
#ifdef CP_DEBUG
    LinkedList* ll = new LinkedList;
#else
    int tests;
    cin >> tests;
    LinkedList* ll = new LinkedList;
    while (tests--) {
        char c;
        cin >> c;
        if (c == 'I') {
            int type;
            cin >> type;
            if (type == 0) {
                int x;
                cin >> x;
                ll->insert(x);
            } else if (type == 1) {
                int x, y;
                cin >> x >> y;
                ll->lookalike_insert(x, y);
            } else {
                int z, y, x;
                cin >> z >> y >> x;
                ll->middle_insert(z, y, x);
            }
        } else {
            int x, p;
            cin >> x >> p;
            ll->move_next(x, p);
        }
    }

    int multiple_links = 0;
    for (auto i: ll->links) {
        if (i.second > 1) {
            multiple_links++;
        }
    }

    cout << ll->circular << endl;
    cout << multiple_links << endl;
    if (multiple_links) {
        for (auto i: ll->links) {
            if (i.second > 1) {
                cout << i.first << " ";
            }
        }
        cout << endl;

        for (auto i: ll->links) {
            if (i.second > 1) {
                cout << i.second << " ";
            }
        }
        cout << endl;

    } else {
       ll->print(); 
    }
#endif
}