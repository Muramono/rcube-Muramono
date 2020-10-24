import hashlib

def _check(parms):
    status = ''
    firstSpot = ''
    midSpot = ''
    counter = 0
    FullCheck = True
    SpotCheck = False
    midIndexs = [4,13,18,23,28,33]
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    if(parms['integrity'] != IntegrityKey):
        return {'status': 'error bad integrity key'}
    for spot in parms['cube']:
        if(counter == 0 or counter % 9 == 0):
            firstSpot = spot
        if(counter in midIndexs):
            print("Spot Check")
            midSpot = spot
        if(spot != midSpot):
            SpotCheck = True
        if(spot != firstSpot):
            print("Full Check")
            FullCheck = False
        counter += 1
    if(FullCheck == True):
        status = 'full'
    if(SpotCheck == True):
        status = 'spots'
    result = {'status': status}
    return result

_check({'op': 'check', 'cube': 'rrrrbrrrryyyyryyyyoooogoooowwwwowwwwbbbbby', 'integrity': '103D576CB789BDAE083FBD95A05B5829009C465E388F9A8CFAD60B87CF6DD21A'})