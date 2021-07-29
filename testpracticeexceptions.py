import unittest
import practiceexceptions

class TestException(unittest.TestCase):
    def test_add(self):
        a = 10
        b = 10
        r = practiceexceptions.addnumber(a,b)
        self.assertEquals(20,r)
if __name__ == "__main__":
    unittest.main()