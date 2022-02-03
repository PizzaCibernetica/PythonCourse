score = input("Enter Score: ")
fs = float(score)

if fs > 1.0:
    print("Out of range... above")
    exit()
elif fs < 0:
    print("Oot of range... below")
    exit()
else:
    if fs >= 0.9:
        print("A") 
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    else:
        print("F")


# file read

#fileHandle = open('filename.txt')
#for line in fileHandle:
#    line = line.rstrip()
#    if not '@icloud.com' in line:
#        continue
#    print(line)
