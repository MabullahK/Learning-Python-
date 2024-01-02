class A:
  def showA(self):
    print("This is class A")

class B(A):
  def show(self):
    print("This is class B")

obj = B()
obj.show()

obj.showA()
