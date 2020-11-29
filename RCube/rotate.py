import hashlib
import RCube.check as _check

def _rotate(parms):
    result = dict()
    status = ''
    cube = ''
    integritykey = ''
    
    #Check For Valid Key
    if(IntegrityCheck(parms) != dict()):
        return IntegrityCheck(parms)
    
    cube = parms['cube']
    status = 'rotate'
    integritykey = '546F560EB2D04BAA5F0F0EBB2F74EF9B0EC42B5EF005E2418B69671DAD467FCF'
    
    result = {'status': status, 'cube': cube, 'integrity': integritykey}
    return result

## Idea Transpose left and right side to get columns then swap them itertively 
def FrontFaceRotate():
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
    result = _.check._EdgeCheck(parms)
    if(result != dict()):
        return result
##END


