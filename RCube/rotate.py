import hashlib
import RCube.check as _check

def _rotate(parms):
    result = dict()
    status = ''
    cube = ''
    integrityKey = ''
    
    #Input Parms Check
    ## TODO Add Parm checks around Side values e.g look for incorrect side input
    if(SideParmCheck(parms) != dict()):
        return SideParmCheck(parms)
    if(_check._ParmsCheck(parms) != dict()):
        return _check._ParmsCheck(parms)
    #Check that the inputed cube is valid.
    if(CubeValidation(parms) != dict()):
        return CubeValidation(parms)
    
    #Check For Valid Key
    if(IntegrityCheck(parms) != dict()):
        return IntegrityCheck(parms)
    #Set Integrity Key
    ByteCube = bytearray(parms['cube'],'utf8')
    integrityKey = hashlib.sha256(ByteCube).hexdigest()
    integrityKey = integrityKey.upper()
    
    if(parms['side'] == 'f' or parms['side'] == 'F'):
        cube = FrontFaceRotate(parms)
        status = 'rotated'
    if(parms['side'] == 'r' or parms['side'] == 'R'):
        cube = RightFaceRotate(parms)
        status = 'rotated'
    if(parms['side'] == 'b' or parms['side'] == 'B'):
        cube = BackFaceRotate(parms)
        status = 'rotated'
    if(parms['side'] == 'l' or parms['side'] == 'L'):
        cube = LeftFaceRotate(parms)
        status = 'rotated'
    if(parms['side'] == 't' or parms['side'] == 'T'):
        cube = TopFaceRotate(parms)
        status = 'rotated'
    if(parms['side'] == 'u' or parms['side'] == 'U'):
        cube = BottomFaceRotate(parms)
        status = 'rotated'

    
    
    result = {'status': status, 'cube': cube, 'integrity': integrityKey}
    return result

## Idea Transpose left and right side to get columns then swap them itertively 
def FrontFaceRotate(parms):
    if(parms['side'] == 'f'):
        cube = list(parms['cube'])
        #Right Side Values That Change
        RightS = cube[9] + cube[12] + cube[15]
        #Bottom Side Values That Change
        BotS = cube[45] + cube[46] + cube[47]
        #Left Side Values That Change
        LeftS = cube[29] + cube[32] + cube[35]
        #Top Side Values That Change
        TopS = cube[42] + cube[43] + cube[44]
        #Set Right Side
        cube[9] =  TopS[2]
        cube[12] = TopS[1]
        cube[15] = TopS[0]
        #Set Bottom
        cube[45] = RightS[2]
        cube[46] = RightS[1]
        cube[47] = RightS[0]
        #Set Left
        cube[29] = BotS[0]
        cube[32] = BotS[1]
        cube[35] = BotS[2]
        #Set Top
        cube[42] = LeftS[2]
        cube[43] = LeftS[1]
        cube[44] = LeftS[0]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
    if(parms['side'] == 'F'):
        cube = list(parms['cube'])
        #Right Side Values That Change
        RightS = cube[9] + cube[12] + cube[15]
        #Bottom Side Values That Change
        BotS = cube[45] + cube[46] + cube[47]
        #Left Side Values That Change
        LeftS = cube[29] + cube[32] + cube[35]
        #Top Side Values That Change
        TopS = cube[42] + cube[43] + cube[44]
        #Set Right Side
        cube[9] =  BotS[2]
        cube[12] = BotS[1]
        cube[15] = BotS[0]
        #Set Bottom
        cube[45] = LeftS[0]
        cube[46] = LeftS[1]
        cube[47] = LeftS[2]
        #Set Left
        cube[29] = TopS[2]
        cube[32] = TopS[1]
        cube[35] = TopS[0]
        #Set Top
        cube[42] = RightS[0]
        cube[43] = RightS[1]
        cube[44] = RightS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
##END

def RightFaceRotate(parms):
    if(parms['side'] == 'r'):
        cube = list(parms['cube'])
        #Front Side Values That Change
        FrontS = cube[2] + cube[5] + cube[8]
        #Bottom Side Values That Change
        BotS = cube[47] + cube[50] + cube[53]
        #Back Side Values That Change
        BackS = cube[18] + cube[21] + cube[24]
        #Top Side Values That Change
        TopS = cube[38] + cube[41] + cube[44]
        #Set Front Side
        cube[2] = BotS[0]
        cube[5] = BotS[1]
        cube[8] = BotS[2]
        #Set Bottom
        cube[47] = BackS[2]
        cube[50] = BackS[1]
        cube[53] = BackS[0]
        #Set Back
        cube[18] = TopS[2]
        cube[21] = TopS[1]
        cube[24] = TopS[0]
        #Set Top
        cube[38] = FrontS[0]
        cube[41] = FrontS[1]
        cube[44] = FrontS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
    if(parms['side'] == 'R'):
        cube = list(parms['cube'])
        #Front Side Values That Change
        FrontS = cube[2] + cube[5] + cube[8]
        #Bottom Side Values That Change
        BotS = cube[47] + cube[50] + cube[53]
        #Back Side Values That Change
        BackS = cube[18] + cube[21] + cube[24]
        #Top Side Values That Change
        TopS = cube[38] + cube[41] + cube[44]
        #Set Front Side
        cube[2] = TopS[0]
        cube[5] = TopS[1]
        cube[8] = TopS[2]
        #Set Bottom
        cube[47] = FrontS[0]
        cube[50] = FrontS[1]
        cube[53] = FrontS[2]
        #Set Back
        cube[18] = BotS[0]
        cube[21] = BotS[1]
        cube[24] = BotS[2]
        #Set Top
        cube[38] = BackS[2]
        cube[41] = BackS[1]
        cube[44] = BackS[0]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
##END

def BackFaceRotate(parms):
    if(parms['side'] == 'b'):
        cube = list(parms['cube'])
        #Left Side Values That Change
        LeftS = cube[27] + cube[30] + cube[33]
        #Bottom Side Values That Change
        BotS = cube[51] + cube[52] + cube[53]
        #Right Side Values That Change
        RightS = cube[11] + cube[14] + cube[17]
        #Top Side Values That Change
        TopS = cube[36] + cube[37] + cube[38]
        #Set Left Side
        cube[27] = TopS[2]
        cube[30] = TopS[1]
        cube[33] = TopS[0]
        #Set Bottom
        cube[51] = LeftS[0]
        cube[52] = LeftS[1]
        cube[53] = LeftS[2]
        #Set Right
        cube[11] = BotS[2]
        cube[14] = BotS[1]
        cube[17] = BotS[0]
        #Set Top
        cube[36] = RightS[0]
        cube[37] = RightS[1]
        cube[38] = RightS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
    if(parms['side'] == 'B'):
        cube = list(parms['cube'])
        #Left Side Values That Change
        LeftS = cube[27] + cube[30] + cube[33]
        #Bottom Side Values That Change
        BotS = cube[51] + cube[52] + cube[53]
        #Right Side Values That Change
        RightS = cube[11] + cube[14] + cube[17]
        #Top Side Values That Change
        TopS = cube[36] + cube[37] + cube[38]
        #Set Left Side
        cube[27] = BotS[0]
        cube[30] = BotS[1]
        cube[33] = BotS[2]
        #Set Bottom
        cube[51] = RightS[2]
        cube[52] = RightS[1]
        cube[53] = RightS[0]
        #Set Right
        cube[11] = TopS[0]
        cube[14] = TopS[1]
        cube[17] = TopS[2]
        #Set Top
        cube[36] = LeftS[1]
        cube[37] = LeftS[1]
        cube[38] = LeftS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
##END
def LeftFaceRotate(parms):
    if(parms['side'] == 'l'):
        cube = list(parms['cube'])
        #Back Side Values That Change
        BackS = cube[20] + cube[23] + cube[26]
        #Bottom Side Values That Change
        BotS = cube[45] + cube[48] + cube[51]
        #Front Side Values That Change
        FrontS = cube[0] + cube[3] + cube[6]
        #Top Side Values That Change
        TopS = cube[36] + cube[39] + cube[42]
        #Set Back Side
        cube[20] = BotS[2]
        cube[23] = BotS[1]
        cube[26] = BotS[0]
        #Set Bottom
        cube[45] = FrontS[2]
        cube[48] = FrontS[1]
        cube[51] = FrontS[0]
        #Set Front
        cube[0] = TopS[0]
        cube[3] = TopS[1]
        cube[6] = TopS[2]
        #Set Top
        cube[36] = BackS[0]
        cube[39] = BackS[1]
        cube[42] = BackS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
    if(parms['side'] == 'L'):
        cube = list(parms['cube'])
        #Back Side Values That Change
        BackS = cube[20] + cube[23] + cube[26]
        #Bottom Side Values That Change
        BotS = cube[45] + cube[48] + cube[51]
        #Front Side Values That Change
        FrontS = cube[0] + cube[3] + cube[6]
        #Top Side Values That Change
        TopS = cube[36] + cube[39] + cube[42]
        #Set Back Side
        cube[20] = TopS[2]
        cube[23] = TopS[1]
        cube[26] = TopS[0]
        #Set Bottom
        cube[45] = BackS[2]
        cube[48] = BackS[1]
        cube[51] = BackS[0]
        #Set Front
        cube[0] = BotS[0]
        cube[3] = BotS[1]
        cube[6] = BotS[2]
        #Set Top
        cube[36] = FrontS[0]
        cube[39] = FrontS[1]
        cube[42] = FrontS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
##END
def TopFaceRotate(parms): 
    if(parms['side'] == 't'):
        cube = list(parms['cube'])
        #Back Side Values That Change
        BackS = cube[18] + cube[19] + cube[20]
        #Left Side Values That Change
        LeftS = cube[27] + cube[28] + cube[29]
        #Front Side Values That Change
        FrontS = cube[0] + cube[1] + cube[2]
        #Right Side Values That Change
        RightS = cube[9] + cube[10] + cube[11]
        #Set Back Side
        cube[18] = LeftS[0]
        cube[19] = LeftS[1]
        cube[20] = LeftS[2]
        #Set Left
        cube[27] = FrontS[0]
        cube[28] = FrontS[1]
        cube[29] = FrontS[2]
        #Set Front
        cube[0] = RightS[0]
        cube[1] = RightS[1]
        cube[2] = RightS[2]
        #Set Right
        cube[9] = BackS[0]
        cube[10] = BackS[1]
        cube[11] = BackS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
    if(parms['side'] == 'T'):
        cube = list(parms['cube'])
        #Back Side Values That Change
        BackS = cube[18] + cube[19] + cube[20]
        #Left Side Values That Change
        LeftS = cube[27] + cube[28] + cube[29]
        #Front Side Values That Change
        FrontS = cube[0] + cube[1] + cube[2]
        #Right Side Values That Change
        RightS = cube[9] + cube[10] + cube[11]
        #Set Back Side
        cube[18] = RightS[0]
        cube[19] = RightS[1]
        cube[20] = RightS[2]
        #Set Left
        cube[27] = BackS[0]
        cube[28] = BackS[1]
        cube[29] = BackS[2]
        #Set Front
        cube[0] = LeftS[0]
        cube[1] = LeftS[1]
        cube[2] = LeftS[2]
        #Set Right
        cube[9] = FrontS[0]
        cube[10] = FrontS[1]
        cube[11] = FrontS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
##END

def BottomFaceRotate(parms):
    if(parms['side'] == 'u'):
        cube = list(parms['cube'])
        #Back Side Values That Change
        BackS = cube[24] + cube[25] + cube[26]
        #Left Side Values That Change
        LeftS = cube[33] + cube[34] + cube[35]
        #Front Side Values That Change
        FrontS = cube[6] + cube[7] + cube[8]
        #Right Side Values That Change
        RightS = cube[15] + cube[16] + cube[17]
        #Set Back Side
        cube[24] = RightS[0]
        cube[25] = RightS[1]
        cube[26] = RightS[2]
        #Set Left
        cube[33] = BackS[0]
        cube[34] = BackS[1]
        cube[35] = BackS[2]
        #Set Front
        cube[6] = LeftS[0]
        cube[7] = LeftS[1]
        cube[8] = LeftS[2]
        #Set Right
        cube[15] = FrontS[0]
        cube[16] = FrontS[1]
        cube[17] = FrontS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
    if(parms['side'] == 'U'):
        cube = list(parms['cube'])
        #Back Side Values That Change
        BackS = cube[24] + cube[25] + cube[26]
        #Left Side Values That Change
        LeftS = cube[33] + cube[34] + cube[35]
        #Front Side Values That Change
        FrontS = cube[6] + cube[7] + cube[8]
        #Right Side Values That Change
        RightS = cube[15] + cube[16] + cube[17]
        #Set Back Side
        cube[24] = LeftS[0]
        cube[25] = LeftS[1]
        cube[26] = LeftS[2]
        #Set Left
        cube[33] = FrontS[0]
        cube[34] = FrontS[1]
        cube[35] = FrontS[2]
        #Set Front
        cube[6] = RightS[0]
        cube[7] = RightS[1]
        cube[8] = RightS[2]
        #Set Right
        cube[15] = BackS[0]
        cube[16] = BackS[1]
        cube[17] = BackS[2]
        #Concatenating List Back Together
        Separator = ''
        return Separator.join(cube)
##END

def IntegrityCheck(parms):
    #Sha256 Conversion
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    #Integrity Key Check
    if(parms['integrity'] != IntegrityKey):
        return {'status': 'error: bad integrity key'}
    return dict()
##END

def CubeValidation(parms):
    result = dict()
    #Distinct Elements Check
    result = _check._CubeDistinctCheck(parms)
    if(result != dict()):
        return result
    #Invalid Corner Check
    #TopLeft Corner
    result = _check._TopLeftCornerCheck(parms)
    if(result != dict()):
        return result
    #TopRight Corner
    result = _check._TopRightCornerCheck(parms)
    if(result != dict()):
        return result
    #BottomRight Corner
    result = _check._BottomRightCornerCheck(parms)
    if(result != dict()):
        return result
    #BottomLeft Corner
    result = _check._BottomLeftCornerCheck(parms)
    if(result != dict()):
        return result
    #Invalid Edge Check
    result = _check._EdgeCheck(parms)
    if(result != dict()):
        return result
    return dict()
##END

def SideParmCheck(parms):
    ValidSides = ['f', 'F', 'r', 'R', 'b', 'B', 'l', 'L', 't', 'T', 'u', 'U']
    if(parms['side'] not in ValidSides):
        return {'status': 'error: bad side'}
    if(parms['side'] == ''):
        return {'status': 'error: blank side input'}
    return dict()
    


