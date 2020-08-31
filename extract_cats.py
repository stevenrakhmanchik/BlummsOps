read = open("output.txt",'r')
lines = read.readlines()
count = 0
data = []
for x in lines:
    if not(x=='\n') and not(x==' \n'):
        x = x.strip(' \n')
        if not(x==' '):
            data.append(x)
lines = data
for x in lines:
    if "CATEGORY TABLE OF CONTENTS:" in x:
        lines = lines[count::]
        break
    count+=1
lines = lines[3:11]
print(lines)
