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
        parms = {'op': 'check', 'cube': 'ybybbbybybrbrrrbrbwgwgggwgwgogooogogryryyyryrowowwwowo', 'integrity': '3A2CA2368EDAB67D1EAB30A5DCA67757FC389AC2924E3EDAB522BAABF8403202'}
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
        parms = {'op': 'check', 'cube': '111111111222222222333333333444444444555555555111111111', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_060_CheckLackingElementsReturnError(self):
        expectedResult = {'status': 'error lacking 9 elements of each distinct'}
        parms = {'op': 'check', 'cube': '111111111222222222333333333444444444555555555666666555', 'integrity': '6225DE1E096694A927A193B1281028E8D528EB8004D9F2999781D07E58BCA2D4'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_070_CheckNonDistinctMidReturnError(self):
        expectedResult = {'status': 'error non-distinct middle'}
        parms = {'op': 'check', 'cube': '111141111222222222333333333144444444555555555666666666', 'integrity': '0628732992F58A84A7F291067AB6CC9DC9B1AD8428DC93EE5126B0CD88108B0E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_080_CheckInvalidCornersReturnError(self):
        expectedResult = {'status': 'error impossible corner'}
        parms = {'op': 'check', 'cube': 'bbgbbbbbbwoooooooogogggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy', 'integrity': '573D39853F85AFD6E55A0760EFA1EBE8A7EACA41753055D9B41D0B3FC5C2E986'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_090_CheckInvalidEdgesReturnError(self):
        expectedResult = {'status': 'error impossible edge'}
        parms = {'op': 'check', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr', 'integrity': '3C0BA8BDCEDE1484616367FF864B66B643B8AF08566F650C4A43148CEAC8D289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_100_CheckNoKeyValueReturnError(self):
        expectedResult = {'status': 'error missing key value'}
        parms = {'op': 'check', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr', 'integrity': None}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_100_CheckNoKeyReturnError(self):
        expectedResult = {'status': 'error missing key'}
        parms = {'op': 'check', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
