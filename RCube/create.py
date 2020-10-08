import hashlib

def _create(parms):
    
    if(len(parms['faces']) != 6):
        return {'status': 'error: bad length'}
    
    for char in parms['faces']:
        if(parms['faces'].count(char) > 1):
            return {'status': 'error: duplicate'}
    
    faces = str(parms['faces'])
    
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
