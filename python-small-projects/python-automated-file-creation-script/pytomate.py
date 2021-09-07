import os

def change_path(desired_path):
    try:
    # Change the current working Directory    
        os.chdir(desired_path)
        print("Directory located Successfully")
    except OSError:
        print("Can't change the Current Working Directory") 

def next_path(path,path_pattern):
    
    """
    Finds the next free path in an sequentially named list of files

    e.g. path_pattern = 'file-%s.py':

    file-1.py
    file-2.py
    file-3.py

    Runs in log(n) time where n is the number of existing files in sequence
    """
    
    change_path(path)

    i = 1

    # First do an exponential search
    while os.path.exists(path_pattern % i):
        i = i * 2

    # Result lies somewhere in the interval (i/2..i]
    # We call this interval (a..b] and narrow it down until a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2 # interval midpoint
        a, b = (c, b) if os.path.exists(path_pattern % c) else (a, c)

    return path_pattern % b



folderPath = input("Enter folder Path: \n")
startingNumber = int(input("Enter the starting number: \n"))
endingNumber = int(input("Enter the ending number: \n"))
prefixName = input("Enter the file prefix: \n")


for i in range(startingNumber,endingNumber+1):
    with open(next_path(folderPath,prefixName + '-%s.py'), 'w'):
        pass