'''

One brute force strategy could be to first count the number of nodes in the LinkedList 
and then find the middle node in the second iteration. 

Can we do this in one iteration?

We can use the Fast & Slow pointers method such that the fast pointer 
is always twice the nodes ahead of the slow pointer. 
This way, when the fast pointer reaches the end of the LinkedList, 
the slow pointer will be pointing at the middle node.

'''


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  slow = head
  fast = head
  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next
  return slow


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()

'''

Time complexity
The above algorithm will have a time complexity of O(N) 
where 'N' is the number of nodes in the LinkedList.

Space complexity
The algorithm runs in constant space O(1).

'''
