import unittest

# runs the baseline software tests:
#       * opening and closing a socket
#       * testing for PUT methods
#       * testing for GET methods
#       * testing for CLEAR methods
#       * testing for QUIT methods
#       * running the example sequence
# 
class test_base(unittest.TestCase):

    def test_dummy_test(self):
        self.assertTrue(True)


def dummy_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_base, 'test'))
    return suite

if __name__ == '__main__':
    unittest.main()
