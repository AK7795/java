import unittest


def cube(a):
    return a*a*a


class c1(unittest.TestCase):

    def test1(self):
        z = float(input("enter to cubed : "))
        r = cube(z)

        self.assertAlmostEqual(1.88136596,r)


if __name__ == "__main__":
    unittest.main()

'''to find biggest among two numbers'''