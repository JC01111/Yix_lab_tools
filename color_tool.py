# Author: Jay Chen
# jc01@berkeley.edu
# Mar 13 2023
##################Import########################
# Import
from datetime import datetime
now = datetime.now()
time = now.strftime("%m/%d/%Y %H:%M:%S")
# Create file
file = open("color_tool.txt", "a")

#################Input##########################
# Prompt for info
chain_id1 = input("Chain_ID_1 (e.g, 1/A): ")
chain_id2 = input("Chain_ID_2 (e.g, 1/A): ")
color1 = input("Atom_color1: ")
color2 = input("Atom_color2: ")
style = input("Style of Atoms (ball): ")
# Prompt for sequence and index
index = int(input("Index: "))
sequence1 = input("Sequence1: ")
sequence2 = input("Sequence2: ")
nick_name = input("Nick_name: ")
k = -1
count = 0

#################file###########################
# Write into txt file
file.write(time)
file.write(" ")
file.write(nick_name)
file.write("\n")
file.write("Index: ")
file.write(str(index))
file.write("\n")
file.write("sequence1: ")
file.write(sequence1)
file.write("\n")
file.write("sequence2: ")
file.write(sequence2)
file.write("\n")

##################Algorithm#####################
# Check if two sequences have the same length
if len(sequence1) != len(sequence2):
    file.write("Error: sequences are not the same length")
    file.write("\n")
    print("Error: sequences are not the same length")
else:
    # Loop over each base pair in the sequences and compare them
    for i in range(len(sequence1)):
        k += 1
        if sequence1[i] != sequence2[i]:
            count += 1
            file.write(str("select #" + chain_id1 + ":" + str(k + index) + ";" + " color sel " + color1 + "; show sel atoms;" + "style sel " + style + "\n"))
            file.write(str("select #" + chain_id2 + ":" + str(k + index) + ";" + " color sel " + color2 + "; show sel atoms;" + "style sel " + style + "\n"))
            print(str("select #" + chain_id1 + ":" + str(k + index) + ";" + " color sel " + color1 + "; show sel atoms;" + "style sel " + style))
            print(str("select #" + chain_id2 + ":" + str(k + index) + ";" + " color sel " + color2 + "; show sel atoms;" + "style sel " + style))
    if count == 0:
        print("No differnece between these two sequences")
        file.write("No differnece between these two sequences")
        file.write("\n")

print("Number of differences: " + str(count))
file.write("Number of differences: " + str(count))
file.write("\n")
file.write("\n")
file.close()
