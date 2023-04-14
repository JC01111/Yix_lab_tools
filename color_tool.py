# Author: Jay Chen
# jc01@berkeley.edu
# Mar 13 2023
##################Import########################
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
index = int(input("Index: "))
sequence1 = input("Sequence1: ")
sequence2 = input("Sequence2: ")
k = -1
count = 0

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
        k += 1
        if sequence1[i] != sequence2[i]:
            count += 1
            file.write(f"select #{chain_id1}:{k + index}; color sel {color1}; show sel atoms; style sel {style}\n")
            file.write(f"select #{chain_id2}:{k + index}; color sel {color2}; show sel atoms; style sel {style}\n")
            print(f"select #{chain_id1}:{k + index}; color sel {color1}; show sel atoms; style sel {style}")
            print(f"select #{chain_id2}:{k + index}; color sel {color2}; show sel atoms; style sel {style}")

print(f"Number of differences: {count}")
file.write(f"Number of differences: {count}\n\n")
file.close()
