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
    def test100_040_SimpleUnknownCheck(self):
        expectedResult = {'status': 'unknown'}
        parms = {'op': 'check', 'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
## Sad Path Test
    def test200_010_CheckBadKeyReturnError(self):
        expectedResult = {'status': 'error bad integrity key'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_020_CheckMissingCubeReturnError(self):
        expectedResult = {'status': 'error missing cube'}
        parms = {'op': 'check', 'cube': None, 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_030_CheckMissingCubeOpReturnError(self):
        expectedResult = {'status': 'error no cube op'}
        parms = {'op': 'check', 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_040_CheckCubeElementsReturnError(self):
        expectedResult = {'status': 'error incorrect cube size'}
        parms = {'op': 'check', 'cube': '11111111122222222233333333344444444455555555566666666', 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_050_CheckDistinctCubeReturnError(self):
        expectedResult = {'status': 'error non-distinct cube'}
        parms = {'op': 'check', 'cube': '111111111222222222333333333444444444555555555111111111', 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)