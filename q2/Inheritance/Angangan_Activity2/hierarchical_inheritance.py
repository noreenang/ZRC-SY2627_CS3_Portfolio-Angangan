class Parent:

  def __init__(self, text):
    self._text = text

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, val):
    self._text = val

  def func1(self):
    print(self._text)


class Child1(Parent):

  def func2(self):
    print("Child 1")


class Child2(Parent):

  def func3(self):
    print("Child 2")


class Child3(Parent):

  def func4(self):
    print("Child 3")


o1 = Child1("Text 1")
o2 = Child2("Text 2")
o3 = Child3("Text 3")

o1.func1()
o1.func2()

o2.text = "Updated text 2"
o2.func1()
o2.func3()

o3.func1()
o3.func4()
