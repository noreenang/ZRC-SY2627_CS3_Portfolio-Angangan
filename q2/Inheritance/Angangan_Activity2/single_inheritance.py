class Parent:

  def __init__(self, msg):
    self._msg = msg

  @property
  def msg(self):
    return self._msg

  @msg.setter
  def msg(self, val):
    self._msg = val

  def func1(self):
    print(self._msg)


class Child(Parent):

  def __init__(self, msg, c_msg):
    super().__init__(msg)
    self._c_msg = c_msg

  @property
  def c_msg(self):
    return self._c_msg

  @c_msg.setter
  def c_msg(self, val):
    self._c_msg = val

  def func2(self):
    print(self._c_msg)


obj = Child("Parent msg", "Child msg")
obj.func1()
obj.func2()

obj.msg = "Updated parent"
obj.c_msg = "Updated child"
obj.func1()
obj.func2()

obj2 = Child("New parent", "New child")
obj2.func1()
obj2.func2()
