import hashlib

def _check(parms):
    status = ''
    firstSpot = ''
    midSpot = ''
    cornerSpot = ''
    counter = 0
    FullCheck = True
    SpotCheck = True
    CrossCheck = True
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    if(parms['integrity'] != IntegrityKey):
        return {'status': 'error bad integrity key'}
    for spot in parms['cube']:
        #Sets Tracked spots to the appropriate value of the current face
        if(counter == 0 or counter % 9 == 0):
            firstSpot = spot
            midSpot = parms['cube'][counter + 4]
            cornerSpot = spot
        #Checks to see if the odd and not the middle spot are equal to the corner spot(s) **CROSS CHECK**
        if( ( counter + 1) % 2 != 0 and (counter + 1) % 5 != 0):
            if(spot != cornerSpot):
                CrossCheck = False
        #Checks if the even spots or middle spot is equal to the middle **CROSS CHECK**
        if( (counter + 1) % 2 == 0 and (counter + 1) % 5 == 0):
            if(spot != midSpot):
                CrossCheck = False
        #Checks if the middle spot is equal to any outer spots **SPOTS CHECK**
        if( (counter + 1) % 5 != 0):
            if(spot == midSpot):
                SpotCheck = False
        if( (counter + 1) % 5 == 0):
            if(spot != firstSpot):
                SpotCheck = False
        #Checks to see if any spot is different **FULL CHECK**
        if(spot != firstSpot):
            FullCheck = False
        counter += 1
    if(FullCheck == True):
        status = 'full'
    if(SpotCheck == True):
        status = 'spots'
    result = {'status': status}
    return result