class RecentCounter:

    def __init__(self):
        self.calls = []
        self.length = 0

    def ping(self, t: int) -> int:
        self.calls.insert(0, t)
        self.length += 1

        while self.length > 0 and self.calls[self.length - 1] < (t - 3000):
            self.calls.pop()
            self.length -= 1
        
        return self.length

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)