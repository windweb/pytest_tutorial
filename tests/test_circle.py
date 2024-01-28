import pytest
import source.shapes as shapes


class TestCircle:


    def setup_meаthod(self, method):
        print( f"Setting up {method}")


    def teardown_meаthod(self, method):
        print( f"Tearing down {method}")



    def test_one(self):
        assert True
        # circle = shapes.Circle(1)
        # assert circle.area() == math.pi


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