#!/usr/bin/env python3

def copy_file(infilename, outfilename):
    infile = open(infilename)
    outfile = open(outfilename,'w')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()

#copy_file("binary-tree.py","pepe")
###########################################
def print_file(filename):
    infile = open(filename)
    for line in infile:
        print(line, end="")
    infile.close()

# print_file("binary-tree.py")
##############################################
def write_to_file(filename, myname, myage, major):
    outfile = open(filename,'w')
    name = "My name is " + myname + "\n"
    outfile.write(name)
    age = "My age is " + str(myage) + "\n"
    outfile.write(age)
    grad = "I am majoring in " + major + "\n"
    outfile.write(grad)
    outfile.close()

write_to_file("namefile.txt","Santiago",47,"Computers")
