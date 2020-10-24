import hashlib

def _check(parms):
    status = ''
    firstSpot = ''
    midSpot = parms['cube'][4]
    counter = 0
    FullCheck = True
    SpotCheck = False
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    if(parms['integrity'] != IntegrityKey):
        return {'status': 'error bad integrity key'}
    for spot in parms['cube']:
        if(counter == 0 or counter % 9 == 0):
            firstSpot = spot
            midSpot = parms['cube'][counter + 4]
        if(spot != midSpot):
            SpotCheck = True
        if(spot != firstSpot):
            FullCheck = False
        counter += 1
    if(FullCheck == True):
        status = 'full'
    if(SpotCheck == True):
        status = 'spots'
    result = {'status': status}
    return result