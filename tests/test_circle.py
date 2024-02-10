import math

import source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)  # создаем экземпляр класса Circle

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        # self.circle = shapes.Circle(10) # создаем экземпляр класса Circle
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    # def test_area(self):
    #     circle = shapes.Circle(5)
    #     assert circle.area() == 78.53981633974483
    #
    # def test_perimeter(self):
    #     circle = shapes.Circle(5)
    #     assert circle.perimeter() == 31.41592653589793
    #
    # def test_negative_radius(self):
    #     with pytest.raises(ValueError):
    #         shapes.Circle(-5)
    #
    # def test_zero_radius(self):
    #     with pytest.raises(ValueError):
    #         shapes.Circle(0)

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
