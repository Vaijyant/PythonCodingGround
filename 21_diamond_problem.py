class A:
    def my_print(self):
        print("In class A")

class B(A):
    def my_print2(self):
        print("In class B")

class C(A):
    def my_print2(self):
        print("In class C")
    def my_print(self):
        print("In class C, my_print")


class D(B, C):
    pass


obj_d = D()

obj_d.my_print()
obj_d.my_print2()