#circular linked list 
class ExchangeRate:
    def __init__(self, rate):
        self.rate = rate
        self.next = None

class ExchangeRateTracker:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = size
        self.count = 0

    def add_rate(self, rate):
        new_rate = ExchangeRate(rate)
        if not self.head:
            self.head = self.tail = new_rate
            new_rate.next = self.head  # Circular link (son vagon head kismina baglaniyor)
        else:
            new_rate.next = self.head
            self.tail.next = new_rate
            self.tail = new_rate

        if self.count < self.size:
            self.count += 1
        else:  # Remove oldest rate
            self.head = self.head.next
            self.tail.next = self.head

    def display_rates(self):
        if not self.head:
            print("No rates recorded.")
            return
        current = self.head
        for _ in range(self.count):
            print(f"${current.rate}", end=" -> ")
            current = current.next
        print("(Back to start)")

rates = ExchangeRateTracker(5)
rates.add_rate(1.10)
rates.add_rate(1.12)
rates.add_rate(1.15)
rates.add_rate(1.18)
rates.add_rate(1.20)
rates.display_rates() # Output: $1.10 -> $1.12 -> $1.15 -> $1.18 -> $1.2 -> (Back to start)

rates.add_rate(1.22) #oldest rate (1.10) is removed
rates.display_rates() #output: $1.12 -> $1.15 -> $1.18 -> $1.2 -> $1.22 -> (Back to start)
