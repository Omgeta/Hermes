class A:
    def __init__(self, a):
        self.a = a

    def idk(self):
        print("Hello world!")


class B(A):
    def idk(self):
        print("Hell")

    def b(self):
        print("a different thing!")


b = B("a")
b.idk()
