'''
Created on Oct 23, 2020

@author: xxcha
'''
import unittest
import RCube.check as check

class checkTest(unittest.TestCase):
    
    ## Iteration 2 incremental development test
    
    def test000_010_ShouldReturnDefaultStatus(self):
        expectedResult = {'check': 'check stub'}
        parms = {'op': 'check'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test000_020_ShouldTakeCubeParmas(self):
        expectedResult = {'check': 'check stub'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test000_030_SimpleFullCheck(self):
        expectedResult = {'status': 'full'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)