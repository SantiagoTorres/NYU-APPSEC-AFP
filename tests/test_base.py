import unittest
import socket

import server

# runs the baseline software tests:
#       * opening and closing a socket
#       * testing for PUT methods
#       * testing for GET methods
#       * testing for CLEAR methods
#       * testing for QUIT methods
#       * running the example sequence
class test_base(unittest.TestCase):

    # a placeholder to test the unittest framework
    def test_dummy_test(self):
        self.assertTrue(True)

    # tests whether the connection is alive
    def test_open_close(self):
        afpserver = server.afp_server(10)
        afpserver.start()
       
        print("connecting 11 times...")
        for i in range(1,11):
            client = socket.create_connection(('127.0.0.1',
                afpserver.port))
            client.close()
        print("done")

    # tests the put scenarios, different lengths, etc
    def test_put(self):
        pass

    # tests the get methods, put occurs  here also
    def test_get(self):
        pass

    # tests the clear methods, put occurrs here also
    def test_clear(self):
        pass




def base_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_base, 'test'))
    return suite

if __name__ == '__main__':
    unittest.main()
