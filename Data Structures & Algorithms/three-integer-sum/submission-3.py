class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i, num in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            # print(num, end=": ")
            while l<r:
                two_sum = nums[l]+nums[r]
                # print(two_sum, end = ", ")
                
                if two_sum == -num:
                    ans.append([num,nums[l],nums[r]])
                    # break
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while r>l and nums[r] == nums[r+1]:
                        r-=1
                elif two_sum < -num:
                    l+=1
                else:
                    r-=1
            # print()
            
        return ans

        # -4,-1,-1,0,1,2
        