class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def check_number(self, n):
        if n % 15 == 0:
            return "fizzbuzz"
        elif n % 5 == 0:
            return "buzz"
        elif n % 3 == 0:
            return "fizz"
        else:
            return n

    def run(self):
        for n in range(1, self.number):
            self.check_number(n)


