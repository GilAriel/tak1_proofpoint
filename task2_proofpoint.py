import os
import hashlib
import sys

#Hashes each block of the file and aggregates everything to a single value
def fileToHash(filename):
    f = open(filename , 'rb')
    blockSize = 256
    sha256 = hashlib.sha256()
    data = f.read(blockSize)
    while data:
        sha256.update(data)
        data = f.read(blockSize)
    f.close()
    return sha256.digest()

#goes over the values of each key, if num of values is bigger than 1 means dups exist
def printDups(dictionary): 
    results = dictionary.values()
    for res in results:
        count = len(res)
        if len(res) >1:
            for sub in res:
                if count == 1:
                    print(sub)
                else:
                    print(sub + ", ", end='')
                    count -= 1
                
    
def findDups(originPath):
    dups = {}
    for dirPath, dirNames, fileNames in os.walk(originPath):            #os.walk return a triple
        for fName in fileNames:                                         #iterate over the files is the directory
            path = os.path.join(dirPath, fName)                         #get the full path
            hashOfFile = fileToHash(path)                               #hash the file, it is the key in the dictionary
            if hashOfFile in dups:
                dups[hashOfFile].append(path)                           #add duplicate
                
                
            else:
                dups[hashOfFile] = [path]                               #added as a list so can append other dup files to same key

    printDups(dups)



if __name__ == '__main__':  
    if os.path.exists(sys.argv[1]):  #verifies that the given folder exists in the filesystem
        findDups(sys.argv[1])
    else:
        print("Invalid path")
        sys.exit
            

    
