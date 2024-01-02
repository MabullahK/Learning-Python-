class cat:
  def intro(self):
    print("I Am a cat!")

class Hcat(cat):
  def fact(self):
    print("I am a small house cat")
    print()
    
class Jaguar(cat):
  def fact(self):
    print("My habitat is the jungle")
    print()
    
class Lion(cat):
  def fact(self):
    print("I have a big mane")
    print()
    
c=Hcat()
j=Jaguar()
l=Lion()

c.intro()
c.fact()
j.intro()
j.fact()
l.intro()
l.fact()
