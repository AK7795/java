import unittest

def big(a,b):
    if a>b:
        return a
    else:
        return b

class c1(unittest.TestCase):

    def test1(self):
        x= int(input("no 1 : "))
        y = int(input("no 2 : "))
        r = big(x,y)
        s = max(x, y)
        self.assertEqual(s,r)


if __name__== "__main__":
    unittest.main()