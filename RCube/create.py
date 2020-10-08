import hashlib

def _create(parms):
    
    faces = str(parms['faces'])
    
    if(faces.length() != 6):
        return {'status': 'error: bad length'}
    
    cube = ""
    for i in faces:
        for x in range(9):
            cube += str(i)
    #print(cube)
    ByteCube = bytearray(cube,'utf8')
    Sha256 = hashlib.sha256(ByteCube).hexdigest()
    Sha256 = Sha256.upper()
    result = {'cube': cube, 'integrity': Sha256}
    return result

_create({'op': 'create', 'faces': '123457'})
