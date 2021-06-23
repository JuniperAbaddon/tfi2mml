import sys
import os
from tkinter import Tk   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes=[(".tfi files", "*.tfi")]) # show an "Open" dialog box and return the path to the selected file
file = os.path.split(filename)
filebase = os.path.splitext(file[1])

f = open(file[1], "br")

sys.stdout = open(filebase[0]+".txt", "w")

# algorithm and feedback #
f.seek(0)
alg = str(ord(f.read(1)))

f.seek(1)
fb = str(ord(f.read(1)))

print("@1 fm ; " + filebase[0])
print(";	ALG  FB")

print("     " + alg.rjust(2) + ' ' + fb.rjust(3))

print(";	 AR  DR  SR  RR  SL  TL  KS  ML  DT SSG")

# offset of 2 puts us past the algo and fb, at op0 mult
offset=2

# op offsets #

# [AR,DR,SR,RR,SL,TL,KS,ML,DT,SSG]
opoffsets = [4,5,6,7,8,2,3,0,1,9]
algoffsets = [0,2,1,3]

# main loop #
i=0
x=0
while x < 4:
    i=0
    offset = 2 + (algoffsets[x]*10)
    print("	", end="")
    while i < 10:
        seekoffset=offset+opoffsets[i]
        f.seek(seekoffset)
        print(str(ord(f.read(1))).rjust(3) + " ", end="")
        i+=1
    print("; OP"+str(x))
    x+=1



sys.stdout.close()

f.close()

"""
example from ctrmml guide:
@1 fm ; finger bass
;	ALG  FB
	  3   0
;	 AR  DR  SR  RR  SL  TL  KS  ML  DT SSG
	 31   0  19   5   0  23   0   0   0   0 ; OP1 (M1)
	 31   6   0   4   3  19   0   0   0   0 ; OP2 (C1)
	 31  15   0   5   4  38   0   4   0   0 ; OP3 (M2)
	 31  27   0  11   1   0   0   1   0   0 ; OP4 (C2)
	  0 ; TRS (optional)
"""