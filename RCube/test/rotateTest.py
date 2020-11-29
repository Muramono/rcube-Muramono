'''
Created on Nov 27, 2020

@author: xxcha
'''
import unittest
import RCube.rotate as rotate

class rotateTest(unittest.TestCase):

    ## Iteration 3 incremental pre-product development test
     
#     def test000_010_ShouldReturnDefaultStatus(self):
#         expectedResult = {'rotate': 'rotate stub'}
#         parms = {'op': 'rotate'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
        
    def test000_020_ShouldReturnCubeStatusIntegrity(self):
        expectedResult = {'status': 'rotated', 'cube': 'ggggggggg rrrrrrrrr bbbbbbbbb ooooooooo wwwwwwwww yyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        parms = {'op': 'rotate', 'side': 'F', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    ## Happy Test
#     def test100_010_FrontClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggggggggg wrrwrrwrr bbbbbbbbb ooyooyooy wwwwwwooo rrryyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'f', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_020_FrontCounterClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggggggggg yrryrryrr bbbbbbbbb oowoowoow wwwwwwrrr oooyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'F', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_030_RightClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggyggyggy rrrrrrrrr wbbwbbwbb ooooooooo wwgwwgwwg yybyybyyb', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'r', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_040_RightCounterClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggwggwggw rrrrrrrrr ybbybbybb ooooooooo wwbwwbwwb yygyygyyg', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'R', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_050_BackClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggggggggg rryrryrry bbbbbbbbb woowoowoo rrrwwwwww yyyyyyooo', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'b', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_060_BackCounterClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggggggggg rrwrrwrrw bbbbbbbbb yooyooyoo ooowwwwww yyyyyyrrr', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'B', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_070_LeftClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'wggwggwgg rrrrrrrrr bbybbybby ooooooooo bwwbwwbww gyygyygyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'l', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_080_LeftCounterClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'yggyggygg rrrrrrrrr bbwbbwbbw ooooooooo gwwgwwgww byybyybyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'L', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_090_TopClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'rrrgggggg bbbrrrrrr ooobbbbbb gggoooooo wwwwwwwww yyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 't', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_100_TopCounterClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ooogggggg gggrrrrrr rrrbbbbbb bbboooooo wwwwwwwww yyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'T', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_110_UnderClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggggggooo rrrrrrggg bbbbbbrrr oooooobbb wwwwwwwww yyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'u', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
#     def test100_120_UnderCounterClockwiseCheck(self):
#         expectedResult = {'status': 'rotated', 'cube': 'ggggggrrr rrrrrrbbb bbbbbbooo ooooooggg wwwwwwwww yyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'U', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
    #Sad Test
    def test200_010_CheckBadKeyReturnError(self):
        expectedResult = {'status': 'error: bad integrity key'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_020_CheckMissingCubeReturnError(self):
        expectedResult = {'status': 'error: missing cube'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': None, 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_030_CheckMissingCubeOpReturnError(self):
        expectedResult = {'status': 'error: no cube op'}
        parms = {'op': 'rotate', 'side': 'f', 'integrity': '563F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_040_CheckCubeElementsReturnError(self):
        expectedResult = {'status': 'error: incorrect cube size'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': '11111111122222222233333333344444444455555555566666666', 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_050_CheckDistinctCubeReturnError(self):
        expectedResult = {'status': 'error: non-distinct cube'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': '111111111222222222333333333444444444555555555111111111', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_060_CheckLackingElementsReturnError(self):
        expectedResult = {'status': 'error: lacking 9 elements of each distinct'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': '111111111222222222333333333444444444555555555666666555', 'integrity': '6225DE1E096694A927A193B1281028E8D528EB8004D9F2999781D07E58BCA2D4'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_070_CheckNonDistinctMidReturnError(self):
        expectedResult = {'status': 'error: non-distinct middle'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': '111141111222222222333333333144444444555555555666666666', 'integrity': '0628732992F58A84A7F291067AB6CC9DC9B1AD8428DC93EE5126B0CD88108B0E'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_080_CheckInvalidCornersReturnError(self):
        expectedResult = {'status': 'error: impossible corner'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'bbgbbbbbbwoooooooogogggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy', 'integrity': '573D39853F85AFD6E55A0760EFA1EBE8A7EACA41753055D9B41D0B3FC5C2E986'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_090_CheckInvalidEdgesReturnError(self):
        expectedResult = {'status': 'error: impossible edge'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr', 'integrity': '3C0BA8BDCEDE1484616367FF864B66B643B8AF08566F650C4A43148CEAC8D289'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_100_CheckNoKeyValueReturnError(self):
        expectedResult = {'status': 'error: missing key value'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr', 'integrity': None}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_100_CheckNoKeyReturnError(self):
        expectedResult = {'status': 'error: missing key'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)