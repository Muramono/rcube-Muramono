import hashlib
import RCube.check as _check

def _rotate(parms):
    result = dict()
    status = ''
    cube = ''
    integrityKey = ''
    
    #Input Parms Check
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
        return cube
    return
##END

def RightFaceRotate():
    return
##END

def BackFaceRotate():
    return
##END

def TopFaceRotate(): 
    return
##END

def BottomFaceRotate():
    return
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


