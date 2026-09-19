

    /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* partition(struct ListNode* head, int x) {
    // Create two dummy nodes:
    // one for the "less than x" list, and one for "greater or equal to x"
    struct ListNode lessDummy = {0, NULL};
    struct ListNode greaterDummy = {0, NULL};

    struct ListNode* less = &lessDummy;
    struct ListNode* greater = &greaterDummy;

    // Traverse the original list
    while (head != NULL) {
        if (head->val < x) {
            less->next = head;       // Add to 'less' list
            less = less->next;
        } else {
            greater->next = head;    // Add to 'greater' list
            greater = greater->next;
        }
        head = head->next;
    }

    // End the greater list
    greater->next = NULL;

    // Join the two lists
    less->next = greaterDummy.next;

    // Return head of the 'less' list (skip dummy)
    return lessDummy.next;
}

    
