from figures import Rectangle, Square


def check_area(figure):
    figure.set_height(10)
    figure.set_width(25)
    assert(figure.get_area() == 250)

def check_perimeter(figure):
    figure.set_height(10)
    figure.set_width(25)
    assert(figure.get_perimeter() == 70)

def main():
    rect = Rectangle()
    sq = Square()

    check_area(rect)
    check_area(sq)

    check_perimeter(rect)
    check_area(sq)


if __name__ == '__main__':
    main()