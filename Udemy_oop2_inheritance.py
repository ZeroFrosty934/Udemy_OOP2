class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    pass


t = Cat()
t.make_sound("Meow")

print(t.cool)
print(Cat.cool)
print(Animal.cool)
