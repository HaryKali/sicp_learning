
class Solutions():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def bigger(self, a, b):
        if a > b:
            return a
        else:
            return b

    def smaller(self, a, b):
        if a < b:
            return a
        if b < a:
            return b

    def question1(self):
        return self.bigger(self.a, self.bigger(self.b, self.c)), self.bigger(self.smaller(self.a, self.b), self.c)

    def question2(self):
        temp = 0
        for num in self.question1():
            temp = temp + num ** 2
        return temp

    def display(self, func):
        print(func)


test = Solutions(1, 2, 3)
test.display(test.question1())
test.display(test.question2())