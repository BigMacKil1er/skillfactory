from rectangle import Rectangle, Square, Circle

r1 = Rectangle(10, 5)
r2 = Rectangle(13, 12)

sq1 = Square(5)
sq2 = Square(10)

cr1 = Circle(5)
cr2 = Circle(2)

figures = [r1, r2, sq1, sq2, cr1, cr2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.getArea())