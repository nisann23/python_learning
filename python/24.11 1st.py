#linked list
class Node:  
    def __init__(self, price):
        self.price = price
        self.next = None

class StockPrices:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_price(self, price):
        new_node = Node(price)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_oldest_price(self):
        if not self.head:
            print("No stock prices recorded.")
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def find_highest_price(self):
        if not self.head:
            return None
        max_price = self.head.price
        current = self.head
        while current:
            if current.price > max_price:
                max_price = current.price
            current = current.next
        return max_price

    def display_prices(self):
        current = self.head
        while current:
            print(f"${current.price}", end=" -> ")
            current = current.next
        print("None")

# Test Kodları
stocks = StockPrices()
stocks.add_price(120)
stocks.add_price(130)
stocks.add_price(125)
stocks.display_prices()  # output: $120 > $130 > $125 > None

stocks.remove_oldest_price()
stocks.display_prices() #output : $130 > $125 > None

print("Highest Price:", stocks.find_highest_price())