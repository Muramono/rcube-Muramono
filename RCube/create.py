import hashlib

def _create(parms):
    faces = parms['faces']
    cube = ""
    for i in faces:
        for x in range(9):
            cube += x
    cube = bytearray(cube)
    Sha256 = hashlib.sha256(cube).hexdigest()
    Sha256 = Sha256.upper()
    result = {'cube': faces, 'integrity': Sha256}
    return result
