import hashlib

def _check(parms):
    status = 'unknown'
    firstSpot = ''
    midSpot = ''
    cornerSpot = ''
    DistinctElem = []
    counter = 0
    faceIndex = 1
    FullCheck = True
    SpotCheck = True
    CrossCheck = True
    #Parms/Sad Checks
    
    #Missing Cube Parm Check
    if('cube' not in parms):
        return {'status': 'error no cube op'}
    #Missing Cube Value Check
    if(parms['cube'] == None):
        return {'status': 'error missing cube'}
    #Proper Cube Length Check
    if(len(parms['cube']) != 54):
        return {'status': 'error incorrect cube size'}
    #Distinct Elements Check
    for elements in parms['cube']:
        DistinctElem.append(elements)
    DistinctElem = list(set(DistinctElem))
    if(len(DistinctElem) != 6):
        return {'status': 'error non-distinct cube'}
    #9 Of Each Distinct Element Check
    ElementCounter = [0,0,0,0,0,0]
    for element in parms['cube']:
        i = 0
        for DistElements in DistinctElem:
            if(element == DistElements):
                ElementCounter[i] += 1
            i += 1
    for Counter in ElementCounter:
        if(Counter != 9):
            return {'status': 'error lacking 9 elements of each distinct'}
    #Sha256 Conversion
    ByteCube = bytearray(parms['cube'],'utf8')
    IntegrityKey = hashlib.sha256(ByteCube).hexdigest()
    IntegrityKey = IntegrityKey.upper()
    #Integrity Key Check
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