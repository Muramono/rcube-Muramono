def Testing():
    testList = [[1,2,3],[4,5,6],[7,8,9]] 
    print("Pre Transpose", testList)
    transposeList = zip(*testList)
    print("Tranposed", *transposeList)
    
Testing()