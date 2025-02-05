def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
    def d_c(start, end):
        if start < end:
            mid = (start+end+1)//2
            cur = TreeNode(nums[mid])
            cur.left = d_c(start, mid-1)
            cur.right = d_c(mid+1, end)
            return cur
        elif start == end:
            cur = TreeNode(nums[start])
            return cur
        return None

    return d_c(0, len(nums)-1)
