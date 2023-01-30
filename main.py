"""
Name: Kevin Wander
Email: kevin.wander30@myhunter.cuny.edu
Resources:  My notes
I attended lecture today.
Row: Last Row
Seat:  101
"""

#takes name of file as input, makes dictionary of the lines of the file.


#name = input("Enter file name, with extension: ")

def make_dict(filename, sep=': '):
    dict = {}
    with open(filename) as md:
        counter = 0
        for line in md:
            dict[counter] = line
            counter+=1
    return dict

print(filename())

