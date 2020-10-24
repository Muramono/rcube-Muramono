def _check(parms):
    status = ''
    firstSpot = ''
    counter = 0
    FullCheck = True
    for spot in parms['cube']:
        if(counter == 0 or counter % 9 == 0):
            firstSpot = spot
        if(spot != firstSpot):
            FullCheck = False
    if(FullCheck == True):
        status = 'full'
    result = {'status': status}
    return result
