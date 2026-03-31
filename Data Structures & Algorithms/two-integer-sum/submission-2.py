class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            nums_list[i] = (num, i)
        

        nums_list.sort(key = lambda x: x[0])

        l,r = 0, len(nums)-1
        ans = [10**18,10**18]
        while l<r:
            sum = nums_list[l][0] + nums_list[r][0]
            if sum == target:
                index_l = nums_list[l][1]
                index_r = nums_list[r][1]

                if index_l > index_r:
                    l+=1
                    index_l, index_r = index_r, index_l
                else:
                    r-=1
                if index_l < ans[0]:
                    ans = [index_l,index_r]
                
            elif sum < target:
                l+=1
            else:
                r-=1

        return ans

