import hashlib

def _create(parms):
    faces = "111111111222222222333333333444444444555555555666666666"
    Sha256 = hashlib.sha256(b"111111111222222222333333333444444444555555555666666666").hexdigest()
    Sha256 = Sha256.upper()
    result = {'cube': faces, 'integrity': Sha256}
    return result
