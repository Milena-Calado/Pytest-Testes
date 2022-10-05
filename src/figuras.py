class Figuras:

    def triangle_type(self, a, b, c):

      if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
      elif a == b == c:
        return 'Equilateral'
      elif a == b or b == c or a == c:
        return 'Isosceles'
      else:
        return 'Scalene'