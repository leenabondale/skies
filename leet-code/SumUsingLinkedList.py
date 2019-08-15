class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def _addNodes(self, l1: ListNode, l2: ListNode, carry: int) -> int:

        l1_val = l1.val if l1 is not None else 0
        l2_val = l2.val if l2 is not None else 0

        print('adding {} and {} with carry {}'.format(l1_val, l2_val, carry))

        l3_val = l1_val + l2_val + carry

        return l3_val

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l3 = ListNode(0)
        root_l3 = l3

        isCarry = 0
        prev_l3 = None

        while (l1 is not None or l2 is not None or isCarry is not 0):

            l3 = ListNode(0)

            if prev_l3 is not None:
                prev_l3.next = l3

            l3_val = self._addNodes(l1, l2, isCarry)


            if l3_val > 9:
                isCarry = 1
                l3_val = l3_val % 10
            else:
                isCarry = 0

            l3 = ListNode(l3_val)
            prev_l3 = l3

            print('output: {} and carry: {}'.format(l3_val, isCarry))

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return root_l3







    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:

        l3 = ListNode(0)

        while l1 is not None or l2 is not None or l3 is not None:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            l3_val = l3.val if l3 is not None else 0

            val = l1_val + l2_val + l3_val

            print('=============val: {}'.format(val))

            isCarry = True if val > 9 else False


            l3 = None if l1 is None and l2 is None else ListNode(val if isCarry is False else val % 10)

            if l3 is not None:
                print('l1: {}, l2: {}, l3: {}'.format(l1_val, l2_val, l3.val))

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            if l1 is None and l2 is None and isCarry is False:
                return l3
            else:
                l3 = ListNode(1) if isCarry is True else ListNode(0)
                print('carrying over')

        return l3

    def printLinkedList(self, ll: ListNode):

        while(ll is not None):
            print('{}'.format(ll.val))
            ll = ll.next
            if ll is not None:
                print(' -> ')


    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        while l3 is not None:
            print('l3: {}'.format(l3.val))

            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            val = l3.val + l1_val + l2_val
            print('value of l1 is {}, l2 is {}, l3 is {}'.format(l1_val, l2_val, l3.val))
            carry = 0
            if val > 9:
                carry = 1
                val = val % 10
            l3 = ListNode(val)
            print('value of l3 is {}'.format(l3.val))
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            # l3.next = ListNode(0)
            l3 = l3.next
            if carry is 1:
                l3 = ListNode(1)
            else:
                l3 = ListNode(0)



sol = Solution()

# 1 -> 5 -> 8 [851]
ll11 = ListNode(8)
ll12 = ListNode(5)
ll12.next = ll11
ll13 = ListNode(1)
ll13.next = ll12

# 6 -> 5 -> 4 [456]
ll21 = ListNode(4)
ll22 = ListNode(5)
ll22.next = ll21
ll23 = ListNode(6)
ll23.next = ll22

print('bello!!')
l3 = sol.addTwoNumbers(ll13, ll23)

print('ending bello!!')
print("output: {}".format(sol.printLinkedList(l3)))

