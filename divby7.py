import unittest


def divby7(a):

    if a % 7 == 0:
        return True
    else:
        return False


class c(unittest.TestCase):

    def test1(self):
        x = int(input("enter no : "))
        res = divby7(x)
        self.assertTrue(res)


    def test2(self):
        y= int(input("enter not 7 : "))
        re = divby7(y)
        self.assertFalse(re)



if __name__ == "__main__":
    unittest.main()
