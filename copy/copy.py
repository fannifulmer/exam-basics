import sys
#import shutil
# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

def arguments():
    if len(sys.argv) == 1:
        print("copy [source] [destination]")
    elif len(sys.argv) != 3:
        print("No destination provided")
    else:
        try:
            file_from = open(sys.argv[1], 'r+')
            file_copy = file_from.read()
            file_to = open(sys.argv[2], 'w')
            file_to.write(str(file_copy))
        except IOError:
            print("File does not exist")

arguments()
