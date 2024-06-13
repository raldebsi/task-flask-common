class MyClass:
    my_list = []

    def __init__(self, me) -> None:
        self.my_list.append(me)

    def print(self):
        print(self.my_list)

    def __new__(cls) -> Self:
        pass


obj1 = MyClass(3)
obj1.print()

obj2 = MyClass(5)
obj2.print()

obj1.print()

