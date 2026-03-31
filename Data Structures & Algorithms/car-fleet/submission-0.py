class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = len(position)
        pos_speed_initial = zip(position, speed)

        pos_speed = sorted(pos_speed_initial, key = lambda x : x[0], reverse=True)

        times = []

        for x in pos_speed:
            times.append((target-x[0])/x[1])
        ptr = 0
        for i in range(1, len(times)):
            if times[i] <= times[ptr]:
                fleet -= 1
            else:
                ptr = i
        return fleet
        




        
        

        