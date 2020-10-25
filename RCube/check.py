import hashlib

def _check(parms):
    status = 'unknown'
    firstSpot = ''
    midSpot = ''
    cornerSpot = ''
    counter = 0
    faceIndex = 1
    FullCheck = True
    SpotCheck = True
    CrossCheck = True
    #Parms/Sad Checks
    if(parms['cube'] == None):
        return {'status': 'error missing cube'}
    #Sha256 Conversion
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    #Integrity Key Check
    if('cube' not in parms):
        return {'status': 'error no cube op'}
    if(parms['integrity'] != IntegrityKey):
        return {'status': 'error bad integrity key'}
    # Cube Valid Status Checks
    for spot in parms['cube']:
        #Sets Tracked spots to the appropriate value of the current face
        if(counter == 0 or counter % 9 == 0):
            firstSpot = spot
            midSpot = parms['cube'][counter + 4]
            cornerSpot = spot
        #Checks to see if the odd and not the middle spot are equal to the corner spot(s) **CROSS CHECK**
        if( (faceIndex) % 2 != 0 and (faceIndex) % 5 != 0):
            if(spot != cornerSpot):
                CrossCheck = False
        #Checks if the even spots or middle spot is equal to the middle **CROSS CHECK**
        if( (faceIndex) % 2 == 0 or (faceIndex) % 5 == 0):
            if(spot != midSpot):
                CrossCheck = False
        #Check to make sure the corner and non corner spots are equal **CROSS CHECK**
        if(midSpot == firstSpot):
            CrossCheck = False
        #Checks if the middle spot is equal to any outer spots **SPOTS CHECK**
        if( (faceIndex) % 5 != 0):
            if(spot == midSpot):
                SpotCheck = False
        #Checks if the all outer spots are equal. **SPOTS CHECK**
        if( (faceIndex) % 5 != 0):
            if(spot != firstSpot):
                SpotCheck = False
        #Checks to see if any spot is different **FULL CHECK**
        if(spot != firstSpot):
            FullCheck = False
        counter += 1
        faceIndex += 1
        if(faceIndex > 9):
            faceIndex = 1
    if(FullCheck == True):
        status = 'full'
    if(SpotCheck == True):
        status = 'spots'
    if(CrossCheck == True):
        status = 'crosses'
    result = {'status': status}
    return result