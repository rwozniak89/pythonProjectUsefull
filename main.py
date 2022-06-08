#Pograming is Usefull
#To solve this challenge You need to know, how many lines in file have
#the number of 0's which is a multiple of 3 or the numbers of 1s is a multiple of 2.
#Tips: Flag format: "flag{number_of_lines}"
#"flag{9938}"
#flag{6662}
import re
f = open("data.dat", "r")
#print(f.read())
i=0
counter0 = 0
counter1 = 0
counter2 = 0
for x in f:
    i=i+1
    str0 = ""
    str1 = ""
    for c in x:
        if (c == "0"):
            str0+=c
        if (c == "1"):
            str1 += c
    if (str0.find("000") != -1) or (str1.find("11") != -1):
        if(len(str0) % 3 ==0):
            counter2 = counter2 + 1
        elif (len(str1) % 2 ==0):
            counter2 = counter2 + 1


    if (x.find("000") != -1) or (x.find("11") != -1):
        counter0 = counter0 + 1
    #if x.find("1") != -1:
    #    counter1 = counter1 + 1
    print(x)
print(f"i: {i}")
print(f"counter0: {counter0}")
print(f"counter2: {counter2}")


#i: 10000
#counter0: 9999
#counter1: 9998

#counter0: 9938

