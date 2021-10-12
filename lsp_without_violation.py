from figures import Rectangle, True_Square


def check_area_rect(rect):
    assert(rect.get_area() == 250)

def check_area_sq(sq):
    assert(sq.get_area() == 625)

def check_perimeter_rect(rect):
    assert(rect.get_perimeter() == 70)

def check_perimeter_sq(sq):
    assert(sq.get_perimeter() == 100)

def main():
    rect = Rectangle()
    rect.set_height(10)
    rect.set_width(25)

    sq = True_Square()
    sq.set_size(10)
    sq.set_size(25)

    check_area_rect(rect)
    check_area_sq(sq)

    check_perimeter_rect(rect)
    check_area_sq(sq)


if __name__ == '__main__':
    main()