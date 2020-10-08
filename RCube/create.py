import hashlib

def _create(parms):
    faces = '111111111222222222333333333444444444555555555666666666'
    Sha256 = hashlib.sha256(faces).hexdigest()
    result = {'cube': faces, 'integrity': Sha256}
    return result
