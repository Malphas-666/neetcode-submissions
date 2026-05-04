class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        count = 1
        for i in range(len(self.stack) - 2, -1, -1):
            if price >= self.stack[i]:
                count += 1
            else:
                break
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)