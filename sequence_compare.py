# Author: Jay Chen
# jc01@berkeley.edu
# Mar 12 2023
##################Import#########################
from datetime import datetime
now = datetime.now()
time = now.strftime("%m/%d/%Y %H:%M:%S")

#################Input###########################
# Prompt for sequence and index
index = int(input("Index: "))
sequence1 = input("Sequence1: ")
sequence2 = input("Sequence2: ")
nick_name = input("Nick_name: ")
k = 0

#################file###########################
# Open a file, and write into the log
file = open("sequence_compare.txt", "a")
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
        if sequence1[i] != sequence2[i]:
            k += 1
            file.write(f"difference at position {i + index}: {sequence1[i]} vs. {sequence2[i]} \n")
            print(f"difference at position {i + index}: {sequence1[i]} vs. {sequence2[i]}")
    if k == 0:
        print("No differnece between these two sequences")
        file.write("No differnece between these two sequences")
        file.write("\n")

print("Number of differences: " + str(k))
file.write("Number of differences: ")
file.write(str(k))
file.write("\n")
file.write("\n")
file.close()
