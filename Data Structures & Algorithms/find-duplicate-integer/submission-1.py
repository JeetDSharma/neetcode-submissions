class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while True:
            if slow == fast:
                slow = 0
                while True:
                    slow = nums[slow]
                    fast = nums[fast]
                    if slow == fast:
                        return slow
            else:
                slow = nums[slow]
                fast = nums[nums[fast]]
            


        