class Circle:
    def draw(self):
        print("Drawing a Circle.")

class Square:
    def draw(self):
        print("Drawing a Square.")

shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()
