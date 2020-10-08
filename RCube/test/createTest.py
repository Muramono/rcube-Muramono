'''
Created on Oct 7, 2020

@author: xxcha
'''
import unittest
import RCube.create as create

class createTest(unittest.TestCase):


#     def test100_010_ShouldRetrunCubeWithFaces(self):
#         expectedResult = {'cube': '111111111222222222333333333444444444555555555666666666'}
#         parms = {'op': 'create'}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)

#     def test100_020_ShouldRetrunCubeWithSHA(self):
#         expectedResult = {'cube': '111111111222222222333333333444444444555555555666666666', 'integrity': '88D897BD22E132D21A538745E63995B07D7C52CE9617A0979520545753EE0DED'}
#         parms = {'op': 'create'}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)

#     def test100_020_ShouldRetrunFacesWithInput(self):
#         expectedResult = {'cube': '111111111222222222333333333444444444555555555777777777', 'integrity': '5CD36407758A5A2701A93E233647785E3833C67155A081BBF9F9BB214C253BD6'}
#         parms = {'op': 'create', 'faces': 123457}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020_ShouldRetrunFacesNonNumerical(self):
        expectedResult = {'cube': 'AAAAAAAAABBBBBBBBBCCCCCCCCCDDDDDDDDDEEEEEEEEEFFFFFFFFF', 'integrity': '60024C1DB8138D8D199D879E936ADD2AF35739DDC9FBC6348E2F555259FD7E9D'}
        parms = {'op': 'create', 'faces': 'ABCDEF'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)