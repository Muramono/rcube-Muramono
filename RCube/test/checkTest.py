'''
Created on Oct 23, 2020

@author: xxcha
'''
import unittest
import RCube.check as check

class checkTest(unittest.TestCase):
    
    ## Iteration 2 incremental development test
    
#     def test000_010_ShouldReturnDefaultStatus(self):
#         expectedResult = {'check': 'check stub'}
#         parms = {'op': 'check'}
#         actualResult = check._check(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test000_020_ShouldTakeCubeParmas(self):
#         expectedResult = {'check': 'check stub'}
#         parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'}
#         actualResult = check._check(parms)
#         self.assertDictEqual(expectedResult, actualResult)

## Iteration 2 Acceptance Test

# Happy Path Test
    def test100_010_SimpleFullCheck(self):
        expectedResult = {'status': 'full'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_020_SimpleSpotCheck(self):
        expectedResult = {'status': 'spots'}
        parms = {'op': 'check', 'cube': 'rrrrbrrrryyyyryyyyoooogoooowwwwowwwwbbbbybbbbggggwgggg', 'integrity': '8BE0EEDF13B2B464A2C7A120E6104AC7039B758E93D6F65651616FBBEED9A1EF'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_030_SimpleCrossesCheck(self):
        expectedResult = {'status': 'crosses'}
        parms = {'op': 'check', 'cube': 'ybybbbybybrbrrrbrbwgwgggwgwgygyyygygryryyyryrowowwwowo', 'integrity': 'CE16F6174A8E0339E556FFDD1358AA56A03B1EB548AC31E324E52AAD7DC8BEF9'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
## Sad Path Test
    def test200_020_FullCheckBadKeyReturnError(self):
        expectedResult = {'status': 'error bad integrity key'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        