
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = 1
        for pile in piles:
            max_speed = max(max_speed, pile)
        
        answer = None

        
        while min_speed<=max_speed:

            speed = min_speed + (max_speed-min_speed)//2
            hour = 0
            for pile in piles:
                hour += pile//speed + (1 if pile%speed != 0 else 0)
            
            if hour <= h:
                max_speed = speed-1
                if answer:
                    answer = min(answer, speed)
                else:
                    answer = speed
            else:
                min_speed = speed+1
            # print(speed, hour, min_speed, max_speed)

        return answer
