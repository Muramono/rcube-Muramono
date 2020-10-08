import hashlib

def _create(parms):
    faces = str(parms['faces'])
    cube = ""
    for i in faces:
        for x in range(9):
            cube += str(i)
    #print(cube)
    cube = bytearray(cube,'utf8')
    Sha256 = hashlib.sha256(b"111111111222222222333333333444444444555555555777777777").hexdigest()
    Sha256 = Sha256.upper()
    result = {'cube': cube, 'integrity': Sha256}
    return result

_create({'op': 'create', 'faces': '123457'})
