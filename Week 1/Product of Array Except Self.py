class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # an element in left_products contains the product of all elements on its left
        # initialize left_products array
        left_products=[0 if i!=0 else 1 for i in range(len(nums))]
        # calculate the left products
        for i in range(1,len(nums)):
            left_products[i]=left_products[i-1]*nums[i-1]
        # calcuate the right products using the left products
        # initialize the first right product value
        right=1
        # from right (the last element) to left (the first element)
        for i in range(1,len(nums)+1):
            left_products[-i]*=right
            right*=nums[-i]
        # now we have the answer in the left_products
        return left_products
