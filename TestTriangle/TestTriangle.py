import unittest


def classify_triangle(a, b, c):
    if a == b and a == c and b == c:
        print('Equilateral triangle')
    elif a == b or a == c or b == c:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')

    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print('Right triangle')
    else:
        print('Not a right triangle')


class Testclassify_triangle(unittest.TestCase):
    def equal_sides(self):
        self.assertEqual(classify_triangle(2, 2, 2))

    def noequal_sides(self):
        self.assertNotEqual(classify_triangle(1, 2, 3))


print('Enter 3 side lengths')
a = int(input())
b = int(input())
c = int(input())
classify_triangle(a, b, c)

if __name__ == '__main__':
    unittest.main()
