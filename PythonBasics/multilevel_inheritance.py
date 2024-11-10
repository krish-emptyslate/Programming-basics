class A:
    def display_a(self):
        return "im from class a"

class B(A):
    def display_b(self):
        return "im from class B"

class C(B):
    def display_c(self):
        return "im from class c"

object = C()
print(object.display_c())
print(object.display_a())
print(object.display_b())