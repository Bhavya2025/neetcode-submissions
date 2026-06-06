/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/


class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) return NULL;
        unordered_map<Node*,Node*> mp;
        Node *dummy = head;
        Node *cpy_head = new Node(dummy->val);
        Node *prev = cpy_head;
        mp[dummy] = cpy_head;
        while (dummy->next) {
            dummy = dummy->next;
            Node *node = new Node(dummy->val);
            mp[dummy] = node;
            prev->next = node;
            prev = node;
        }
        prev->next = NULL;

        for (auto& [orig, copy] : mp) {
            if (orig->random) {
                copy->random = mp[orig->random];
            } else {
                copy->random = NULL;
            }
        }
        return cpy_head;
    }
};
