import unittest

class AssertTestDemo(unittest.TestCase):

    def test_ae(self):
        self.assertEqual("a", "a")

    def test_tf(self):
        a = True
        self.assertTrue(a)

    def test_in(self):
        a = "dasdas"
        self.assertIn("da",a)

if __name__ == '__main__':
    unittest.main()