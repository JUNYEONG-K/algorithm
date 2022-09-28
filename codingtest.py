class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1.sort(reverse=True)
        l2.sort(reverse=True)
        _l1 = 0
        _l2 = 0
        for l in l1:
            _l1 += l
        for l in l2:
            _l2 += l
        print(_l1, _l2)
