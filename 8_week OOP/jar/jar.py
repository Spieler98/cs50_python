class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not capacity == 12:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        elif size < 0:
            raise ValueError
        self._size = size


def main():
    j = Jar()
    j.deposit(1) * 12
    print(j)
    j.withdraw(1) * 12
    print(j)
    j.deposit(1) * 12
    print(j)
    
if __name__ == "__main__":
    main()