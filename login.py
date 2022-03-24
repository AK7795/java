import unittest

def log(usnam,passw):
    if usnam == "admin" and passw == "123456":
        return True
    else:
        return False

class new(unittest.TestCase):
    def test1(self):
        x = input("username : ")
        y = input("password : ")
        r = log(x,y)
        self.assertTrue(r)





if __name__ == "__main__":
    unittest.main()