class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1_idx=0
        num2_idx=len(numbers)-1
        while num1_idx<num2_idx:
            if numbers[num1_idx]+numbers[num2_idx]==target:
                return [num1_idx+1,num2_idx+1]
            # current pair is larger than the target
            elif numbers[num1_idx]+numbers[num2_idx]>target:
                num2_idx-=1
            # current pair is less than the target
            else:
                num1_idx+=1
