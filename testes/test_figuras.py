import pytest 
from src.figuras import Figuras

class TestFiguras():

    def setup_class(self):
        self.fig = Figuras()
        print("\nsetup executado uma vez para cada classe")

    def teardown_class(self):
       pass
       print("\nteardown executado uma vez para cada classe")

    def test_triangle_type(self):
        assert self.fig.triangle_type(2, 2, 2) == 'Equilateral' 

    def test_triangle_type1(self):
        assert self.fig.triangle_type(4,5,7) == 'Scalene'

    def test_triangle_type2(self):
        assert self.fig.triangle_type(3,3,4) == 'Isosceles' 

    def test_triangle_type3(self):
        assert self.fig.triangle_type(0,1,4) == 'Not a triangle' 
    
   

    
