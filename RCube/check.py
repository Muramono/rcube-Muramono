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
    #Missing Key Value
    if(parms['integrity'] == None):
        return {'status': 'error missing key value'}
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
    #Non-Distinct Middle Check
    MiddleEle = [(parms['cube'][4]), (parms['cube'][13]), (parms['cube'][22]), (parms['cube'][31]), (parms['cube'][40]), (parms['cube'][49])]
    DistinctMiddleEle = []
    [DistinctMiddleEle.append(x) for x in MiddleEle if x not in DistinctMiddleEle]
    if(len(DistinctMiddleEle) != 6):
        return {'status': 'error non-distinct middle'}
    #Invalid Corner Check
    
    #TopLeft Corner
    #Front To Top Comparison
    if(parms['cube'][0] == MiddleEle[0]  and parms['cube'][42] == MiddleEle[2] or parms['cube'][42] == MiddleEle[0]  and parms['cube'][0] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][0] == MiddleEle[4]  and parms['cube'][42] == MiddleEle[5] or parms['cube'][42] == MiddleEle[4]  and parms['cube'][0] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][0] == MiddleEle[1]  and parms['cube'][42] == MiddleEle[3] or parms['cube'][42] == MiddleEle[1]  and parms['cube'][0] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #Front To Left Comparison
    if(parms['cube'][0] == MiddleEle[0]  and parms['cube'][29] == MiddleEle[2] or parms['cube'][29] == MiddleEle[0]  and parms['cube'][0] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][0] == MiddleEle[4]  and parms['cube'][29] == MiddleEle[5] or parms['cube'][29] == MiddleEle[4]  and parms['cube'][0] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][0] == MiddleEle[1]  and parms['cube'][29] == MiddleEle[3] or parms['cube'][29] == MiddleEle[1]  and parms['cube'][0] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #TopRight Corner
    #Front To Top Comparison
    if(parms['cube'][2] == MiddleEle[0]  and parms['cube'][44] == MiddleEle[2] or parms['cube'][44] == MiddleEle[0]  and parms['cube'][2] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][2] == MiddleEle[4]  and parms['cube'][44] == MiddleEle[5] or parms['cube'][44] == MiddleEle[4]  and parms['cube'][2] == MiddleEle[5] ):
        return {'status': 'error impossible corner'}
    if(parms['cube'][2] == MiddleEle[1]  and parms['cube'][44] == MiddleEle[3] or parms['cube'][44] == MiddleEle[1]  and parms['cube'][2] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #Front To Right Comparison
    if(parms['cube'][2] == MiddleEle[0]  and parms['cube'][9] == MiddleEle[2] or parms['cube'][9] == MiddleEle[0]  and parms['cube'][2] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][2] == MiddleEle[4]  and parms['cube'][9] == MiddleEle[5] or parms['cube'][9] == MiddleEle[4]  and parms['cube'][2] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][2] == MiddleEle[1]  and parms['cube'][9] == MiddleEle[3] or parms['cube'][9] == MiddleEle[1]  and parms['cube'][2] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #BottomRight Corner
    #Front To Under Comparison
    if(parms['cube'][8] == MiddleEle[0]  and parms['cube'][47] == MiddleEle[2] or parms['cube'][47] == MiddleEle[0]  and parms['cube'][8] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][8] == MiddleEle[4]  and parms['cube'][47] == MiddleEle[5] or parms['cube'][47] == MiddleEle[4]  and parms['cube'][8] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][8] == MiddleEle[1]  and parms['cube'][47] == MiddleEle[3] or parms['cube'][47] == MiddleEle[1]  and parms['cube'][8] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #Front To Right Comparison
    if(parms['cube'][8] == MiddleEle[0]  and parms['cube'][15] == MiddleEle[2] or parms['cube'][15] == MiddleEle[0]  and parms['cube'][8] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][8] == MiddleEle[4]  and parms['cube'][15] == MiddleEle[5] or parms['cube'][15] == MiddleEle[4]  and parms['cube'][8] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][8] == MiddleEle[1]  and parms['cube'][15] == MiddleEle[3] or parms['cube'][15] == MiddleEle[1]  and parms['cube'][8] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #BottomLeft Corner
    #Front To Under Comparison
    if(parms['cube'][6] == MiddleEle[0]  and parms['cube'][45] == MiddleEle[2] or parms['cube'][45] == MiddleEle[0]  and parms['cube'][6] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][6] == MiddleEle[4]  and parms['cube'][45] == MiddleEle[5] or parms['cube'][45] == MiddleEle[4]  and parms['cube'][6] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][6] == MiddleEle[1]  and parms['cube'][45] == MiddleEle[3] or parms['cube'][45] == MiddleEle[1]  and parms['cube'][6] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #Front To Left Comparison
    if(parms['cube'][8] == MiddleEle[0]  and parms['cube'][35] == MiddleEle[2] or parms['cube'][35] == MiddleEle[0]  and parms['cube'][8] == MiddleEle[2]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][8] == MiddleEle[4]  and parms['cube'][35] == MiddleEle[5] or parms['cube'][35] == MiddleEle[4]  and parms['cube'][8] == MiddleEle[5]):
        return {'status': 'error impossible corner'}
    if(parms['cube'][8] == MiddleEle[1]  and parms['cube'][35] == MiddleEle[3] or parms['cube'][35] == MiddleEle[1]  and parms['cube'][8] == MiddleEle[3]):
        return {'status': 'error impossible corner'}
    #Invalid Edge Check
    
    #Top Front To Top Comparison
    if(parms['cube'][1] == MiddleEle[0]  and parms['cube'][43] == MiddleEle[2] or parms['cube'][1] == MiddleEle[0]  and parms['cube'][43] == MiddleEle[2]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][1] == MiddleEle[4]  and parms['cube'][43] == MiddleEle[5] or parms['cube'][1] == MiddleEle[4]  and parms['cube'][43] == MiddleEle[5]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][1] == MiddleEle[1]  and parms['cube'][43] == MiddleEle[3] or parms['cube'][1] == MiddleEle[1]  and parms['cube'][43] == MiddleEle[3]):
        return {'status': 'error impossible edge'}
    #Right Front To Right Comparison
    if(parms['cube'][5] == MiddleEle[0]  and parms['cube'][12] == MiddleEle[2] or parms['cube'][12] == MiddleEle[0]  and parms['cube'][5] == MiddleEle[2]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][5] == MiddleEle[4]  and parms['cube'][12] == MiddleEle[5] or parms['cube'][12] == MiddleEle[4]  and parms['cube'][5] == MiddleEle[5]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][5] == MiddleEle[1]  and parms['cube'][12] == MiddleEle[3] or parms['cube'][12] == MiddleEle[1]  and parms['cube'][5] == MiddleEle[3]):
        return {'status': 'error impossible edge'}
    #Bottom Front To Under Comparison
    if(parms['cube'][7] == MiddleEle[0]  and parms['cube'][46] == MiddleEle[2] or parms['cube'][46] == MiddleEle[0]  and parms['cube'][7] == MiddleEle[2]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][7] == MiddleEle[4]  and parms['cube'][46] == MiddleEle[5] or parms['cube'][46] == MiddleEle[4]  and parms['cube'][7] == MiddleEle[5]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][7] == MiddleEle[1]  and parms['cube'][46] == MiddleEle[3] or parms['cube'][46] == MiddleEle[1]  and parms['cube'][7] == MiddleEle[3]):
        return {'status': 'error impossible edge'}
    #Left Front To Left Comparison
    if(parms['cube'][3] == MiddleEle[0]  and parms['cube'][32] == MiddleEle[2] or parms['cube'][32] == MiddleEle[0]  and parms['cube'][3] == MiddleEle[2]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][3] == MiddleEle[4]  and parms['cube'][32] == MiddleEle[5] or parms['cube'][32] == MiddleEle[4]  and parms['cube'][3] == MiddleEle[5]):
        return {'status': 'error impossible edge'}
    if(parms['cube'][3] == MiddleEle[1]  and parms['cube'][32] == MiddleEle[3] or parms['cube'][32] == MiddleEle[1]  and parms['cube'][3] == MiddleEle[3]):
        return {'status': 'error impossible edge'}
    ## Cube Face Order F, R, B, L, T, U
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