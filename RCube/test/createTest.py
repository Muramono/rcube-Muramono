'''
Created on Oct 7, 2020

@author: xxcha
'''
import unittest
import RCube.create as create

class createTest(unittest.TestCase):


    def test100_010_ShouldRetrunCubeWithFaces(self):
        expectedResult = {'cube': '111111111222222222333333333444444444555555555666666666'}
        parms = {'op': 'create'}
        actualResult = create._create(parms)
        self.assertDictEqual(expectedResult, actualResult)