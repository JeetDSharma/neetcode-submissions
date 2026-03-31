class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r=0,1
        ans = 0
        deduction = 0
        while r<n:
            if height[r]>=height[l]:
                # print(l,r)
                ans += (height[l]*(r-l-1))-deduction
                # print(ans)
                l=r
                deduction = 0
            else:
                deduction += height[r]
            r+=1
        l,r=n-2,n-1 
        deduction = 0
        while l>=0:
            if height[l]>height[r]:
                # print(l,r)
                ans += (height[r]*(r-l-1))-deduction
                # print(ans)
                r=l
                deduction = 0
            else:
                deduction += height[l]
            l-=1
        return ans

    #     How is water even trapped in first place
    #     water cannot be trapped in adjacent blocks
    #     I need two boundaries, between which water gets blocked

    #     maximum water that can be trapped is the min(h(a),h(b)) * gap assuming that the gap has 0 buildings

    #     what if there is a building in our gap? Then obviously reduce our capacity

    #     bascially the capacity is reduced by the same amount as the height of the building

    #     so either it is max(0,storage-height)

    #     So the left and right border that I pick, must have some positive value

    #     can I somehow use prefix or suffix sum to solve this?
    #     beacuse at the point I am, I need to know, like given my border what deductions I will be facing at each step for my gap

    #     but the summation of height gives me no value, it is a scalar quanitity, I need to know with repsect to each point in hand, 

    #     so I have to go from start to end, and I cannot start from opposit ends

    #     so water is always trapped between two borders or in chunks, so basically, calulate for all these chunks?

    #     I can currently only think with respect to starting, if I keep incrementing my right pointer, I will basically know 


    #     ummm

    #     I can never know if a point starts a new chunk

    #     I know this is a two pointer sum, but how it is being used is tricky

    #     Maybe, I am forcing two pointers on this, like I did in 3sum, try to first find invariants 

    #     Let us actually try to understand this sum

    #     The thing is, the way I solve it visually is not how this sum is actually going to be solved

    #     Let us try and understand all possible scenarios

    #     0,2,2,5,6,6,7,10,12,13
    #     14,14,11,11,8,7,7,6,5,3,1


