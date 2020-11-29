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
        
#     def test000_020_ShouldReturnCubeStatusIntegrity(self):
#         expectedResult = {'status': 'rotated', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         parms = {'op': 'rotate', 'side': 'F', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
#         actualResult = rotate._rotate(parms)
#         self.assertDictEqual(expectedResult, actualResult)
        
    ## Happy Test
    def test100_010_FrontClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 'integrity': '0F3BDBE402C16D85756959CDEE1649281296A8507CDDF29EC328C72CC758DA28'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_020_FrontCounterClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy', 'integrity': '40C2BD2C76A2F307F760FEB0FAE3352809840F76BD8974613E2BA3B11AFC395E'}
        parms = {'op': 'rotate', 'side': 'F', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_030_RightClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb', 'integrity': '52F7A03F6CCD1422952F5DF17DE880B41EC309427339A2DAC0A8E114EFAE3F7B'}
        parms = {'op': 'rotate', 'side': 'r', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_040_RightCounterClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg', 'integrity': '0BC487F537509ACECE983337A0B682902129D2803AA6E9700F1035511DCE22A6'}
        parms = {'op': 'rotate', 'side': 'R', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_050_BackClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo', 'integrity': '660FDE671B5BEA48B0111447BA18EBB728F3F9A4AE10813AAFAE294CD04652DD'}
        parms = {'op': 'rotate', 'side': 'b', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_060_BackCounterClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'gggggggggrrwrrwrrwbbbbbbbbbyooyooyooooowwwwwwyyyyyyrrr', 'integrity': 'B38E19C30B88E65EECE3D7CCA4A963F06C99D3F5C4E32F8D76611BB1A9BCADDA'}
        parms = {'op': 'rotate', 'side': 'B', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_070_LeftClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy', 'integrity': 'BB960DFCBFE7BCFCA3BE95A22FFD088DB492FB942EB3EC5EE750FAD272330DB0'}
        parms = {'op': 'rotate', 'side': 'l', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_080_LeftCounterClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'yggyggyggrrrrrrrrrbbwbbwbbwooooooooogwwgwwgwwbyybyybyy', 'integrity': '3BE670BD7D442CAD986B42CFBC913695C4D666364208B723814DB1F8A3C5DA68'}
        parms = {'op': 'rotate', 'side': 'L', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_090_TopClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy', 'integrity': '0F91C6D401C276775A580869A8BFFC660BF45B134493D77F819636DA29612916'}
        parms = {'op': 'rotate', 'side': 't', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_100_TopCounterClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy', 'integrity': 'C2541978094B8FF38D7F143F1E3608F90565CF6501215D597E7E3DDD5D4F65B4'}
        parms = {'op': 'rotate', 'side': 'T', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_110_UnderClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'ggggggooorrrrrrgggbbbbbbrrroooooobbbwwwwwwwwwyyyyyyyyy', 'integrity': '41B16B12A06F65615143AB4AC653F65B4B599A4C5FE87AB4C879CDEB742FF301'}
        parms = {'op': 'rotate', 'side': 'u', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test100_120_UnderCounterClockwiseCheck(self):
        expectedResult = {'status': 'rotated', 'cube': 'ggggggrrrrrrrrrbbbbbbbbbooooooooogggwwwwwwwwwyyyyyyyyy', 'integrity': '6FCD2F0E5F44AB2BBA6F84A5BCECDD4DA0C9E2CEA96A36EEF72529695F230D25'}
        parms = {'op': 'rotate', 'side': 'U', 'cube':  'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
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
    def test200_110_CheckNoKeyReturnError(self):
        expectedResult = {'status': 'error: missing key'}
        parms = {'op': 'rotate', 'side': 'f', 'cube': 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_120_BadSideReturnError(self):
        expectedResult = {'status': 'error: bad side'}
        parms = {'op': 'rotate', 'side': 'x', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_130_BlankSideReturnError(self):
        expectedResult = {'status': 'error: blank side input'}
        parms = {'op': 'rotate', 'side': '', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_140_NoneSideReturnError(self):
        expectedResult = {'status': 'error: None side'}
        parms = {'op': 'rotate', 'side': None, 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
    def test200_150_MissingSideOpReturnError(self):
        expectedResult = {'status': 'error: Missing side'}
        parms = {'op': 'rotate', 'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'integrity': '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'}
        actualResult = rotate._rotate(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    