'''
Created on Oct 7, 2020

@author: xxcha
'''
import unittest
import RCube.create as create

class createTest(unittest.TestCase):

# Test in this section where test used to incrementally develop the 'Create' function. They are now commented out to avoid unnecessary confusion of 'failed test'

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

#     def test100_030_ShouldRetrunFacesWithInput(self):
#         expectedResult = {'cube': '111111111222222222333333333444444444555555555777777777', 'integrity': '5CD36407758A5A2701A93E233647785E3833C67155A081BBF9F9BB214C253BD6'}
#         parms = {'op': 'create', 'faces': 123457}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)
        
#     def test100_040_ShouldRetrunFacesNonNumerical(self):
#         expectedResult = {'cube': 'AAAAAAAAABBBBBBBBBCCCCCCCCCDDDDDDDDDEEEEEEEEEFFFFFFFFF', 'integrity': '60024C1DB8138D8D199D879E936ADD2AF35739DDC9FBC6348E2F555259FD7E9D'}
#         parms = {'op': 'create', 'faces': 'ABCDEF'}
#         actualResult = create._create(parms)
#         self.assertDictEqual(expectedResult, actualResult)

## Test below are production acceptance test.
    # All sad path tests are 200 tests
    # All happy path tests are 100 tests
    def test200_010_ShouldRetrunErrorBadLength(self):
        expectedResult = {'status': 'error: bad length'}
        parms = {'op': 'create', 'faces': 'ABCDE'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)

    def test200_020_ShouldRetrunErrorDuplicate(self):
        expectedResult = {'status': 'error: duplicate'}
        parms = {'op': 'create', 'faces': 'AABCDE'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_050_ShouldRetrunDefaultCreateResponse(self):
        expectedResult = {'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289', 'status': 'ok'}
        parms = {'op': 'create'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)



