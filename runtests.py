import unittest
from tests import test_base

# runs the baseline software tests:
#       * opening and closing a socket
#       * testing for PUT methods
#       * testing for GET methods
#       * testing for CLEAR methods
#       * testing for QUIT methods
#       * running the example sequence
def base_suite():
    suite = unittest.TestSuite()
    suite.addTest(test_base.base_suite())
    return suite

# base test runner, will run the base suite
if __name__ == '__main__':
    unittest.main(defaultTest='base_suite')
