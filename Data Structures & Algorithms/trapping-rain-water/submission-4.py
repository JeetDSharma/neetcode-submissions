class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0

        l,r = 0, len(height)-1
        lmax, rmax = height[0],height[r]
        l+=1
        r-=1
        ans = 0
        while l<=r:
            if lmax < rmax:
                ans += max(lmax - height[l],0)
                lmax = max(lmax,height[l])
                l+=1
            else:
                ans += max(rmax - height[r],0)
                rmax = max(rmax,height[r])
                r -= 1
        
        return ans