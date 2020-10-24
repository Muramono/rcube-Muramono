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
    def test000_010_ShouldTakeCubeParmas(self):
        expectedResult = {'check': 'check stub'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)