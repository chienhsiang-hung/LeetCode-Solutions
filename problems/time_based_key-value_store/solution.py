class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append( (value, timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        '''
        [All the timestamps timestamp of set are strictly increasing]: implement a binary search
        '''
        arr = self.map[key]
        l, r = 0, len(arr)-1

        current_value = None
        while l <= r:
            mid = (l+r) // 2
            if arr[mid][1] < timestamp:
                current_value = arr[mid][0]
                l = mid+1
            elif arr[mid][1] == timestamp:
                return arr[mid][0]
            else:
                r = mid-1

        return current_value or ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)