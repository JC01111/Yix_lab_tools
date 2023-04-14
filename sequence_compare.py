# Author: Jay Chen
# jc01@berkeley.edu
# Mar 12 2023
##################Import#########################
from datetime import datetime
now = datetime.now()
time = now.strftime("%m/%d/%Y %H:%M:%S")
file = open("sequence_compare.txt", "a")
#################Input###########################
# Prompt for sequence and index
index = int(input("Index: "))
sequence1 = input("Sequence1: ")
sequence2 = input("Sequence2: ")
k = 0

# Check if two sequences have the same length
if len(sequence1) != len(sequence2):
    file.write(f"{time}\nIndex: {index}\nsequence1: {sequence1}\nsequence2: {sequence2}\n")
    file.write(f"Error: sequences are not the same length \n\n")
    raise Exception("sequences are not the same length")
else:
    nick_name = input("Nick_name (optional): ")
    file.write(f"{time} {nick_name}\nIndex: {index}\nsequence1: {sequence1}\nsequence2: {sequence2}\n")
    # Loop over each base pair in the sequences and compare them
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            k += 1
            file.write(f"difference at position {i + index}: {sequence1[i]} vs {sequence2[i]} \n")
            print(f"difference at position {i + index}: {sequence1[i]} vs {sequence2[i]}")

print("Number of differences: " + str(k))
file.write(f"Number of differences: {str(k)}\n\n")
file.close()
