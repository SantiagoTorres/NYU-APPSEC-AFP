#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :

import unittest
import socket

import server

from threadServlet import identify_command
import threadServlet

# runs the baseline software tests:
#       * opening and closing a socket
#       * testing for PUT methods
#       * testing for GET methods
#       * testing for CLEAR methods
#       * testing for QUIT methods
#       * running the example sequence
class test_base(unittest.TestCase):
    

    # tests whether the connection is alive
    def test_open_close(self):
        afpserver = server.afp_server(10)
        afpserver.start()
       
        for i in range(1,11):
            client = socket.create_connection(('127.0.0.1',
                afpserver.port))
            client.close()

    # tests the put scenarios, different lengths, etc
    def test_put(self):
        pass

    # tests the get methods, put occurs  here also
    def test_get(self):
        pass

    # tests the clear methods, put occurrs here also
    def test_clear(self):
        pass

    # tests the quit methods
    def test_quit(self):
        pass

    def test_identify_command_existing(self):
       
        # test for existing commands... this is the pretty part
        command = 'GET foo'
        result = identify_command(command)
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0] == threadServlet.get)
        self.assertTrue(len(result[1]) == 1)

        command = 'PUT foo 12'
        result = identify_command(command)
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0] == threadServlet.put)
        self.assertTrue(len(result[1]) == 2)


        command = 'CLEAR foo'
        result = identify_command(command)
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0] == threadServlet.clear)
        self.assertTrue(len(result[1]) == 1)

        command = 'QUIT'
        result = identify_command(command)
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0] == threadServlet.quit)
        self.assertTrue(len(result[1]) == 0)


    def test_identify_command_nonexisting(self):
        # nonexisting commands 
        command = "quet"
        result = identify_command(command)
        self.assertTrue(result is None)

        command = "EXIT"
        result = identify_command(command)
        self.assertTrue(result is None)

        command = "I QUIT"
        result = identify_command(command)
        self.assertTrue(result is None)


    def test_identify_command_wrong_case(self):
        # wrong case commands
        command = "quit"
        result = identify_command(command)
        self.assertTrue(result is None)

        command = 'get foo'
        result = identify_command(command)
        self.assertTrue(result is None)

        command = 'put foo 12'
        result = identify_command(command)
        self.assertTrue(result is None)

        command = 'clear foo'
        result = identify_command(command)
        self.assertTrue(result is None)
    
    
    def test_identify_command_repeated_command(self):
        # repeated arguments
        command = 'GET QUIT foo'
        result = identify_command(command)
        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0] == threadServlet.get)
        self.assertTrue(len(result[1]) == 2)


    def test_identify_command_unicode(self):
        # punicode shit
        command = 'GET por favor señor'
        result = identify_command(command)
        self.assertTrue(result is None)

    def test_identify_command_long_strings(self):
        # incredibly long strings, we will define a sensible maximum, and 200 get's
        # will probably be it.
        command =  "GET "*200
        result = identify_command(command)
        self.assertTrue(result is None)

    def test_identify_command_empty_strings(self):
        # empty strings
        command = ''
        result = identify_command(command)
        self.assertTrue(result is None)

        #none as a string
        command = None
        result = identify_command(command)
        self.assertTrue(result is None)

def base_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_base, 'test'))
    return suite

if __name__ == '__main__':
    unittest.main()
