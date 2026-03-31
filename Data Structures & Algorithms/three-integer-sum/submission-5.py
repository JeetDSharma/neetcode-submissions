class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-2):
            l = i+1
            r = n-1
            target = -(nums[i])
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l+=1
                    continue
                if r < n-1 and nums[r] == nums[r+1]:
                    r-=1
                    continue
                if nums[l]+nums[r] == target:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[l]+nums[r] < target:
                    l+=1
                else:
                    r-=1
            
        return [list(x) for x in ans]

                
            # -4, -1, -1, 0, 1, 2