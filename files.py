# file read

fileHandle = open('filename.txt')
for line in fileHandle:
    line = line.rstrip()
    if not '@icloud.com' in line:
        continue
    print(line)

    

