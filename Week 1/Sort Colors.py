class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the sorted array will look like:
        # [R, R, ... , | W, W, ... , | B, B, ... ]
        # r_w: the split line between red elements and white elements
        r_w=0
        # w_b: the split line between white elements and blue elements
        w_b=len(nums)-1
        # i: start index
        i=0
        while i<=w_b:
            # current element is red
            if nums[i]==0:
                # swap with the element on the right of the r_w bound
                nums[i],nums[r_w]=nums[r_w],nums[i]
                r_w+=1
            # current element is blue
            elif nums[i]==2:
                # swap with the element on the left of the w_b bound
                nums[i],nums[w_b]=nums[w_b],nums[i]
                w_b-=1
                # since the current element was swap from the untraversed part,
                # we need to check it again, so go back to the current index
                i-=1
            i+=1
            # doing nothing for if the current is white

