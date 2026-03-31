class TimeMap:

    def __init__(self):
        self._store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self._store:
            list_values = self._store[key]
            l,r = 0,len(list_values)-1
            max_time = -1
            max_item = None
            if list_values[r][1] <= timestamp:
                return list_values[r][0]
            while l<=r:
                m = (l+r)//2
                # print(f'm: {m}')
                if timestamp>=list_values[m][1]:
                    if list_values[m][1] >= max_time:
                        max_time = list_values[m][1]
                        max_item = list_values[m][0]

                    l=m+1
                else:
                    r=m-1
            # print(f'Max time: {max_time}')
            # print("===Binary Search Ends===")
            return max_item if max_item else ""
        # print("===Binary Search Ends===")

        # print()
        return ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)