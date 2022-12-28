
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      return True  # found the cycle
  return False


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()

'''
LinkedList has cycle: False
LinkedList has cycle: True
LinkedList has cycle: True
'''


'''
Time Complexity#
As we have concluded above, once the slow pointer enters the cycle, 
the fast pointer will meet the slow pointer in the same loop. 
Therefore, the time complexity of our algorithm will be O(N) 
where 'N' is the total number of nodes in the LinkedList.

Space Complexity#
The algorithm runs in constant space O(1).
'''
