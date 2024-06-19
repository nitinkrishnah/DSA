# https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/
# https://www.geeksforgeeks.org/problems/insert-in-a-sorted-list/1

def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        new_node = Node(key)
        if head1 is None:
            head1.append(new_node)
        
        if key<= head1.data:
            new_node.next = head1
            return new_node
            
        temp = head1
        while temp.next and temp.next.data<key:
            temp = temp.next
            
        new_node.next = temp.next
        temp.next = new_node
                
        return head1