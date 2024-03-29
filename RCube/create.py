'''
Created on Oct 7, 2020

@author: Chase Dumbacher
'''
import hashlib

def _create(parms):
    if('faces' not in parms):
        parms['faces'] = 'gybwro'
    if(parms['faces'] == None):
        parms['faces'] = 'gybwro'
    if(len(parms['faces']) != 6):
        return {'status': 'error: bad length'}
    
    for char in parms['faces']:
        if(parms['faces'].count(char) > 1):
            return {'status': 'error: duplicate'}
    faces = str(parms['faces'])
    
    cube = ""
    for face in faces:
        for numOfFaces in range(9):
            cube += str(face)
    ByteCube = bytearray(cube,'utf8')
    Sha256 = hashlib.sha256(ByteCube).hexdigest()
    Sha256 = Sha256.upper()
    result = {'cube': cube, 'integrity': Sha256, 'status': 'ok'}
    return result
