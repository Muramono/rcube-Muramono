import hashlib

def _check(parms):
    status = ''
    firstSpot = ''
    midSpot = ''
    counter = 0
    FullCheck = True
    SpotCheck = True
    midIndexs = [5,14,19,24,29,34]
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    if(parms['integrity'] != IntegrityKey):
        return {'status': 'error bad integrity key'}
    for spot in parms['cube']:
        if(counter == 0 or counter % 9 == 0):
            firstSpot = spot
        if(counter in midIndexs):
            midSpot = spot
        if(spot == midSpot):
            SpotCheck = False
        if(spot != firstSpot):
            FullCheck = False
        counter += 1
    if(FullCheck == True):
        status = 'full'
    if(SpotCheck == True):
        status = 'spots'
    result = {'status': status}
    return result
