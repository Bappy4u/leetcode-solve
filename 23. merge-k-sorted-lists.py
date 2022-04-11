class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        
        arr.sort()
        res = ListNode(0)
        rNext = res
        for d in arr:
            rNext.next = ListNode(d)
            rNext = rNext.next
            
        return res.next
        