'''
Created on Oct 7, 2020

@author: xxcha
'''
import unittest
import RCube.info as info

class InfoTest(unittest.TestCase):


    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user': 'cdd0035'}
        parms = {'op': 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)