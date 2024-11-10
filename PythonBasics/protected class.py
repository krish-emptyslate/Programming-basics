class Parent:
    def __init__(self):
        self._value = "im from parent class"

    def _show_value(self):
        print(f"im from show_value of Parent method {self}")
        print(self._value)



class child(Parent):

    def _display(self):
        print(f"im from display method of child {self}")
        super()._show_value()
        print(self._value)

kid1 = child()
kid1._display()
