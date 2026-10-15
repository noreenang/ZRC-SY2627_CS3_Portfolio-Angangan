class Grandfather:

  def __init__(self, g_name):
    self._g_name = g_name

  @property
  def g_name(self):
    return self._g_name

  @g_name.setter
  def g_name(self, val):
    self._g_name = val


class Father(Grandfather):

  def __init__(self, f_name, g_name):
    super().__init__(g_name)
    self._f_name = f_name

  @property
  def f_name(self):
    return self._f_name

  @f_name.setter
  def f_name(self, val):
    self._f_name = val


class Son(Father):

  def __init__(self, s_name, f_name, g_name):
    super().__init__(f_name, g_name)
    self._s_name = s_name

  @property
  def s_name(self):
    return self._s_name

  @s_name.setter
  def s_name(self, val):
    self._s_name = val

  def print_name(self):
    print(self._g_name, self._f_name, self._s_name)


s1 = Son("Prince", "Rampal", "Lal mani")
s1.print_name()

s1.g_name = "Lal Bahadur"
s1.f_name = "Vikram"
s1.s_name = "Aryan"
s1.print_name()

s2 = Son("Leo", "Arthur", "Edward")
s2.print_name()
