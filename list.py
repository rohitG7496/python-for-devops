import sys
import os

#command line argument to getting inputs
#folders = sys.argv[0]

#using inputs we can getting inputs from runtime or execution time
#number = input("provide number: ")
#print(number)

folders = input("provider folder names:").split()
#print (folders)

for folder in folders:
    files = os.listdir(folder)
    print("======= Print list of folder - " + folder + "=======")
    for file in files:
        print(file)

    
